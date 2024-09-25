class Employee:
    language = 'python'
    salary = 1200000
    
    def __init__(self,name,salary,language): #this is dunder method which ks automatically called,we don't need to call it
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"the language is{self.language}.The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print('good morning')

mayank = Employee("Haary",1300000,"JavaScript")
# mayank.name ="MJ84EE21"
print(mayank.name,mayank.salary,mayank.language)


# Q.to print square of a number using constructor

class Calculator:
    def  __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square is {self.n*self.n}")

a=Calculator(4)
a.square()