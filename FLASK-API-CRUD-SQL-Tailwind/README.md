# 📝 Task Inventory – Flask CRUD Application

Task Inventory adalah aplikasi web sederhana berbasis **Flask + MySQL** yang digunakan untuk mengelola daftar tugas (task).  
Aplikasi ini mendukung fitur **CRUD (Create, Read, Update, Delete)**, filter berdasarkan kategori, serta tampilan modern menggunakan **Tailwind CSS**.

Project ini dibuat sebagai latihan backend web development dan pengelolaan database menggunakan Python.

---

## 🚀 Fitur Utama

- 📋 Menampilkan semua task
- ➕ Menambahkan task baru
- ✏️ Mengedit task yang sudah ada
- 🗑️ Menghapus task (AJAX / Fetch API)
- 🔍 Filter task berdasarkan kategori:
  - Important
  - Urgent
  - Reguler
- 🎨 UI modern dengan Tailwind CSS

---

## 🛠️ Teknologi yang Digunakan

- **Backend**
  - Python 3
  - Flask
  - PyMySQL
- **Database**
  - MySQL / MariaDB
- **Frontend**
  - HTML5
  - Tailwind CSS
  - JavaScript (Fetch API)

---

## 📂 Struktur Project
├── app.py
├── templates/
│ ├── index.html
│ ├── add_task.html
│ └── update_task.html
├── README.md




## ⚙️ Cara Menjalankan Project

--Clone Repository
bash
git clone https://github.com/username/task-inventory-flask.git
cd task-inventory-flask

--Install Dependency
pip install flask pymysql

--Pastikan MySQL Aktif
Username: root
Password: kosong ("")
Database akan dibuat otomatis

--Jalankan Aplikasi
python app.py

--- Akses di browser:
http://127.0.0.1:5000