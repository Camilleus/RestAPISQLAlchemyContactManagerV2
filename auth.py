from datetime import datetime, timedelta
from jose import JWTError, jwt
from models import Token, TokenData, User


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def authenticate_user(username: str, password: str):
    if username == "test" and password == "testpassword":
        return User(username="test", email="test@example.com", hashed_password="testpassword")
    return None


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
