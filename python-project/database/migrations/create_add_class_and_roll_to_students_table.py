def migrate(conn):
    try:
        cursor = conn.cursor()

        # Check if 'class' column already exists
        cursor.execute("""
            SHOW COLUMNS FROM students LIKE 'class'
        """)
        result = cursor.fetchone()
        if not result:
            cursor.execute("ALTER TABLE students ADD COLUMN class VARCHAR(50)")
            print("✅ Column 'class' added.")

        # Check if 'roll' column already exists
        cursor.execute("""
            SHOW COLUMNS FROM students LIKE 'roll'
        """)
        result = cursor.fetchone()
        if not result:
            cursor.execute("ALTER TABLE students ADD COLUMN roll INT")
            print("✅ Column 'roll' added.")

        conn.commit()
        cursor.close()

    except Exception as e:
        print("❌ Error altering table:", e)
