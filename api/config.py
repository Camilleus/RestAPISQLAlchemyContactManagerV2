from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = "your-secret-key"  
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")