def migrate(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
           CREATE TABLE IF NOT EXISTS transcriber (
               id INT AUTO_INCREMENT PRIMARY KEY,
               title TEXT NOT NULL,
               url TEXT NOT NULL,
               keywords LONGTEXT,
               language VARCHAR(10) NOT NULL DEFAULT 'bn-BD',
               transcription_id TEXT,
               transcription LONGTEXT,
               summary LONGTEXT,
               status VARCHAR(20) DEFAULT 'created',
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
               updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        """)
        print("✅ Table 'transcriber' created or already exists.")
        cursor.close()
    except Exception as e:
        print("❌ Error creating table:", e)
