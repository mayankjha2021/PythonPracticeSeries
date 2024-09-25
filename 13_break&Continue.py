for i in range(100):
    if(i==34):
        break #exit the loop right now
    print(i)

for i in  range(100):
    if(i==34):
        continue #skip this iteration
    print(i)

#Q.to print multiplication of any table

a = int(input('Enter the number you want to print: '))
i=1
for i in  range(11):
 # or we can also write it as for i in range(1,11):
    print(a*i)
