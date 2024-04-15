name = input("what is your name?")  # the value that we take from input always str so we need to convert it if we'd like to use it as a int or float
age= int(input("how old are you?"))
age= age+1 
height= float(input("how tall are you?"))


print("hello "+ name)
print("i am "+ str(age)+ " years old ")
print("you are " + str(height)+"cm tall")