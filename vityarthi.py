# STUDENT GRADE MANAGEMENT SYSTEM

students = []


# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


# Function to add student
def add_student():
    print("\n--- ADD STUDENT ---")

    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    print("\nEnter marks out of 100:")

    maths = float(input("Maths: "))
    python = float(input("Python: "))
    physics = float(input("Physics: "))
    english = float(input("English: "))
    chemistry = float(input("Chemistry: "))

    total = maths + python + physics + english + chemistry
    percentage = total / 5
    grade = calculate_grade(percentage)

    student = {
        "roll": roll,
        "name": name,
        "maths": maths,
        "python": python,
        "physics": physics,
        "english": english,
        "chemistry": chemistry,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    print("\nStudent added successfully!")
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)


# Function to display one student
def display_student(student):
    print("\n-----------------------------")
    print("Roll Number :", student["roll"])
    print("Name        :", student["name"])
    print("-----------------------------")
    print("Maths       :", student["maths"])
    print("Python      :", student["python"])
    print("Physics     :", student["physics"])
    print("English     :", student["english"])
    print("Chemistry   :", student["chemistry"])
    print("-----------------------------")
    print("Total       :", student["total"])
    print("Percentage  :", student["percentage"], "%")
    print("Grade       :", student["grade"])
    print("-----------------------------")


# Function to display all students
def display_all_students():
    print("\n--- ALL STUDENTS ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        display_student(student)


# Function to search student
def search_student():
    print("\n--- SEARCH STUDENT ---")

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            display_student(student)
            return

    print("Student not found.")


# Function to update marks
def update_student():
    print("\n--- UPDATE STUDENT ---")

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:

            print("Enter new marks:")

            student["maths"] = float(input("Maths: "))
            student["python"] = float(input("Python: "))
            student["physics"] = float(input("Physics: "))
            student["english"] = float(input("English: "))
            student["chemistry"] = float(input("Chemistry: "))

            student["total"] = (
                student["maths"]
                + student["python"]
                + student["physics"]
                + student["english"]
                + student["chemistry"]
            )

            student["percentage"] = student["total"] / 5
            student["grade"] = calculate_grade(student["percentage"])

            print("Student record updated successfully!")
            return

    print("Student not found.")


# Function to delete student
def delete_student():
    print("\n--- DELETE STUDENT ---")

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main program
while True:

    print("\n===================================")
    print("   STUDENT GRADE MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_all_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank you for using Student Grade Management System!")
        break

    else:
        print("Invalid choice! Please try again.")