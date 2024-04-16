# we cant chance the tuples 

a_tuple= ("john","tom",3)

print(type(a_tuple))

# a_tuple[0] = 99 # TypeError: 'tuple' object does not support item assignment

a_tuple = list(a_tuple)  # if we want to chance tuple we can convert it a list 
a_tuple[0] = 99
print(a_tuple)

a_tuple= tuple(a_tuple)
print(type(a_tuple))