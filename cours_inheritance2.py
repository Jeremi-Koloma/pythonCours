class Person:
    def __init__(self, fist_name, last_name, age):
        self.fist_name = fist_name;
        self.last_name = last_name;
        self.age = age;

    def __str__(self):
        return f"{self.fist_name} is {self.age} years old"
    
class Professor(Person):
    def __init__(self, fist_name, last_name, age, modules):
        super().__init__(fist_name, last_name, age)
        self.modules = modules
    
    def __str__(self):
        return super().__str__()+" " + " - ".join(self.modules)
    
modules = ["JavaScript", "React", "Python", "Flutter"]
prof1 = Professor("John", "KEITA", 45, modules)
print(prof1)