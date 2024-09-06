class Person:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"name = {self.name} age = {self.age} email = {self.email}")

    def __str__(self) -> str:
        return f"name = {self.name} age = {self.age} email = {self.email}"


pallab = Person("Pallab Majumdar", 30, "pallab@gmail.com")

print(pallab)
pallab.display_info()

# inheritance


class Student(Person):
    def __init__(self, name: str, age: int, email: str):
        super().__init__(name, age, email)

    def __str__(self) -> str:
        return super().__str__() + " is a student"


student = Student("Pallab", 30, "pallab@gmail.com")
print(student)
