# Hackathon_tranierapp
Hackathon Trainer App
Overview
The Hackathon Trainer App is a web application designed to enhance the hackathon experience for participants and organizers. It provides a platform to manage hackathons, form teams, submit projects, and access training resources to prepare for coding challenges and competitions.
Features

User Management: Register and manage user accounts with secure authentication.
Hackathon Management: Create, view, and join hackathons with detailed event information.
Team Collaboration: Form and manage teams for collaborative project development.
Project Submission: Submit hackathon projects and deliverables through the platform.
Training Resources: Access tutorials, coding challenges, and resources to improve hackathon skills.

Tech Stack

Backend: Python 3.x
Framework: Django
Database: MySQL
Frontend: HTML, CSS, JavaScript (Django templates)
Dependencies: Listed in requirements.txt (e.g., django, mysqlclient)

Installation
Prerequisites

Python 3.8 or higher
MySQL Server
pip (Python package manager)
Git

Steps

Clone the Repository:
git clone https://github.com/Siddhesh204/Hackathon_tranierapp.git
cd Hackathon_tranierapp


Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

Ensure mysqlclient is included in requirements.txt for MySQL support. If not, install it:
pip install mysqlclient


Set Up MySQL Database:

Create a MySQL database:CREATE DATABASE hackathon_trainer;


Update the DATABASES setting in settings.py (located in your Django project directory, e.g., hackathon_trainer/settings.py):DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hackathon_trainer',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}




Apply Migrations:Run Django migrations to create the database tables:
python manage.py makemigrations
python manage.py migrate


Create a Superuser (optional, for admin access):
python manage.py createsuperuser


Run the Development Server:
python manage.py runserver


Access the App:Open your browser and navigate to http://localhost:8000. For admin access, go to http://localhost:8000/admin.


Database Migration (SQLite3 to MySQL)
If migrating an existing SQLite3 database to MySQL:

Export the SQLite3 schema and data:sqlite3 database.db .dump > dump.sql


Modify dump.sql to ensure MySQL compatibility (e.g., adjust data types, remove SQLite-specific syntax like AUTOINCREMENT).
Import the schema and data into MySQL:mysql -u your_mysql_username -p hackathon_trainer < dump.sql


Update Django’s settings.py to use MySQL (as shown above).
Run migrations to ensure the schema aligns with Django models:python manage.py migrate



Usage

Register/Login: Create an account or log in to access the platform.
Manage Hackathons: Browse, join, or create hackathons.
Form Teams: Collaborate with others by creating or joining teams.
Submit Projects: Upload project submissions for hackathons.
Train: Use integrated resources to prepare for hackathons.

Project Structure
Hackathon_tranierapp/
├── hackathon_trainer/    # Django project directory
│   ├── settings.py       # Configuration (update DATABASES for MySQL)
│   ├── urls.py           # URL routing
│   └── ...
├── app/                  # Django app directory (example)
│   ├── migrations/       # Database migrations
│   ├── models.py         # Database models (defines tables)
│   ├── views.py          # Application logic
│   ├── templates/        # HTML templates
│   └── ...
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # This file

Number of Tables
The number of tables in MySQL will match the number of models defined in your Django models.py files (one model per table, plus Django’s built-in tables for authentication, sessions, etc.). To confirm the exact number:

Check all models.py files in your Django apps.
Count the model classes (e.g., User, Hackathon, Team, Submission).
Add Django’s default tables (e.g., auth_user, django_session), typically 6–10 additional tables, depending on your configuration.

Run python manage.py migrate to create these tables in MySQL.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name.
Make changes and commit: git commit -m "Add your feature".
Push to your branch: git push origin feature/your-feature-name.
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or support, contact any collaborator or open an issue on GitHub.
