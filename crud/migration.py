import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Read from .env
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def run_migration():
    try:
        # Step 1: Connect to MySQL (without selecting DB first)
        conn = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD
        )
        cursor = conn.cursor()

        # Step 2: Create database if not exists
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' created or already exists.")

        # Step 3: Select the Database
        conn.database = DB_NAME

        # Step 4: Create Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                grade VARCHAR(10) NOT NULL
            )
        """)
        print("Table 'students' created or already exists")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("Error:", err)

# Run Migration
if __name__ == "__main__":
    run_migration()
