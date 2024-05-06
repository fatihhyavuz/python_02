# lambda map filter reduce
def summer(a,b):
  return a+b

new_sum = lambda a,b: a+b
new_sum(4,5)

#map


salaryies = [ 1000,2000,3000,4000,5000]

def new_salary(x):
  return x * 20/100 +x

new_salary

for salary in salaryies:
     print(new_salary(salary))

#list(map(new_salary, salaryies))

list(map(lambda x: x*20/100 +x, salaryies))

#filter

list_store= [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x%2 ==0,list_store))

#reduce

from functools import reduce
list_store =[1,2,3,4]
reduce(lambda a, b: a+b, list_store)
