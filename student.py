class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

s1 = Student("Rahul", 101, 85)
s1.display()
s1.result()
