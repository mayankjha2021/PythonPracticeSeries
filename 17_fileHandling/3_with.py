f= open("file.txt")

print(f.read())
f.close()

# the same can be written with the help of mWITH statement like this

with open("file.txt") as f:
    print(f.read())
    #you don't have to explicitly close the file
    