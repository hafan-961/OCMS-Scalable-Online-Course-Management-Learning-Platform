const API_URL = "http://127.0.0.1:8000/api";

// Helper to save tokens
function saveTokens(access, refresh) {
    localStorage.setItem('access_token', access);
    localStorage.setItem('refresh_token', refresh);
}

// Helper to get headers with JWT
function getAuthHeaders() {
    const token = localStorage.getItem('access_token');
    return {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
    };
}

// Logout
function logout() {
    localStorage.clear();
    window.location.href = 'login.html';
}