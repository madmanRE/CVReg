from dotenv import load_dotenv
import os

load_dotenv()

SALT = int(os.environ.get("SALT"))
