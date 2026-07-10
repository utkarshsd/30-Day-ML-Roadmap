# MINI PROJECT 
# STUDENT MANGEMENT SYSTEM


students = {}

while True:
    print("\n====== Student Management ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        students[name] = {
            "Age": age,
            "Marks": marks
        }

        print("✅ Student Added Successfully!")

    elif choice == "2":

        if not students:
            print("No students found.")
        else:
            print("\nStudent Records")
            print("--------------------------")
            for name, details in students.items():
                print(f"Name : {name}")
                print(f"Age  : {details['Age']}")
                print(f"Marks: {details['Marks']}")
                print("--------------------------")

    elif choice == "3":

        name = input("Enter student name: ")

        if name in students:
            print(students[name])
        else:
            print("Student Not Found!")

    elif choice == "4":

        name = input("Enter student name: ")

        if name in students:
            del students[name]
            print("Student Removed!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")    