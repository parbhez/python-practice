def migrate(conn):
    try:
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
    except Exception as e:
        print("❌ Error creating table:", e)
