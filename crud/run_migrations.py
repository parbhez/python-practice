import os
import importlib.util
from db_config import connect_to_db  # Make sure this file has the connect_to_db function

def run_migrations():
    migrations_dir = os.path.join("database", "migrations")
    if not os.path.exists(migrations_dir):
        print("⚠️  Migrations folder not found.")
        return

    migration_files = sorted(f for f in os.listdir(migrations_dir) if f.endswith(".py"))

    for file in migration_files:
        path = os.path.join(migrations_dir, file)
        module_name = file[:-3]
        print(module_name)
        return

        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "migrate"):
            print(f"🔁 Running migration: {file}")
            conn = connect_to_db()
            module.migrate(conn)
        else:
            print(f"⚠️  Skipped {file} (no migrate function)")

if __name__ == "__main__":
    run_migrations()
