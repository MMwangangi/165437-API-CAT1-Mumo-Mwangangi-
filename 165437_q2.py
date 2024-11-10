# Student class definition
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name} (ID: {self.student_id}):")
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print(f"{self.name} has no grades yet.")

# Instructor class definition
class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) has been added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found.")

    def display_students_grades(self):
        if self.students:
            print(f"Grades for students in {self.course_name}:")
            for student in self.students:
                student.display_grades()
        else:
            print("No students enrolled in this course.")

# Interactive Code
if __name__ == "__main__":
    # Create an instructor for a specific course
    instructor = Instructor("Dr. Smith", "Introduction to Python")

    while True:
        print("\nOnline Course Management")
        print("1. Add a student")
        print("2. Assign a grade to a student")
        print("3. Display all students and their grades")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            student_name = input("Enter the student's name: ")
            student_id = input("Enter the student's ID: ")
            student = Student(student_name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            student_id = input("Enter the student's ID to assign a grade: ")
            assignment_name = input("Enter the assignment name: ")
            grade = input("Enter the grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == "3":
            instructor.display_students_grades()

        elif choice == "4":
            print("Exiting the Online Course Management system.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 4.")
