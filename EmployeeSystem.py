#Represents an Employee with name, age and salary.
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


# Manages a list of Employees.
class EmployeesManager:

    def __init__(self):
        self._employees_list = []

    def add_employee(self):
        name = input("Enter employee name: ")
        age = self._get_int_input("Enter employee age: ")
        salary = self._get_int_input("Enter employee salary: ")
        emp = Employee(name, age, salary)
        self._employees_list.append(emp)
        print("Employee added successfully!")

    def print_employees(self):
        if self._employees_list:
            for emp in self._employees_list:
                print(f"Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
        else:
            print("No employees at the moment!")

    def delete_by_age(self):
        start_age = self._get_int_input("Enter start age: ")
        end_age = self._get_int_input("Enter end age: ")
        self._employees_list = [emp for emp in self._employees_list if not (start_age <= emp.age <= end_age)]
        print(f"{len(self._employees_list)} employees deleted successfully!")

    def update_salary_by_name(self):
        name = input("Enter employee name to update salary: ")
        new_salary = self._get_int_input("Enter new salary: ")
        for emp in self._employees_list:
            if emp.name == name:
                emp.salary = new_salary
                print(f"{name}'s salary updated successfully!")
                return
        print(f"No employee found with the name {name}.")

    def _get_int_input(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Invalid input! Please enter a valid number.")


class FrontendManager:

    def __init__(self):
        self._emp_manager = EmployeesManager()

    def display_menu(self):
        print("\nEnter your choice:")
        print("1) Add new employee")
        print("2) Print all employees")
        print("3) Delete by age")
        print("4) Update salary by name")
        print("5) End the program")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice from 1-5: ")
            if not choice.isdigit() or int(choice) not in range(1, 6):
                print("Invalid choice! Please enter a valid choice.")
                continue
            choice = int(choice)
            if choice == 1:
                self._emp_manager.add_employee()
            elif choice == 2:
                self._emp_manager.print_employees()
            elif choice == 3:
                self._emp_manager.delete_by_age()
            elif choice == 4:
                self._emp_manager.update_salary_by_name()
            else:
                print("Exiting the program...")
                break


if __name__ == '__main__':
    frontend = FrontendManager()
    frontend.start()
