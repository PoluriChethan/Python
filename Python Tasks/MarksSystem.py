# Define Student class
class Student:
    
    # Constructor method (Automatically runs when object is created)
    def __init__(self):
        # Taking student details as input
        self.name = input("Enter Student name : ")              # Student name
        self.attendance = int(input("Enter student attendance : "))  # Attendance percentage
        self.percentage = int(input("Enter student percentage : "))  # Marks percentage

    # Method to check whether student passed or failed
    def check_result(self):
        
        # Condition for passing:
        # Attendance must be 75% or more
        # Percentage must be 40% or more
        if self.attendance >= 75 and self.percentage >= 40:
            print(f"{self.name} is Pass")
        
        # If attendance is less than 75
        elif self.attendance < 75:
            print(f"{self.name} is Fail because of Low Attendance")
        
        # If percentage is less than 40
        else:
            print(f"{self.name} is Fail because of Low Percentage")

    # Method to display student details
    def display(self):
        print("Student name : ", self.name)
        print("Student attendance : ", self.attendance)
        print("Student Percentage : ", self.percentage)


# Create object of Student class
# This will automatically call __init__ method
result = Student()

# Call method to check result
result.check_result()

# Call method to display student details
result.display()
