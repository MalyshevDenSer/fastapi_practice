import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD_SALT = os.getenv('PASSWORD_SALT')