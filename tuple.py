#tuple with comnstructor
a = tuple((1,2,3,4,5))
print(type(a))


#tuple without constructor
a=(1,2,3,4,5,5,6)
print(type(a))
b=(1,)
print(type(b))

#a[0]= 'rohit'
print(a[-1])
print(a[0])
print(a)

#can not add or remove valuse from tuple
#but you can add two tuples together
b = (11,22)
print(a+b)
