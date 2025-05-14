import mysql.connector

# ✅ Database connection function
def get_connection():
    return mysql.connector.connect(
        host="localhost",       # 👉 তোমার MySQL সার্ভার হোস্ট
        user="root",            # 👉 ইউজারনেম
        password="",            # 👉 পাসওয়ার্ড (ফাঁকা থাকলে ফাঁকা রাখো)
        database="school"       # 👉 তোমার তৈরি ডেটাবেইস
    )

# ✅ Create
def add_student():
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)", (name, grade))
    conn.commit()
    print("✅ Student added successfully.")
    cursor.close()
    conn.close()

# ✅ Read
def show_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        print("\n📋 Student List:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}")
    else:
        print("❌ No students found.")
    cursor.close()
    conn.close()

# ✅ Update
def update_student():
    student_id = input("Enter student ID to update: ")
    new_grade = input("Enter new grade: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = %s WHERE id = %s", (new_grade, student_id))
    conn.commit()
    print("✅ Student updated successfully.")
    cursor.close()
    conn.close()

# ✅ Delete
def delete_student():
    student_id = input("Enter student ID to delete: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    print("🗑️ Student deleted successfully.")
    cursor.close()
    conn.close()

# ✅ Menu
def menu():
    while True:
        print("\n📘 Student Management System (MySQL)")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            show_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

# ✅ Run
if __name__ == "__main__":
    menu()
