from datetime import datetime, timedelta
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Security,HTTPException,status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def generate_jwt_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(hours=1)
    to_encode.update({"exp": expire.timestamp()})
    encode_jwt=jwt.encode(to_encode,"1234",algorithm="HS256")
    return encode_jwt

def decode_jwt_token(token:str):
    try:
        payload = jwt.decode(token,"1234",algorithms=["HS256"])
        if payload.get("exp") and payload["exp"] >= datetime.now().timestamp():
            return payload
    except JWTError:
        return None
    
def get_current_user(token:str=Security(oauth2_scheme))->dict:
    payload = decode_jwt_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload