class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"hello I am {self.name}")

    def grow_up(self):
        self.age = self.age + 1
    
    def print_age(self):
        print(f"age - {self.age}")


maxym_student = Student(name = "Maxym", age=12)
maxym_student.greeting()

matvii_stydent = Student(name = "Matvii", age=14)
matvii_stydent.greeting()

matvii_stydent.print_age()
matvii_stydent.grow_up()
matvii_stydent.print_age()

maxym_student.print_age()