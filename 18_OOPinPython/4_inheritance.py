class Employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
class coder:
    language = "Python" 
    def printLanguages(self):
        print(f"out of all the languages here is your language:{self.language}")     
# class Programmer:
#     company = "ITC InfoTech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
        
#     def showLanguage(self):
#         print(f"the name is {self.name} and he is good in {self.language} language")

#we can do that by above way but this is too lenghty, here we will use inheritance method

# here it is

class Programmer(Employee):
    company = "ITC InfoTech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good in {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()
print(a.company,b.company)