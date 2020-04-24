"""
#prime numbers
n=int(input("Enter the value of n"))

x=1
while n:
    i=2
    while i<x:
        if x%i==0:
            break
        else:
            i+=1
    if i==x:
        print(x)
        n-=1
    x+=1    
        

#union of two sets
n=eval(input("enter the elements of sets"))
n1=eval(input("enter the elements of set"))

print(n.union(n1))

#common elements in two sets
n=eval(input("enter the elements of sets"))
n1=eval(input("enter the elements of set"))

for x in n:
    for c in n1:
        if x==c:
            print(x)
        else:
            pass



#cartesian product




l=[10,23,40]
l1=[10,34,30]
d=[]

for i in l:
    for x in l1:
        d.append([i,x])        

print(d)




"""


import itertools

l=[10,20,30]
l1=[30,40,50]

for i in itertools.product(l,l1):
    print(i)
















