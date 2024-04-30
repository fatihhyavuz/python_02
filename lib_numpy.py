import numpy as np
'''
print(np.array([1,2,3,4,5]))
print(np.zeros(10, dtype=int))
print(np.random.randint(0,10,size=10))
print(np.random.normal( 10 ,4,(3,4)))

a = np.random.randint(10, size= 5)
print(a)
print(a.ndim) # boyut 
print(a.shape)
print(a.size)
print(a.dtype)

np.random.randint(1,10,size=9)

ab = np.random.randint(1,10,size=9).reshape(3,3) # boyut degistirme "reshaping"

print(ab)
# index islemleri 
abc = np.random.randint(10,size =10 )

print(a[0])
print(a[0:5])
abc[0 ]=999
print(abc)
m = np.random.randint(10, size=(3,5))
print(m[0,0])
print(m[2,3])
m[2,3]= 999
print(m)
print(m[:,1])
print(m[0:2,0:3])

v = np.arange(0,30,3 )
v[1]
v[4]

catch = [1 ,2 ,3]

print(v[catch]) # fancy index 
'''
h = np.array([1,2,3,4,5,6])

new = []

for n in h:
    if n > 3 : 
        new.append(n)
print(new)    

# numpy kullanarak 

print(h>3)
print(h[h>3])

