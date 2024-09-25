marks = {
    'mj':100,
    'awe':45,
    'pm':34,
    'rm':23, 
    98: 'lord puneet'
}
print(marks)
print(type(marks))

# print(marks.items()) it will give all items detail

# print(marks.keys()) it will give key value of all item
# print(marks.values())  #it will give value to corresponding keys

marks.update({'pm':98})
print(marks)

# dictionary is unordered
# it is mutable
# it is indexed
# cannot contain duplicate key 


# some questions on dictionary
# Q.write a program to create a dictionary of Hindi words with values
# as their english translation. provide user with an option to look it up

words = {
    'chair':'kursi ',
    'book':'kitaab ',
    'science':'vigyan ',
    'arts':'kala',
    'economics':'arthsastra '
}

sabd = input('enter the word you want to know: ')

ans = words[sabd]
print(ans) #if we write the word that is not in dictionary it will give keyerror