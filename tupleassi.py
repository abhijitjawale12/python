a = ['rahul', 'rohit', 'abhijit', 'aditya', 'saurabh', 'prabuddha']
length_five = []
for name in a:
    if len(name) == 5:
        length_five.append(name)
print("Names with length 5:", length_five)





a = [163, 11, 27, 24, 140, 556]
odd_numbers = [num for num in a if num % 2 != 0]
print("Odd numbers:", odd_numbers)
