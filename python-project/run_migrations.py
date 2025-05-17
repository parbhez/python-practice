import os
import importlib.util
from db_config import connect_to_db

def ensure_migration_table_exists(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) UNIQUE,
            run_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()

def has_migration_run(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM migrations WHERE name = %s", (name,))
    result = cursor.fetchone()[0]
    cursor.close()
    return result > 0

def save_migration_record(conn, name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO migrations (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()

def run_migrations():
    migrations_dir = os.path.join("database", "migrations")
    if not os.path.exists(migrations_dir):
        print("📁 Migrations folder not found.")
        return

    migration_files = sorted(f for f in os.listdir(migrations_dir) if f.endswith(".py"))
    conn = connect_to_db()
    ensure_migration_table_exists(conn)

    for file in migration_files:
        if has_migration_run(conn, file):
            print(f"⏩ Skipped {file} (already migrated)")
            continue

        path = os.path.join(migrations_dir, file)
        module_name = file[:-3]
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "migrate"):
            print(f"🔁 Running migration: {file}")
            try:
                module.migrate(conn)
                save_migration_record(conn, file)
            except Exception as e:
                print(f"❌ Error running {file}: {e}")
        else:
            print(f"⚠️ Skipped {file} (no 'migrate' function)")
    conn.close()

if __name__ == "__main__":
    run_migrations()
