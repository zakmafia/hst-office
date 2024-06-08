# 🏢 **HST SmartOffice Web App**

Welcome to the HST SmartOffice Web App! This system is designed for HST to manage office room booking, IT help desk management, and IT asset management.

---

## 🌟 **Features**

Our application provides a comprehensive suite of features:

- **Office Room Booking Management:** Efficiently manage your office space by booking rooms in advance.
- **IT Help Desk Ticketing System:** Keep track of IT issues and ensure they're addressed in a timely manner.
- **IT Asset Management:** Maintain an inventory of your IT assets and manage their lifecycle.

---

## 💻 **Technologies Used**

We've built our application using some of the latest technologies:

- **Django:** A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Celery:** An asynchronous task queue/job queue based on distributed message passing.
- **Celery Beat:** A Celery's periodic task scheduler.

---

## 🔧 **Installation**

Follow these steps to get the app up and running:

1. **Clone the repository:**
bash
git clone https://github.com/zakmafia/hst-office.git
cd hst-office

2. Create a virtual environment and activate it (optional but recommended):
python3 -m venv env
source env/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Set up environment variables: Create a .env file in the root directory of the project. Add necessary environment variables such as database settings, secret key, etc. Refer to .env.example for required variables.
   
5. Apply database migrations:
python manage.py migrate

5. Start the Celery worker:
celery -A hst_office worker --beat --scheduler django --loglevel=info

5. Start the Django development server:
python manage.py runserver

5. Access the web app at http://localhost:8000 in your browser.

🖥️ Usage
Navigate to the web app in your browser. Sign up or log in to access the functionalities. Explore the various features such as room booking, IT help desk, and asset management. Enjoy a more organized office environment!

🤝 Contributing
We welcome contributions from the community! Please fork the repository and submit a pull request with your changes.

📄 License
This project is licensed under the MIT License. Enjoy using the HST SmartOffice Web App! 🎉
