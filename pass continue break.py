for i in range(1,10,1):
    pass

#break

for i in range(1,101,1):
    print(i)
    if i==10:
        break


#continue

i =10
while i<=20:
    i+=1
    if i==15:
        continue
    print(i)


    
for i in range(1,110,1):
    if i%3!=0:
        continue
    print(i)
