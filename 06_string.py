name ="Mayankjha"

nameshort =name[0:3]#start from index 0 all the way till 3 excluding 3
print(nameshort)

char1 = name[2]
print(char1)

#now negative slicing
char2 = name[-2]
print(char2)

print(name[:4]) #is same as print(name[0:4])
print(name[1:]) #is same as print(name[1:5])

print(name[1:6:4])

#string is immutable i.e if we apply any funcn on string it will not change the original func
