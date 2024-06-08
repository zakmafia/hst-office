HST SmartOffice Web App 🏢
This system is designed to for HST manage office room booking, IT help desk management, and IT asset management.

Features 🌟
Office room booking management
IT help desk ticketing system
IT asset management
Technologies Used 💻
Django
Celery
Celery Beat
Installation 🔧
Clone the repository:
git clone https://github.com/zakmafia/hst-office.git
cd hst-office

Create a virtual environment and activate it (optional but recommended):
python3 -m venv env
source env/bin/activate

Install dependencies:
pip install -r requirements.txt

Set up environment variables: Create a .env file in the root directory of the project. Add necessary environment variables such as database settings, secret key, etc. Refer to .env.example for required variables.
Apply database migrations:
python manage.py migrate

Start the Celery worker:
celery -A hst_office worker --beat --scheduler django --loglevel=info

Start the Django development server:
python manage.py runserver

Access the web app at http://localhost:8000 in your browser.

Usage 🖥️
Navigate to the web app in your browser. Sign up or log in to access the functionalities. Explore the various features such as room booking, IT help desk, and asset management. Enjoy a more organized office environment!

Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

License 📄
This project is licensed under the MIT License. Enjoy using the HST SmartOffice Web App! 🎉
