from app.configs.database import get_db
from bcrypt import hashpw, checkpw, gensalt
from environs import Env
from datetime import datetime, timedelta
from utils.exception import UserInvalid
import jwt

db = get_db()
env = Env()
SECRET_KEY = env("JWT_SECRET") or "mysecret"


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created_at = datetime.now()

    def create(self):
        salt = gensalt()
        hashed_pass = hashpw(password=self.password, salt=salt)
        user = self.__dict__
        user["password"] = hashed_pass

        result = db.user.insert_one(user)

        user['_id'] = result.inserted_id

        return user

    @staticmethod
    def login(username, password):
        user = db.user.find_one({"username": username})

        if user is None:
            raise UserInvalid("Invalid username or password")

        check_pass = checkpw(password, user[password])

        if not check_pass:
            raise UserInvalid("Invalid username or password")
        
        payload = {
                'exp': datetime.utcnow() + timedelta(days=5),
                'iat': datetime.utcnow(),
                'sub': str(user['_id'])
            }
        
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return token
        
        
