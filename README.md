# User Auth API

Flask-based REST API for user authentication using JWT tokens and password hashing.

## Features
- User signup with hashed passwords
- User login with JWT token generation
- Protected route example (accessible only with valid token)

## Tech Stack
- Python
- Flask
- SQLite
- PyJWT
- Werkzeug (password hashing)

## Routes
| Method | Route     | Description                     | Protected |
|--------|-----------|---------------------------------|-----------|
| POST   | /signup   | Register a new user             | No        |
| POST   | /login    | Login and get JWT token         | No        |
| GET    | /profile  | Get logged-in user's profile    | Yes       |
| GET    | /users    | Get list of all users (testing) | No        |

## Example Requests

**Signup**
```json
POST /signup
{
  "username": "ali123",
  "email": "ali@example.com",
  "password": "test1234"
}
```

**Login**
```json
POST /login
{
  "username": "ali123",
  "password": "test1234"
}
```
Response: `{"token": "..."}`

**Profile** (Protected)

## How to Run

1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies
4. Create a `config.py` file with:
SECRET_KEY = "your-secret-key"
5. Run the app
## Author
[M.Zulqarnain]