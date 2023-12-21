Num=int(input("Enter the number"))
factors=0
for i in range(1,Num+1):
    if Num%i==0:
        factors=factors+1
if factors==2:
    print("Given number is prime")
elif factors==1:
    print("Given number is neither prime nor composite")
else:
    print("Given number is composite")
