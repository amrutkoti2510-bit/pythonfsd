class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "Age:", self.age)

    def study(self, subject):
        print(self.name, "is studying", subject)


s1 = Student("Ravi", 11)
s2 = Student("Raju", 12)

s1.display()
s1.study("Python")

s2.display()
s2.study("Java")