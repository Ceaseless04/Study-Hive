from fastapi import FastAPI, HTTPException, status, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

from backend.db.queries import get_db_connection

app = FastAPI()

# Password hashing context (use for hashing and verifying passwords)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Function to authenticate user
def authenticate_user(username: str, password: str):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()

            # If user exists and password is correct
            if user and verify_password(password, user["password"]):
                return user
            return None
    finally:
        connection.close()



