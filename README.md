
# Utamu Christian Fellowship Website(In development)

A simple and elegant Christian Fellowship Website built with Django. This platform provides information about the fellowship, showcases moments in the gallery, and allows visitors to contact the team.

Features

✅ Responsive and clean UI
✅ Home, About, Gallery, and Contact pages
✅ Contact form with CSRF protection
✅ Easy navigation with a consistent layout
✅ Built with Django and styled using CSS

Tech Stack

	•	Backend: Django (Python)
	•	Frontend: HTML, CSS
	•	Database: SQLite3 (default Django DB)
	•	Version Control: Git & GitHub

Screenshots

🌟 Home Page

📖 About Page

🖼️ Gallery Page

✉️ Contact Page

Setup Instructions

1️⃣ Clone the repository:

git clone https://github.com/yourusername/christian-fellowship-website.git
cd christian-fellowship-website

2️⃣ Create a virtual environment and activate it:

python -m venv env
# On Windows
env\Scripts\activate
# On Mac/Linux
source env/bin/activate

3️⃣ Install dependencies:

pip install -r requirements.txt

4️⃣ Run database migrations:

python manage.py migrate

5️⃣ Start the development server:

python manage.py runserver

Now, visit http://127.0.0.1:8000/ in your browser! 🎉

Folder Structure

christian-fellowship-website/
│── static/                  # Static files (CSS, images)
│── templates/               # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── gallery.html
│   ├── contact.html
│── fellowship/              # Django app folder
│── manage.py                # Django project manager
│── db.sqlite3                # SQLite database (default)
│── README.md                # Project documentation
│── requirements.txt         # Project dependencies

Contributing

We welcome contributions! To contribute:
	1.	Fork the repository
	2.	Create a feature branch (git checkout -b feature-name)
	3.	Commit your changes (git commit -m "Added feature")
	4.	Push to the branch (git push origin feature-name)
	5.	Open a pull request

License

📜 This project is open-source and available under the MIT License.

Contact

📧 Email: yourname@example.com
🌐 GitHub: @yourusername

Let me know if you want any customizations! 🚀
