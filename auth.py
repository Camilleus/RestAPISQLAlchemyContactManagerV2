from models import Token, TokenData, User


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def authenticate_user(username: str, password: str):
    if username == "test" and password == "testpassword":
        return User(username="test", email="test@example.com", hashed_password="testpassword")
    return None



