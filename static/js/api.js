// static/js/api.js
const API_BASE = '/api';

const auth = {
    save(data) {
        localStorage.setItem('ocms_access', data.access);
        localStorage.setItem('ocms_refresh', data.refresh);
        localStorage.setItem('ocms_role', data.role);
        localStorage.setItem('ocms_user', JSON.stringify(data.user));
    },
    logout() {
        localStorage.clear();
        window.location.href = '/login/';
    },
    isLoggedIn: () => !!localStorage.getItem('ocms_access'),
    role: () => localStorage.getItem('ocms_role'),
    getUser: () => JSON.parse(localStorage.getItem('ocms_user') || '{}')
};

const api = {
    async call(endpoint, method = 'GET', body = null) {
        const headers = { 'Content-Type': 'application/json' };
        const token = localStorage.getItem('ocms_access');
        if (token) headers['Authorization'] = `Bearer ${token}`;

        try {
            const res = await fetch(`${API_BASE}${endpoint}`, {
                method, headers, body: body ? JSON.stringify(body) : null
            });
            if (res.status === 401) auth.logout();
            return res;
        } catch (e) {
            console.error("API Error:", e);
            return { ok: false };
        }
    },

    async login(email, password) {
        const res = await fetch(`${API_BASE}/auth/login/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        const data = await res.json();
        if (res.ok) auth.save(data);
        return { ok: res.ok, ...data };
    },

    async register(full_name, email, password, role) {
        const res = await fetch(`${API_BASE}/auth/register/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ full_name, email, password, role })
        });
        const data = await res.json();
        return { ok: res.ok, ...data };
    }
};

// UI Global Helpers
function initNav() {
    if (auth.isLoggedIn()) {
        const user = auth.getUser();
        const avatar = document.getElementById('navAvatar');
        const logoutBtn = document.getElementById('navLogoutBtn');
        const loginBtn = document.getElementById('navLoginBtn');
        const signupBtn = document.getElementById('navSignupBtn');

        if (avatar) {
            avatar.style.display = 'flex';
            avatar.textContent = (user.full_name || 'U').split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2);
        }
        if (logoutBtn) {
            logoutBtn.style.display = 'block';
            logoutBtn.onclick = auth.logout;
        }
        if (loginBtn) loginBtn.style.display = 'none';
        if (signupBtn) signupBtn.style.display = 'none';
    }
}

function requireAuth() { if (!auth.isLoggedIn()) window.location.href = '/login/'; }

function redirectIfLoggedIn() {
    if (auth.isLoggedIn()) {
        const role = auth.role();
        if (role === 'ADMIN') window.location.href = '/admin-dashboard/';
        else if (role === 'INSTRUCTOR') window.location.href = '/instructor/';
        else window.location.href = '/dashboard/';
    }
}