import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=05.getenv("DB_USER"),
            password=05.getenv("DB_PASSWORD"),
            database=05.getenv("DB_NAME")
        )