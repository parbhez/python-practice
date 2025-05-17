from db_config import connect_to_db

#Add Student
def add_student():
    name = input("Enter your name: ")
    if not name:
        raise ValueError("Name cannot be empty")

    grade = input("Enter your grade: ").strip()
    if not grade:
        raise ValueError("Grade cannot be empty")

    roll = input("Enter your roll : ")
    if not roll:
        raise ValueError("Roll can not be empty")

    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT into students (name, graade, roll) values(%s, %s, %s)", (name, grade, roll))
        conn.commit()
        print("Student inserted successfully")
    except Exception as ex:
        print("Exception Error : ", ex)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    add_student()