# Joshua Bailey Module 8 Assignment CSD 325
# This program reads a JSON file and displays the original student list,
# adds a new student to the list, displays the updated list,
# and then saves the updated list to the JSON file.


import json

# Function to display the list of students
def student_list(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : {student['Student_ID']} , Email: {student['Email']}")

# Main function to execute the program
def main():
    # Read the existing student data from the JSON file
    with open('Student.json', 'r') as file:
        students = json.load(file)
    
    # Display the original student list
    print ("Original student list:")
    student_list(students)

    # Add a new student to the list
    new_student = {
        "F_Name": "Joshua",
        "L_Name": "Bailey",
        "Student_ID": 21470237,
        "Email": "jobailey@my365.bellevue.edu"
    }

    # Append the new student to the existing list
    students.append(new_student)

    # Display the updated student list
    print("\nUpdated student list:")
    student_list(students)

    # Save the updated student list back to the JSON file
    with open('Student.json', 'w') as file:
        json.dump(students, file, indent=4)

    # Notify the user that the JSON file has been updated
    print ("\nStudent.json file has been updated.")

# Call the main function to run the program
if __name__ == "__main__":    main()

    
