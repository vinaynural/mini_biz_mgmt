# Mini Business Management System

A simple business management system developed with Django to manage customers, products, and orders efficiently.

**Live URL:** [https://mini-biz-mgmt.onrender.com](https://mini-biz-mgmt.onrender.com)  
**GitHub Repository:** [https://github.com/vinaynural/mini_biz_mgmt](https://github.com/vinaynural/mini_biz_mgmt)

---

## 🔑 Admin Login Credentials (Live Site)

Use these credentials to access the deployed system:

- **Username:** `vinay`
- **Password:** `Vinay@123`

---

## 🚀 Features Implemented

### Module 1: Authentication

- **System:** Django’s built-in authentication system.
- **Functionality:** Secure Login and Logout.
- **Access Control:** Only logged-in users can access the system.

### Module 2: Customer Management

- **Fields:** Name, Phone Number, Email, Created Date.
- **Features:**
  - Add new customer.
  - View customer list.
  - Edit customer details.
  - Delete customer.

### Module 3: Product Management

- **Fields:** Product Name, Price, Stock Quantity.
- **Features:**
  - Add new product.
  - Edit product details.
  - Delete product.
  - View product list.

### Module 4: Order Management

- **Order Fields:** Customer, Order Date, Total Amount (auto-calculated).
- **Order Items:** Product, Quantity, Price, Subtotal (Quantity × Price).
- **Key Logic:**
  - One order can contain multiple products.
  - Total amount calculated automatically.
  - **Stock Reduction:** Product stock automatically reduces after order creation.

### Module 5: Dashboard

Displays a simple overview of business metrics:

- Total number of customers.
- Total number of products.
- Total number of orders.
- Total revenue.

---

## ✨ Bonus Enhancements (Optional)

- **Advanced Reporting:** Monthly Sales Bar Chart & Top Selling Products Pie Chart (Chart.js).
- **PDF Invoices:** Download order details as PDF files.
- **Search & Pagination:** Efficiently manage long lists of customers/products.
- **UI/UX:** Dark Mode toggle, Bootstrap 5 styling.

---

## 🛠 Technology Stack

- **Backend:** Python, Django
- **Frontend:** Django Templates, HTML, CSS, Bootstrap 5
- **Database:**
  - **Development:** SQLite
  - **Production:** PostgreSQL (Hosted on Render)
- **Version Control:** Git & GitHub

---

## ⚙️ Project Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/vinaynural/mini_biz_mgmt.git
cd mini_biz_mgmt
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.
