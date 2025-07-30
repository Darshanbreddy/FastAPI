from passlib.context import CryptContext

pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")     #default algo for password encryption


def has(passw: str):
    return pwd_context.hash(passw)