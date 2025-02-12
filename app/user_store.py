from werkzeug.security import generate_password_hash

users = {
    "admin": {"id": "1", "username": "admin", "email": "admin@example.com", "password_hash": generate_password_hash("password")},
    "user": {"id": "2", "username": "user", "email": "user@example.com", "password_hash": generate_password_hash("12345")},
}
