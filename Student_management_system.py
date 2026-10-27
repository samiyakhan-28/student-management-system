class Student:
    def __init__(self,student_name, Roll_number,Branch,Semester):
        self.student_name = student_name
        self.Roll_number = Roll_number
        self.Branch = Branch
        self.Semester = Semester
    def display_details(self):
        print("Student Details")
        print(f"Name: {self.student_name}")
        print(f"Roll Number: {self.Roll_number}")
        print(f"Semester: {self.Semester}\n")
    def update_semester(self, new_semester):
        self.Semester = new_semester
obj1 = Student("Aman",101, "CSE", 5)
obj2=Student("Priya", 102, "IT", 3)
obj3=Student("Rahul", 103, "CSE", 4)
obj1.display_details()
obj2.display_details()
obj3.display_details()
#Updating Semester
obj1.update_semester(6)
obj1.display_details()
    