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
| Method | Route      | Description                     |
|--------|-----------|----------------------------------|
| POST   | /signup   | Register a new user             |
| POST   | /login    | Login and get JWT token         |
| GET    | /profile  | Get logged-in user's profile (protected) |

## How to Run

1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies
4. Run the app
## Author
[M.Zulqarnain]