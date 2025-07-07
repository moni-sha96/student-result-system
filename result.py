import sqlite3

# Connect to database (or create if not exists)
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept TEXT NOT NULL,
    mark1 INTEGER,
    mark2 INTEGER,
    mark3 INTEGER
)
''')

conn.commit()
conn.close()

print("Student table created successfully!")
def add_student():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    mark1 = int(input("Enter Mark 1: "))
    mark2 = int(input("Enter Mark 2: "))
    mark3 = int(input("Enter Mark 3: "))

    cursor.execute('''
        INSERT INTO students (roll_no, name, dept, mark1, mark2, mark3)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (roll_no, name, dept, mark1, mark2, mark3))
    print("✅ Student added successfully!\n")   
    conn.commit()
    conn.close()
def view_all_students():
     conn = sqlite3.connect('student.db')
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM students")
     rows = cursor.fetchall()
     if len(rows) == 0:
        print("❌ No student records found.")
     else:
        print("\n📄 All Student Records:\n")
        for row in rows:
            print(f"Roll No: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Department: {row[2]}")
            print(f"Marks: {row[3]}, {row[4]}, {row[5]}")
            print(f"Total: {row[3] + row[4] + row[5]}")
            print("-" * 30)
     conn.close()
def search_by_roll():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    roll_no = int(input("🔎 Enter Roll Number to search: "))  # ✅ FIXED here
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
    row = cursor.fetchone()
    conn.close()

    if row:
        print("\n✅ Student Found:\n")
        print(f"Roll No   : {row[0]}")
        print(f"Name      : {row[1]}")
        print(f"Department: {row[2]}")
        print(f"Marks     : {row[3]}, {row[4]}, {row[5]}")
        total = row[3] + row[4] + row[5]
        average = float(total / 3)
        print(f"Total     : {total}")
        print(f"Average   : {average:.2f}")

        if average >= 90:
            grade = "O"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "F"

        print(f"Grade     : {grade}")
def update_marks():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    roll_no = int(input("✏️ Enter Roll Number to update: "))
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
    row = cursor.fetchone()

    if row:
        print(f"\n✅ Current Marks: {row[3]}, {row[4]}, {row[5]}")
        mark1 = int(input("Enter new Mark 1: "))
        mark2 = int(input("Enter new Mark 2: "))
        mark3 = int(input("Enter new Mark 3: "))

        cursor.execute("""
            UPDATE students
            SET mark1 = ?, mark2 = ?, mark3 = ?
            WHERE roll_no = ?
        """, (mark1, mark2, mark3, roll_no))

        conn.commit()
        print("✅ Marks updated successfully!")
    
    conn.close()
def delete_student():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    roll_no = int(input("🗑️ Enter Roll Number to delete: "))
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
    row = cursor.fetchone()

    if row:
        confirm = input(f"Are you sure you want to delete student {row[1]}? (y/n): ").lower()
        if confirm == 'y':
            cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
            conn.commit()
            print("✅ Student deleted successfully!")
        else:
            print("❌ Deletion cancelled.")
    else:
        print("❌ Student not found.")
    
    conn.close()

while True:
    print("\n------ Student Result Management ------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by Roll Number")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_all_students()
    elif choice =='3':
        search_by_roll()
    elif choice =='4':
        update_marks()
    elif choice == '5':
        delete_student()
    elif choice =='6':
        print("Bye Kutty! 😘")
        break
    else:
        print("Invalid choice! Try again.")