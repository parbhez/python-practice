from db_config import connect_to_db

# Specific student info Update
def update_student():
    try:
        student_id = input("Enter Student id: ").strip()

        if not student_id:
            raise ValueError("Student ID cannot be empty")

        student_id = int(student_id)

        if student_id < 0:
            raise ValueError("Student ID cannot be a negative number")

        print(f"✅ Valid Student ID: {student_id}")

    except Exception as e:
        print(f"❌ Error (validation): {e}")
        return

    # Take update info
    name = input("Enter new name (leave blank to skip): ").strip()
    grade = input("Enter new grade (leave blank to skip): ").strip()
    roll = input("Enter new roll (leave blank to skip): ").strip()

    if not (name or grade or roll):
        print("⚠️ Nothing to update.")
        return

    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        update_fields = []
        update_values = []

        if name:
            update_fields.append("name = %s")
            update_values.append(name)

        if grade:
            update_fields.append("grade = %s")
            update_values.append(grade)

        if roll:
            try:
                roll = int(roll)
                update_fields.append("roll = %s")
                update_values.append(roll)
            except ValueError:
                raise ValueError("Roll must be an integer")

        update_values.append(student_id)

        sql = f"UPDATE students SET {', '.join(update_fields)} WHERE id = %s"
        cursor.execute(sql, update_values)
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Student updated successfully.")
        else:
            print("❌ No student found with that ID.")

    except Exception as e:
        print(f"❌ Error (update): {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    update_student()
