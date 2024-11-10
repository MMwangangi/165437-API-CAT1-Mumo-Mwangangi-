# Employee class definition
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary:.2f}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary for {self.name} has been updated to ${self.salary:.2f}.")

# Department class definition
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} (ID: {employee.employee_id}) has been added to the {self.department_name} department.")

    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for the {self.department_name} department is ${total_salary:.2f}.")
        return total_salary

    def display_all_employees(self):
        if self.employees:
            print(f"Employees in the {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in the {self.department_name} department.")

# Interactive Code
if __name__ == "__main__":
    # Create a department
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("\nEmployee and Department Management System")
        print("1. Add an employee")
        print("2. Update an employee's salary")
        print("3. Display all employees")
        print("4. Calculate total salary expenditure")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter the employee's name: ")
            employee_id = input("Enter the employee's ID: ")
            salary = float(input("Enter the employee's salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            employee_id = input("Enter the employee ID to update salary: ")
            employee = next((e for e in department.employees if e.employee_id == employee_id), None)
            if employee:
                new_salary = float(input(f"Enter the new salary for {employee.name}: "))
                employee.update_salary(new_salary)
            else:
                print("Employee not found.")

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            department.calculate_total_salary()

        elif choice == "5":
            print("Exiting the Employee and Department Management System.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 5.")
