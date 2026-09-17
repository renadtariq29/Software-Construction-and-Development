print("Student Grade Management System")
print("-------------------------------")

students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")

        english = float(input("Enter English marks: "))
        maths = float(input("Enter Maths marks: "))
        programming = float(input("Enter Programming marks: "))

        total = english + maths + programming
        percentage = (total / 300) * 100

        if percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        student = {
            "name": name,
            "roll": roll_no,
            "english": english,
            "maths": maths,
            "programming": programming,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List")
            print("----------------")

            for student in students:
                print("Name:", student["name"])
                print("Roll No:", student["roll"])
                print("English:", student["english"])
                print("Maths:", student["maths"])
                print("Programming:", student["programming"])
                print("Total:", student["total"])
                print("Percentage:", round(student["percentage"], 2))
                print("Grade:", student["grade"])
                print("----------------")

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found")
                print("Name:", student["name"])
                print("Roll No:", student["roll"])
                print("Percentage:", round(student["percentage"], 2))
                print("Grade:", student["grade"])
                found = True

        if found == False:
            print("Student not found.")

    elif choice == "4":
        if len(students) == 0:
            print("No students available.")
        else:
            total_percentage = 0

            for student in students:
                total_percentage = total_percentage + student["percentage"]

            average = total_percentage / len(students)
            print("Average percentage of all students:", round(average, 2))

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")