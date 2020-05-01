
#cartesian product




l=[10,23,40]
l1=[10,34,30]
d=[]

for i in l:
    for x in l1:
        d.append([i,x])        

print(d)







import itertools

l=[10,20,30]
l1=[30,40,50]

for i in itertools.product(l,l1):
    print(i)

print("Manish Praveen Barla")














