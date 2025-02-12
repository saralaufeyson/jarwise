from flask import Flask
from flask_login import LoginManager
from config import Config
from app.auth import User
from app.user_store import users  # Import users

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)

    from app.routes import main
    from app.auth import auth
    
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():  # users is now accessible
        if user["id"] == user_id:
            return User(user["id"], user["username"], user["email"])
    return None
