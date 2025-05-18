from db_config import connect_to_db

# Delete student
def delete_student():
    student_id = input("Enter student Id : ").strip()

    if not student_id:
        raise ValueError("Student ID can not be null")
    
    if not student_id.isdigit():
        raise ValueError("Student ID must be positive integer")
    
    student_id = int(student_id)
    
    if student_id <= 0:
            raise ValueError("Student ID must be greater than zero.")

    print(f"✅ Valid Student ID: {student_id}")
    
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("DELETE from students where id = %s", (student_id,))
        conn.commit()

        if cursor.rowcount == 0:
             print(f"⚠️ No student found with ID = {student_id}.")
        else:
            print(f"Student ID = {student_id} deleted successfully!")

    except Exception as e:
        print(f"Exception Error : {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    delete_student()