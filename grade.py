marks= 86

if marks>=40 and marks<60:
    print("c grade")
elif marks>=60 and marks<80:
    print("b grade")
elif marks>=80 and marks<100:
    print("a grade")
else:
    print("better luck next time")






amount = 5000122101
if amount%100 ==0:
    if amount>=500:
        notes = amount//500
        print("500 of notes are ",notes)
        amount = amount%500
    if amount>=200:
        notes = amount//200
        print("200 of notes are ",notes)
        amount = amount%200
    if amount>=100:
        notes = amount//100
        print("100 of notes are ",notes)
        amount = amount%100
else:
    print('amount should be multiple of 100')
              

              
              
