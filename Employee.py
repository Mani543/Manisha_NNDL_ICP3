class Employee:
    num_of_employees = 0  # Variable to count the number of employees

    # constructor to initialize name, family, salary, department
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.num_of_employees = Employee.num_of_employees + 1

    # Function to calculate average salary
    def average_salary(self, full_salaries):
        return full_salaries / Employee.num_of_employees