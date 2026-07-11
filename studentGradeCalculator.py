# Student Grade Calculator

name = input("Enter student name: ")

subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(subjects):
    marks = float(input(f"Enter marks for Subject {i+1}: "))
    total += marks

percentage = total / subjects

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- RESULT -----")
print("Student:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

