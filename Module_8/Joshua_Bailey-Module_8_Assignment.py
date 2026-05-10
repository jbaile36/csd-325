import json

def student_list(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : {student['Student_ID']} , Email: {student['Email']}")

def main():
    with open('Student.json', 'r') as file:
        students = json.load(file)
    
    print ("Original student list:")
    student_list(students)

    new_student = {
        "F_Name": "Joshua",
        "L_Name": "Bailey",
        "Student_ID": 21470237,
        "Email": "jobailey@my365.bellevue.edu"
    }

    students.append(new_student)

    print("\nUpdated student list:")
    student_list(students)

    with open('Student.json', 'w') as file:
        json.dump(students, file, indent=4)

    print ("\nStudent.json file has been updated.")

if __name__ == "__main__":    main()

    
