#first path 
#study path 
#bob

#Styding "Introduction to the language PY"
"""
for i in range(3):
    print (i)

for a in range(3):
    pass
print (a)
"""
#new
#Variables and assignment
"""
a = 1
b = 1.0
c = True
print (type(a), type(b), type(c))

a = 1; b = 1.0; c = True
print (a, b, c)

a1, b1, c1 = 1, 1.0, True
print (a1, b1, c1)
"""

#new
#Basic language constructs

#Conditions
"""
a =1
if a == 1:
    print (1)
elif a==2:
    print (1)
else:
    print ("Не 1 и не 2")

d = "Yes" if a==1 else "No"
print(d)
"""

#Сycles
"""
arr = [3,4,5,6,7]
for a in arr:
    print (a)

for a in range(3,7):
    print (a)

for s in 'строка':
    print (s)

for i, s in enumerate('строка'):
    print (i,s)
"""

#Other operate
    #break 
for a in range(3,10):
    if a % 5 == 0:
        break
    print (a)

    #continue
for a in range(3,10):
    if a % 5 == 0:
        continue
    print (a)
    
