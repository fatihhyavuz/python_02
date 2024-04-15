first_name = "tom "
last_name = " holland"
full_name = first_name + " "+ last_name
print("hello"+" "+ full_name  )
print(type(first_name))


age = 19
age += 1  # age = age + 1
print(age)
print(type(age))  # it`a an int
#  print("my age is " + age) #TypeError: can only concatenate str (not "int") to str  it means we cant collect str 
                           #  and int so we should chance int's type 
print ("my age is " + str(age))

height = 170.5 
print("your height is " + str(height) + "cm")
print(type(height))  # float 

human = False # if i put a bool in "" it turn into a str. 
print("are you a human: " + str(human))
print(type(human)) # bool