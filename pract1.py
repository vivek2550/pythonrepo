# Constructor 

class Student:
    def __init__(self, name, grade):   
        self.name = name
        self.grade = grade


s1 = Student("vivek",[45,54,99])

print(s1.name)
print(s1.grade)



# static method

class Student:
    @staticmethod
    def myfunction():
        print("hello bacchon")

obj = Student()
obj.myfunction()

