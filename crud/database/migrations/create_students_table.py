from db_config import connect_to_db

def create_students_table():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                grade VARCHAR(10) NOT NULL
            )
        """)
        print("✅ Table 'students' created or already exists.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error creating table:", e)

if __name__ == "__main__":
    create_students_table()
