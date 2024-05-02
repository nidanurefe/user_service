# Flask User Management API

This Flask-based API manages user data including registration, authentication, and deletion. It uses JWT tokens for authentication and a MySQL database for storing user information.

## Prerequisites
- Python 3
- Flask
- Peewee
- MySQL database

## Installation

1. Clone this repository to your local machine:
2. Install the required Python packages:
3. Configure the MySQL database settings in `helpers.models.py`:
4. Run the Flask application: ```python app.py ```

## API Endpoits 
- POST /api/user: Create a new user.
- GET /api/user: Get user information.
- DELETE /api/user: Delete a user.
- PUT /api/user/authupdate: Updates user authentication.

## Usage
- Use a tool like Postman or cURL to send requests to the API endpoints.
- Register a new user using a POST request to /api/user.
- Authenticate users using a POST request to /api/user with appropriate credentials.
- Delete users using a DELETE request to /api/user.
- Update user authentication code using a PUT request to /api/user/authupdate.

## Database Setup
Make sure to create a MySQL database with the required schema and configure the database connection details in helpers.models.py.

## Security
User passwords are hashed before storing in the database.
JWT tokens are used for authentication and authorization.
