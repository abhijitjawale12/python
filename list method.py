#append
a= [1,1,1,2,3]
a.append(11)
a.append(12)
print(a)

#insert
a.insert(10,"Abhijit")
print(a)

b=[10]
b.extend(a)
print(b)
print(a+b)

      
#remove
a.remove("Abhijit")
print(a)

#pop
a.pop(0)
print(a)

#del
#del a
del a[1]
print(a)


#clear
a.clear()
print()
