# practices

# 01

x = 8
print(type(x))
z = ("a","b")
print(type(z))
d=["a","b","c"]
print(type(d))
c={2,3,4,5}
print(type(c))
e= {"name":"jake","age":19}
print(type(e))

# 02

text = "hello,my,name.is tom."
text.upper()
text.replace("," ,  " ").replace("."," ")

# 03

list=["d","a","t","a","s","c","i","e","n","c","e"]
list2 = []

len(list)
print(list[0])
print(list[3])

list.pop(8)


list2.append(list[0:4])
print(list2)

list.append("a")

list.insert(8, "n")
print(list)

# 03

dict= {"tom":["use",19],
       "mark":["indea",23],
       "mary":["england",29]}

print(dict.keys())
print(dict.values())
dict.update()

#04

cift = []
tek = []
def func(list):
  for new_list in list:
    if new_list % 2 == 0:
     cift.append(new_list)
    else:
      tek.append(new_list)
  return func

func([1,2,3,4,5,6])
print(cift)
print(tek)

# 05

students = ["kirk","jon","adam","tom","mary","andrew"]

for index, student in enumerate(students, start=1):
  if index <= 3:
    print("enginering " + str(index)+". student: "+ student)
  else: 
     print("medicine " + str(index)+". student: "+student) 

# 06 

pin_of_leasson = [123,234,456,458]
name_of_leasson = ["mat","lit","bio","phs"]
limit_of_number = [23,56,12,34]



new = zip(pin_of_leasson,name_of_leasson,limit_of_number)

new_new= list(new)
print(new)
