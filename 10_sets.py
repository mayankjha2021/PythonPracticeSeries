d = {} # empty dictionary

s = {1,2,3,4,3} #sets
print(type(s))
print(s)

# s.pop() # it will remove random element in a set
# s.clear() # it will clear whole set 

# we can't repeat value inside set it will only print repeated value one time
# sets are unindexed
# there are no way to change items in set
# sets can't contain duplicate value
# can't accessed elements in a  set
s1={2,3,4,5}
s2={6,7,4,9}
print(s1.union (s2))
print(s1.intersection(s2))
print(s1-s2)
print(s2-s1)