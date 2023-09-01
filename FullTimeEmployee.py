from ICP3.Employee import Employee


# Inherits from Employee class
class FullTimeEmployee(Employee):
    pass


# Creating instances of Employee and FullTimeEmployee classes
employee1 = Employee("Manisha", "Lakkarsu", 80000, "Developer")
employee2 = Employee("Neeha", "Kethireddy", 90000, "Cloud Engineer")
fulltime_employee1 = FullTimeEmployee("Sravani", "Lankala", 70000, "HR")
fulltime_employee2 = FullTimeEmployee("Aravind", "Swamy", 75000, "Marketing")

# Calculating total salary
all_salaries = employee1.salary + employee2.salary + fulltime_employee1.salary + fulltime_employee2.salary

# Calculating average salary
average_salary = employee1.average_salary(all_salaries)

# Displaying the total and average salary
print(f"Total number of employees: {Employee.num_of_employees}")
print(f"Average Salary of all employees: ${average_salary:.2f}")



