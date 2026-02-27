# Online Course Management System (OCMS)

![Backend](https://img.shields.io/badge/Backend-Django%205.0-092e20?style=for-the-badge&logo=django)
![API](https://img.shields.io/badge/API-Django%20REST%20Framework-ff1709?style=for-the-badge&logo=django)
![Database](https://img.shields.io/badge/Database-PostgreSQL-336791?style=for-the-badge&logo=postgresql)
![Caching](https://img.shields.io/badge/Caching-Redis-DC382D?style=for-the-badge&logo=redis)
![Auth](https://img.shields.io/badge/Auth-JWT%20Stateless-black?style=for-the-badge&logo=json-web-tokens)

A high-performance, full-stack Learning Management System (LMS) built with a scalable backend-driven architecture. This system is optimized for PostgreSQL and leverages Redis caching to deliver ultra-fast response times for public course discovery.

---

## 📖 Project Overview

OCMS is designed to handle the full lifecycle of online learning. Students can browse, enroll, and track their learning progress via dynamic progress bars. Instructors have dedicated dashboards to manage their curricula, and administrators have access to platform-wide analytics.

---

## 🛠 Technical Stack

- **Backend:** Python, Django 5.0, Django REST Framework
- **Database:** PostgreSQL (Relational storage with optimized indexing)
- **Caching:** Redis (Mandatory caching for high-traffic API endpoints)
- **Authentication:** Stateless JWT (JSON Web Tokens) with a custom Authentication backend
- **Frontend:** Plain HTML5, CSS3 (Bootstrap 5), and Vanilla JavaScript (Fetch API)

> **Note:** Strictly follows the "No React" constraint.

---

## 🚀 Key Features

### 🔐 Authentication & Security
- **Stateless Auth:** Uses JWT Access and Refresh tokens for session management.
- **Custom User Model:** Implements role-based permissions (`STUDENT`, `INSTRUCTOR`, `ADMIN`).
- **CORS Protection:** Configured to secure API communication between the frontend and backend.

### 📚 Course Management
- **Hierarchical Structure:** `Category → Course → Module → Lecture`
- **Search & Filter:** Advanced filtering by difficulty level and SEO-friendly slugs for categories.
- **Optimized Performance:** Course list APIs are cached in Redis with a 15-minute TTL.

### 📈 Enrollment & Progress
- **Duplicate Prevention:** Unique database constraints prevent multiple enrollments in the same course.
- **Progress Logic:** Real-time calculation of student completion percentage based on lecture status.

### 📊 Admin Dashboard
- **Live Analytics:** Aggregated metrics for total users, courses, and enrollments.
- **Top Courses:** Identifying high-performing content through PostgreSQL window functions.

---

## 📂 Project Structure

```
ocms/
├── ocms/           # Main project configuration
├── accounts/       # Custom User models and JWT Auth logic
├── courses/        # Course content, Categories, Modules, Lectures
├── enrollments/    # Enrollment logic and Progress calculation
├── reviews/        # Student feedback and Rating system
├── dashboard/      # Admin analytics (PostgreSQL aggregations)
├── templates/      # Vanilla JS Frontend (HTML pages)
└── static/js/      # API handlers and Global Auth engine
```

---

## ⚙️ Installation & Setup

**1. Clone the repository:**
```bash
git clone <repo-url>
cd ocms
```

**2. Setup Virtual Environment:**
```bash
python -m venv env
source env/bin/activate   # Mac/Linux
# env\Scripts\activate    # Windows
```

**3. Install Dependencies:**
```bash
pip install django djangorestframework psycopg2-binary django-redis djangorestframework-simplejwt django-cors-headers
```

**4. Environment Configuration:**

Ensure PostgreSQL and Redis are running. Update the `DATABASES` and `CACHES` settings in `settings.py`.

**5. Initialize Database:**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

**6. Run Server:**
```bash
python manage.py runserver
```

---

## 📡 API Endpoints Summary

| Feature      | Endpoint                  | Method | Auth         |
|--------------|---------------------------|--------|--------------|
| Login        | `/api/auth/login/`        | POST   | Public       |
| Register     | `/api/auth/register/`     | POST   | Public       |
| Course List  | `/api/courses/`           | GET    | Public (Cached) |
| Enroll       | `/api/enroll/`            | POST   | JWT Required |
| My Progress  | `/api/my-courses/`        | GET    | JWT Required |
| Analytics    | `/api/admin/analytics/`   | GET    | Admin Only   |

---

## ✅ Evaluation Compliance Checklist

- [x] **PostgreSQL:** Used for all relational data storage.
- [x] **Redis:** Implemented for public API caching and high-speed reads.
- [x] **JWT:** Stateless authentication implemented for all protected routes.
- [x] **No React:** Frontend built entirely with HTML/JS.
- [x] **Structure:** Organized into 5 distinct Django applications as per blueprint.

---

**Developed by:** Muhammed Hafan  
**Project Status:** Capstone Ready
