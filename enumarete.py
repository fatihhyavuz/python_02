# enumerate
students = ["tom", "mary","adam","mark"]
for student in students:
  print(student)

for index, student in enumerate(students):
  print(index,student)

  a = []
  b = []
for index, student in enumerate(students):
  if index % 2 == 0:
    a.append(student)

  else:
    b.append(student)

  print(a,b)

  students = ["john", "mark","vennessa","mary"]
aa= []
bb= []
result= []
for index, student in enumerate(students):
   if index % 2 == 0 :
     aa.append(student)
   else:
     bb.append(student)

print(aa,bb)

result.append(aa)
result.append(bb)
print(result)

students = ["john", "mark","vennessa","mary"] ###

def divide_students(students):
  groups = [[],[]]
  for index, student in enumerate(students):
    if index % 2 == 0:
      groups[0].append(student)
    else:
      groups[1].append(student)

  return groups

def alternating_with_enumarete(string):
   new_string = ""
   for i, letter in enumerate(string):
     if i % 2 == 0:
        new_string += letter.upper()
     else:
        new_string += letter.lower()
   print(new_string)

alternating_with_enumarete("hello my name is tom ")

