## Full-Stack Flask Web App

This project is a dynamic web application I built using Python and Flask. It includes a full front-end/back-end integration with database support, security features, and REST API functionality—all designed to create a solid foundation for personal or professional web apps.

### 🧩 Key Features
- Dynamic content rendering with **Flask** and **Jinja2 templates**
- Data storage and retrieval using **Flask-MongoEngine** (MongoDB)
- User registration, login, and authentication using **Flask-Security**
- **REST API** endpoints for interacting with the app’s data programmatically
- API testing with **Postman**
- Web forms for creating and updating data

### 🧠 What I Learned
- How to set up a full Flask project from scratch and run it locally
- How to design HTML templates and connect them to Python data
- How to configure and connect a MongoDB database to Flask using MongoEngine
- How to securely manage user accounts and roles with Flask-Security
- How to expose API endpoints and test them effectively using Postman
- How to build a complete application architecture using modular design principles

### 🛠️ Running Locally
With your virtual environment activated, run the following commands in the terminal:

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_DEBUG = 1
flask run
