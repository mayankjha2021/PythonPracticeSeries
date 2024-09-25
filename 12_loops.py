# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# the same thing we can do using loops
# for i in range(1,6): #for loop
#     print(i)

# while loop 

i=1
while(i<6):
    print(i)
    i+=1  # while loop

# Q. print Mahadev 5 times
j =1
while(j<=5):
    print('mahadev',j)
    j=j+1

# for loop
n=18
for i in range (n):
    print(i) #it goes from i to n-1

#for loops with lists

l=[1,4,5,76,34]
for i in l:
    print(i)

# for loop with tuples
t=(0,11,25,53,25,53)
for i in t:
    print(i)

# for loop with string
s='Harry'

for i in s:
    print(i)

# for loop with else 

l1=[1,7,8]

for item in l1:
    print(item)

else:
    print('done') #this is printed when the loop exhaust

