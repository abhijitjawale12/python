#for loop

for row in range(1,8,1):
    for col in range(1,8,1):
       if col==1 and row==1:
           print("C" , end=" ")
       elif col ==1:
           print("B" , end=" ")
       elif row==1:
           print("A" , end=" ")
    print()    


        

