# Flask User Registration Application

This guide will walk you through setting up a Flask application for user registration, including creating a virtual environment, installing Flask and bcrypt, running the application, and testing it using Postman.

## Getting Started

### 1. Create a Virtual Environment

#### Create a virtual environment named 'env'
python -m venv env

# Activate the virtual environment
#### On Windows
.\env\Scripts\activate
#### On macOS/Linux
source env/bin/activate

### 2.Install Flask and Bcrypt

#### Install Flask
pip install Flask

#### Install bcrypt
pip install bcrypt


### 3.Running the Flask application
#### Run the Flask application
python app.py

### 4.Testing with Postman-API

#### To register a new user, send a POST request to /register with the following JSON payload:
     {
    "username": "ranatarachan",
    "email": "ranatarachan@gmail.com",
    "password": "password123"
     }
