# Mini Business Management System

A simple business management system built with Django.

## Features

- **Authentication**: User login/logout.
- **Customers**: Manage customer details.
- **Products**: Manage inventory.
- **Orders**: Create orders and track sales.
- **Dashboard**: Real-time business overview.

## Tech Stack

- Python, Django
- SQLite
- Bootstrap 5

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repo_url>
   cd mini_biz_mgmt
   ```

2. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install django
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```

## Admin Credentials

_(To be created by user)_

- Username: `admin`
- Password: `admin` (example)
