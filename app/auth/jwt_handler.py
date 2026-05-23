from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def create_token(usrename: str):
    payload = {
        "sub": usrename,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token