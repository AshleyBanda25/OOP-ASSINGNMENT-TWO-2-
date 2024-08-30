class Employee:
    def __init__(self, name, emp_id, salary):
        self.__name = name         # Private variable
        self.__emp_id = emp_id     # Private variable
        self.__salary = salary     # Private variable

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for employee ID
    def get_emp_id(self):
        return self.__emp_id

    # Setter for employee ID
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary with validation
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = salary

# Example usage
try:
    emp = Employee("John Doe", 123, 50000)
    print(f"Name: {emp.get_name()}")
    print(f"Employee ID: {emp.get_emp_id()}")
    print(f"Salary: ${emp.get_salary()}")

    # Update salary with valid value
    emp.set_salary(55000)
    print(f"Updated Salary: ${emp.get_salary()}")

    # Attempt to set a negative salary
    emp.set_salary(-1000)  # This will raise an exception
except ValueError as e:
    print(e)

'''Here's how you can implement encapsulation in Python to manage 
employee records with private variables and public getters and setters:'''#python
class Employee:
    def __init__(self, name, emp_id, salary):
        self.__name = name         # Private variable
        self.__emp_id = emp_id     # Private variable
        self.__salary = salary     # Private variable

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for employee ID
    def get_emp_id(self):
        return self.__emp_id

    # Setter for employee ID
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary with validation
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = salary

# Example usage
try:
    emp = Employee("John Doe", 123, 50000)
    print(f"Name: {emp.get_name()}")
    print(f"Employee ID: {emp.get_emp_id()}")
    print(f"Salary: ${emp.get_salary()}")

    # Update salary with valid value
    emp.set_salary(55000)
    print(f"Updated Salary: ${emp.get_salary()}")

    # Attempt to set a negative salary
    emp.set_salary(-1000)  # This will raise an exception
except ValueError as e:
    print(e)

'''Explanation of the Code and Encapsulation:

1. Private Variables:
   - In Python, private variables are denoted by prefixing the variable
     names with double underscores ('__'). In the 'Employee'
     class, '__name', '__emp_id', and '__salary' are private variables.
     This means they cannot be accessed directly from outside the class. 
     This is a way to ensure that these variables are hidden and protected from unauthorized
     access or modification.

2. Public Getters and Setters:
   - Getters are methods that allow you to retrieve the value of private variables.
     For example, 'get_name()' returns the value of '__name'.
   - Setters are methods that allow you to update the value of private variables. For example,
     'set_name(name)' updates the value of '__name'.

3. Validation in Setters:
   - The setter for '__salary' includes validation to ensure that the 
   salary cannot be set to a negative value. If an invalid value is provided,
   a 'ValueError' is raised. This demonstrates how encapsulation not only
   hides the data but also enforces rules and constraints to maintain data integrity.

4. Encapsulation Implementation:
   - Encapsulation is implemented by restricting direct access to the data fields
    ('__name', '__emp_id', and '__salary') and providing controlled access 
    through getter and setter methods. This ensures that any modifications to
    the data are subject to validation rules, protecting the internal state
    of the object from being changed inappropriately.

By following these principles, you create a robust and maintainable class that protects the integrity of its data while still providing a clear and controlled way to interact with it.
'''