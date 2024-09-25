# a = int(input('kindly enter your age:'))

# if(a>18):
#     print("you are above age of consent")
#     print('you are good to go')

# elif(a<0):
#     print('bsdk mouse hai haath mein to kuch bhi daaloge')

# elif(a<3):
#     print('akhand chutiya ho ji')
# else:
#     print('you are not eligible')

# print('jai hind')   


# there can be any number of Elif statement
# Last else is executed only if all the conditions inside Elifs fail.

# Q.take the marks of students in 3 subjects, marks in each subject>33 and total 
# percentage should be greater than 40%

marks1 = int(input('Enter the marks: '))
marks2 = int(input('Enter the marks: '))
marks3 = int(input('Enter the marks: '))

total = 100*((marks1+marks2+marks3)/300)

if(total >=40 and marks1>33 and marks2>33 and marks3>33):
    print('you are pass')
    print('you got total percentage: ',total)

else:
    print('you are fail,try next year')
 