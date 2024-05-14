a = ('abc',24,'thane')
(name, age,city)=a
print(name)
print(age)
print(city)


b=(11,22,33,1,2,3,4,5,6,5)
(a,b,c,*d)=b
print(a)



a = (1,2,3,44)
b= list(a)
b[1]=22
b[2]=33
a =tuple(b)
print(a)





a = ['rahul', 'rohit', 'abhijit', 'aditya', 'saurabh', 'prabuddha']

# Initialize an empty list to store names with length 5
length_five = []

# Iterate through each element in the list
for name in a:
    # Check if the length of the name is 5
    if len(name) == 5:
        # Add the name to the length_five list
        length_five.append(name)

print("Names with length 5:", length_five)










