class Employee:
    lang='python' #this is a class attribute
    salary = 1200000

     getInfo(self):
           print(f"The language is{self.lang}.The salary is{self.salary}")

     greet(self):
           print("good morning")

mayank =Employee()

mayank.greet()
mayank.getInfo()