# Student Management System
# Python Data Structures: List, Tuple, Set, Dictionary


# List
students = []


# Set
courses = {"Python", "Database", "Django"}


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))

    # Tuple
    basic_info = (student_id, name)

    # Dictionary
    student = {
        "basic_info": basic_info,
        "age": age,
        "courses": set()
    }

    students.append(student)

    print("Student added successfully!")


def enroll_course():
    student_id = input("Enter Student ID: ")
    course = input("Enter Course Name: ")

    if course not in courses:
        print("Course is not available.")
        return

    for student in students:
        if student["basic_info"][0] == student_id:
            student["courses"].add(course)
            print("Course added successfully!")
            return

    print("Student not found.")


def show_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        student_id, name = student["basic_info"]

        print("\n--------------------")
        print("Student ID:", student_id)
        print("Name:", name)
        print("Age:", student["age"])
        print("Courses:", student["courses"])


def show_courses():
    print("\nAvailable Courses:")

    for course in courses:
        print("-", course)


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Enroll Course")
    print("3. Show Students")
    print("4. Show Courses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        enroll_course()

    elif choice == "3":
        show_students()

    elif choice == "4":
        show_courses()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")