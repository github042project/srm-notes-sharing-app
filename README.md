📚 SRM Notes Sharing Website (Django)

A community-driven web application that allows SRM students to upload, organize, and download semester-wise study notes.
Built with Django, this project helps students easily share academic resources.

🚀 Features

📤 Upload PDF notes

📥 Download notes shared by others

🔎 Search notes by semester or subject

🗂️ Categorized by semester & subject

📁 Automatic file storage in /media/notes/

🎨 Simple, clean, user-friendly UI

🛠️ Tech Stack

Backend: Django
Frontend: HTML, CSS
Database: SQLite (default)
Storage: Django Media Files
Language: Python
Version Control: Git & GitHub

📁 Project Structure
```bash
notesapp/
│── manage.py
│── requirements.txt
│── Procfile
│── README.md
│
├── notes/                # App folder
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │     ├── upload.html
│   │     └── notes_list.html
│   └── static/
│
├── notesapp/             # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/                # Uploaded notes stored here
└── static/               # (optional) Custom Static Files
```

▶️ How to Run Locally
git clone <your repo link>
cd notesapp
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Open browser →

http://127.0.0.1:8000/

🤝 Collaborations

Contributions are welcome!
Ideal beginner-friendly tasks:

Improve UI

Add login/logout

Add semester dropdown

Add delete option

Add dark mode

Improve search

Add subject filters

Enhance admin panel

🎯 Purpose

This project was created as part of my community contribution, helping SRM students share study materials easily.

📜 License

This project is open-source for educational purposes.

📷 Screenshots
🖼️ Upload Notes Page
<img width="458" height="207" alt="screenshot - 2" src="https://github.com/user-attachments/assets/1a923c77-f586-4eb8-a65a-631e024bc549" />

🗂️ Notes List Page
<img width="380" height="271" alt="screenshot - 1" src="https://github.com/user-attachments/assets/21aa2f88-8f7a-4771-8ca4-e08679956bda" />

