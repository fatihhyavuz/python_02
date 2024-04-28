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
numbers2 = range(10)
new_d = { n : n ** 2 for n in numbers2 if n % 2 == 0 }

print(new_d)

'''

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n]= n**2 
        print(new_dict)
 
{ n : n**2  for n in numbers if n % 2 == 0}
'''

"""
iing = ["heling","jking","koling","hk","oo"]

[":)" + u if "ing" in u else u for u in iing  ]


[ upper.upper() for upper in iing]
"""
import seaborn as sns 
df = sns.load_dataset("car_crashes")
df.columns

"""
for col in df.columns:
    print(col.upper())
a = []
for col in df.columns:
    a.append(col.upper())

df.columns =a     

df.columns = [col.upper() for col in df.columns]

print(["flag" + i if "INS" in i else "no_flag" + i for i in df.columns])
"""

# amac key'i string, value su asagidaki gibi bir liste olan sozluk olusturmak
# sadece sayisal deger;er icin yapmayi istiyoruz 

import seaborn as sns 
df = sns.load_dataset("car_crashes")
df.columns

num_coals = [col for col in df.columns if df[col].dtype != "O"]
print(num_coals)
soz ={}
agg_list = ["mean","min","max","sum"]

for col in num_coals:
    soz[col]= agg_list
    print(soz)
# kisa yol 

new_dict = {col : agg_list for col in num_coals}

print(df[num_coals].head())


print(df[num_coals].agg(new_dict))