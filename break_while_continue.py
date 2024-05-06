#break while continue

salarys = [ 1000 , 2000 ,3000, 4000, 5000]

for salary in salarys:
  if salary == 3000:

      break
  print(salary)


for salary in salarys:
  if salary ==3000:
    continue
  print(salary)

#while

number = 1
while number < 5:
  print(number)
  number += 1