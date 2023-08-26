import hashlib
from config import SALT


def hash_password(password: str):
    salt = bytes([SALT])

    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return key.hex()
