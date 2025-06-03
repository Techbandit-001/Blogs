# 📝 Blog Platform

A full-stack blog application that allows users to create, edit, and browse blog posts with rich content formatting, categories, and image support.

---

## Features

- Create, edit, and delete blog posts
- Categorize posts (e.g., Tech, Faith, Lifestyle, Other)
- filter posts by title or category
- Optional image support via URL
- Markdown or rich text formatting
- Fast and responsive UI built with React
- RESTful backend built with FastAPI 

---

## 🛠️ Tech Stack

**Frontend**  
- React (with Hooks & Context)
- React Router
- Tailwind CSS
- React Hook Form + Zod (form validation)
- Toast Notifications (react-hot-toast)

**Backend**  
- FastAPI
- SQLite 
- CORS enabled for frontend connection

---

## 📸 Screenshots

> Add screenshots/gifs here showing the homepage, post creation, filtering, and editing.
![image](https://github.com/user-attachments/assets/468c979d-a8d0-46e3-9621-dcbba1249f14)
![image](https://github.com/user-attachments/assets/3c4899fd-12bb-4c26-a45c-d96d2eeabedb)
![image](https://github.com/user-attachments/assets/00e7285a-a593-42b8-804a-ee080a6d220e)

---


pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
