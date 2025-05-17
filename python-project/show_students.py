from db_config import connect_to_db

# SHow all Students list
def show_students():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * from students")
    rows = cursor.fetchall()

    if rows:
        print("Student List: ")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}, Roll: {row[3]}")
    else:
        print("No Student found")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    show_students()