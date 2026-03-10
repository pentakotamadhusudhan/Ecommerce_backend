# Local Baba - E-commerce Backend

Welcome to **Local Baba**, a robust and feature-rich e-commerce backend built with Django and Django Rest Framework (DRF). This project is designed to power a multi-vendor marketplace, handling everything from user authentication to product management and order processing.

It features a polished admin interface using **Jazzmin**, comprehensive API documentation with **Swagger/Redoc**, and a scalable architecture ready for mobile and web clients.

## 🚀 Features

### 🖥️ Admin Dashboard (The Command Center)
*   **Custom Branding**: A completely white-labeled admin interface ("Local Baba Admin") replacing the default Django look.
*   **Visual Analytics**: Integrated charts for revenue flow and category analysis directly in the dashboard.
*   **Role Management**: Specific workflows and views for **Vendors** vs. **Customers**.
*   **Bulk Actions**: Easy management of user statuses and role assignments.
*   **Jazzmin Integration**: sleek, responsive, and customizable admin UI with FontAwesome icons.

### 📱 API & Mobile Ready
*   **RESTful API**: Fully documented APIs served via Django Rest Framework (DRF).
*   **Authentication**: Custom user model supporting mobile numbers and role-based access.
*   **Swagger/Redoc**: Interactive API documentation available at the root URL.
*   **Media Management**: Dedicated handling for product images and static assets.

## 🛠️ Tech Stack

*   **Framework**: Django 5.2.10
*   **API**: Django Rest Framework (DRF)
*   **Documentation**: drf-yasg (Swagger/Redoc)
*   **Admin UI**: Jazzmin
*   **Database**: SQLite (Development) / PostgreSQL (Production ready)
*   **CORS**: django-cors-headers

## 📦 Installation & Setup

Follow these steps to get the project running locally.

### Prerequisites
*   Python 3.8+
*   pip (Python package manager)
*   Virtualenv (recommended)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ecommerce
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv env
.\env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
Set up your database schema:
```bash
python manage.py migrate
```

### 5. Create a Superuser
Create an admin account to access the dashboard:
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

## 🔗 Accessing the Application

*   **API Documentation (Swagger)**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
*   **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
*   **Redoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## 📂 Project Structure

```text
ecommerce_backend/
├── ecommerce/          # Project settings & configuration
├── accounts/           # User authentication & management
├── store/              # Product & store logic
├── static/             # Static assets (CSS, JS, Images)
├── productImages/      # User-uploaded media
├── templates/          # HTML templates
├── manage.py           # Django command-line utility
└── requirements.txt    # Project dependencies
```

## 🤝 Contributing

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---
**Local Baba**