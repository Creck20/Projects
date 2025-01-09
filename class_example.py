# Chat GPT's explanation of class instantiation. 

class MyClass:
    # Class attribute
    class_attribute = "I am a class attribute"

    # Constructor
    def __init__(self, instance_attribute):
        # Instance attribute
        self.instance_attribute = instance_attribute

    # Instance method
    def instance_method(self):
        return f"Instance method called, instance_attribute: {self.instance_attribute}"

    # Class method
    @classmethod
    def class_method(cls):
        return f"Class method called, class_attribute: {cls.class_attribute}"

    # Static method
    @staticmethod
    def static_method():
        return "Static method called"

# Creating an instance of MyClass
my_instance = MyClass("I am an instance attribute")

# Accessing instance and class attributes
print(my_instance.instance_attribute)  # Output: I am an instance attribute
print(MyClass.class_attribute)  # Output: I am a class attribute

# Calling instance, class, and static methods
print(my_instance.instance_method())  # Output: Instance method called, instance_attribute: I am an instance attribute
print(MyClass.class_method())  # Output: Class method called, class_attribute: I am a class attribute
print(MyClass.static_method())  # Output: Static method called


"""
Explanation:
Class Definition:

class MyClass: defines a new class named MyClass.
Class Attributes:

class_attribute is a class attribute, shared among all instances of the class.
Constructor (__init__ method):

def __init__(self, instance_attribute): initializes new instances of the class. self refers to the instance being created, and instance_attribute is an instance-specific attribute.
Instance Method:

def instance_method(self): defines a method that operates on an instance of the class.
Class Method:

@classmethod decorator and def class_method(cls): define a method that operates on the class itself rather than an instance. cls refers to the class.
Static Method:

@staticmethod decorator and def static_method(): define a method that does not operate on either the instance or the class.
Creating an Instance:

my_instance = MyClass("I am an instance attribute") creates a new instance of MyClass.
Accessing Attributes and Methods:

You can access instance attributes and methods through the instance (my_instance).
You can access class attributes and methods directly through the class (MyClass).
"""