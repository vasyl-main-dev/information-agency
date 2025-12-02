# 📡 Information Agency — Django Web Application

**Information Agency** is a modern and stylish Django-powered news platform designed for managing editors, topics, and newspapers.  
The project demonstrates clean architecture, user authentication, CRUD functionality, responsive UI, and a fully customized design.

---

## 🚀 Features

### 🧑‍💻 Redactors (Editors)
- View a list of all redactors  
- Search redactors by username  
- View detailed information (profile, experience, publications)  
- Add new redactors  
- Delete own account securely  

### 📰 Newspapers
- Create, view, search, and delete newspapers  
- Link newspapers to multiple redactors  
- Assign topics  
- Display latest publications on the homepage  

### 📚 Topics
- Assign multiple topics to newspapers  
- Display topic badges for quick categorization  

### 🔐 Authentication
- Secure login and logout  
- POST-based logout for enhanced safety  
- Account-specific delete permissions  

---

## 🎨 UI & Design

The project uses:

- **Bootstrap 5**
- Fully custom **CSS theme**
- Unified button styles  
- Modern gradients & shadows  
- Smooth animations  
- Responsive layout  
- Clean card-based content blocks  
- Dark elegant palette  

---

## 🏗️ Technologies Used

- **Python 3**
- **Django**
- **Bootstrap 5**
- **Crispy Forms**
- **DiceBear Avatars API**
- **SQLite3 (default)**

---

## 🛡️ Security Notes

- SECRET_KEY should be stored in a `.env` file  
- `.env` must be excluded in `.gitignore`  
- Logout is implemented as a POST request  
- Only the account owner can delete their profile  

---

## 🚀 Deployed project

https://information-agency.onrender.com

## 🧪 How to Run Locally

```bash
git clone https://github.com/vasyl-main-dev/information-agency.git
cd information-agency

python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🌟 Summary

Information Agency is a clean, polished Django application that demonstrates strong backend logic combined with modern UI/UX.  
It’s a great example of a structured, production-ready web project with authentication, relationships, custom design, and CRUD functionality.
