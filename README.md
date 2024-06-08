<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HST SmartOffice Web App 🏢</title>
</head>
<body>

<h1>HST SmartOffice Web App 🏢</h1>

<p>This system is designed to for HST manage office room booking, IT help desk management, and IT asset management.</p>

<h2>Features 🌟</h2>
<ul>
    <li>Office room booking management</li>
    <li>IT help desk ticketing system</li>
    <li>IT asset management</li>
</ul>

<h2>Technologies Used 💻</h2>
<ul>
    <li>Django</li>
    <li>Celery</li>
    <li>Celery Beat</li>
</ul>

<h2>Installation 🔧</h2>
<ol>
    <li>Clone the repository:
        <code>git clone https://github.com/zakmafia/hst-office.git</code><br>
        <code>cd hst-office</code></li>

    <li>Create a virtual environment and activate it (optional but recommended):<br>
        <code>python3 -m venv env</code><br>
        <code>source env/bin/activate</code></li>

    <li>Install dependencies:<br>
        <code>pip install -r requirements.txt</code></li>

    <li>Set up environment variables: Create a .env file in the root directory of the project. Add necessary environment variables such as database settings, secret key, etc. Refer to .env.example for required variables.</li>

    <li>Apply database migrations:<br>
        <code>python manage.py migrate</code></li>

    <li>Start the Celery worker:<br>
        <code>celery -A hst_office worker --beat --scheduler django --loglevel=info</code></li>

    <li>Start the Django development server:<br>
        <code>python manage.py runserver</code></li>
</ol>

<p>Access the web app at <a href="http://localhost:8000">http://localhost:8000</a> in your browser.</p>

<h2>Usage 🖥️</h2>
<p>Navigate to the web app in your browser. Sign up or log in to access the functionalities. Explore the various features such as room booking, IT help desk, and asset management. Enjoy a more organized office environment!</p>

<h2>Contributing 🤝</h2>
<p>Contributions are welcome! Please fork the repository and submit a pull request.</p>

<h2>License 📄</h2>
<p>This project is licensed under the MIT License. Enjoy using the HST SmartOffice Web App! 🎉</p>

</body>
</html>
