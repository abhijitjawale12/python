import functools

a = functools.reduce(lambda x,y:x+y,[1,2,3,4,5,6])
print(a)






def checkprime(n=6):
    for i in range(2,n,1):
        r = n%i

        if r==0:
            print(f" n is not prime number")
            break
        else:
            print(f"n is prime number")

            checkprime(5)
