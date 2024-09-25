class Employee:
    lang ='py'#this is a class attribute
    salary = 1200000

harry = Employee() #here we made a object
harry.name = 'Harry'#this is a object attribute
print(harry.name,harry.lang,harry.salary)

rohan = Employee()
rohan.name ='mj84ee21'
rohan.lang ='javascript'#this is an instance attribute
print(rohan.name,rohan.salary,rohan.lang)

# Here name is object attribute and salary and language 
# are class attribute as they directly belong to the class