# DJANGO_REST_API_PROJECT

Project Title: Django REST API – User Authentication (Login System)

Description:
This project demonstrates a simple RESTful API built using Django and the Django REST Framework (DRF) for user authentication. It implements a secure login endpoint (POST /api/login/) that accepts a username and password, validates the credentials, and returns an authentication token (JWT or DRF Auth Token). This token can then be used to access protected API routes.

The project showcases how to:

Configure Django REST Framework for API development.

Implement token-based authentication using JWT or DRF tokens.

Handle user login requests securely through a REST API.

Test authentication using a sample username and password.

Example Test Credentials:

Username: testuser  
Password: testpassword


API Endpoint:

POST /api/login/


Request Body (JSON):

{
  "username": "testuser",
  "password": "testpassword"
}


Response (Example):

{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}


Technologies Used:

Django

Django REST Framework

JWT Authentication (or DRF Token Authentication)

Python
