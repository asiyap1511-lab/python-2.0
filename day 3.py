'''
x=10
y=3.14
z=3+2j

print(type(x))
print(type(y))
print(type(z))


a=10
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)#float
print(a//b)#floor
print(a%b)#modulas:remainder
print(a**b)#power


x=10
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x<=y)

print(x>5 and x<10)#and
print(x<5 or y<11)#or
print(not(x==y))#or



import math

x=10;y=3

#ceil(+1)
print(math.ceil(4.1))
print(math.ceil(4.6))

#floor(1st digit)
print(math.floor(4.2))
print(math.floor(4.5))

#round(even = only for .5)
print(round(5.2))
print(round(6.4))




x=[1,2,4,5]#list as integer
y=["asiya","anu","sufee"]#list as string
z=[True,False,True]
z1=["asiya",4,True]

print(x)
print(y)
print(x[1])#2
print(y[2])#sufee
print(z)
print(z1)



#list operation
x = [1,4,5]
y=["asiya","sufee",]
x.append(7) #[1,4,5,7]
y.append("annu")
x.remove(4)
remove_x=x.pop(1)

print(x)
print(y)
print(x)

'''


a=["asiya","annu","sufee"]
b=[2,3,5,6,7]
c = "asiya"
print(len(a[0]))#len(function)
print(len(b))
print(len(c))

print(5 in b)