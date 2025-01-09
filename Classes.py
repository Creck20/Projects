# Class example: 

class Employee: 
    
    raise_amount = 1.04

    def __init__(self, first, last, pay): # The instance is the first argument. 
        # Calling the instance self is a convention.
        self.first = first
        self.last = last
        self.pay = pay

    def fullName(self): # Instance is the first argument.
        return f"{self.first} {self.last}" # Use parameter for it to be used in all instances.
    
    def ApplyRaise(self):
        self.pay = int(self.pay * self.raise_amount) # Must use parameter when using attribute



emp_1 = Employee("Donna", "Noble", 1000) # The instance is passed automatically. Leave off 'self'.
emp_2 = Employee("John", "Smith", 500)

# emp_1.ApplyRaise()
# print(emp_1.pay)


# print(emp_1.first, emp_1.last, f"Pay: {emp_1.pay}")
# print(emp_2)
# print("Note that they are class objects.")

# print(emp_1.fullName())
# print(f"You can also print attributes: {emp_1.first}")

# print(f"You can also call the method from the classname: {Employee.fullName(emp_1)}")
# print("Note that the instance is given as an argument.")

# Python calls attributes "Class Variables"

# Inheritance in python: 

class Developer(Employee):
    raise_amount = 1.10 # Attributes can be changed.

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # Same as : Base() in C# 
        self.prog_lang = prog_lang




dev_1 = Developer("Bob", "Johnson", 1000, "Python")
print(dev_1.prog_lang)






