row =1
while row<=5:
    col=1
    while col<=5:
        if row==1 and col==1:
            print("A",end=" ")
        if row==1:
            print("B",end=" ")   
        elif col ==1:
            print("C",end=" ")
        col+=1
        row+=1
        print()
