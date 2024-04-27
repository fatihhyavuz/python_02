salaries = [1000,2000,3000,4000,5000]

def new_salary(x):
    return x * 20 /100 + x
new = []
for salary in salaries:
    new.append(new_salary(salary))

for salary in salaries:
    if salary > 3000:
        new.append(new_salary(salary))
    else:
        new.append(new_salary(salary*2))    

print(new)        

[new_salary(salary) if salary > 3000 else new_salary(salary*2) for salary in salaries]

students = ["ali","mary","adam","chris"]

students_no = ["ali","adam"]

[student.lower() if student in students_no else student.upper() for student in students ]

# dictinary

dictionary = { "a":1,
               "b":4,
               "c":5,
               "d":6}

dictionary.keys()
dictionary.values()
dictionary.items()

{k.upper : v**2 for (k,v) in dictionary.items()}

# cift sayilarin karesini alinip bir sozluge eklenecek 

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n]= n**2 
        print(new_dict)
 
print({ n : n**2  for n in numbers if n % 2 == 0})