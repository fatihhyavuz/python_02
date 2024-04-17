set1= set([1,3,5])
set2= set([1,2,3])

print(set1.difference(set2))

print(set1 - set2)

print(set2.difference(set1))

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

print(set1.intersection(set2))

print(set1&set2)

print(set1.union(set2))

print(set1.isdisjoint(set2))
print(set1.issubset(set2))

print(set1.issuperset(set2))