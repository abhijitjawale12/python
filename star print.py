for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0)or(row==1 and col%3==0)or (row-col==2)or(row+col==8):
             print("*",end=" ")
        else:
             print(" ",end=" ")
    print()      




for row in range(7):
    for col in range(5):
        if row==0 and col in{1,2,3}:
            print("A",end=" ")
        elif row in{1,2,3,4,5,6} and col in{0,4}:
            print("A",end=" ")
        elif row==3:
            print("B",end=" ")
        else:
            print(" ",end=" ")
    print()    
         
 
