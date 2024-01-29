r=int(input("No of rows"))
c=int(input("No of columns"))
for i in range(r):
    s=""
    for j in range(c):
        if i==0 or j==0 or i==r-1 or j==c-1:
            s=s+"* "
        else:
            s=s+"  "
    print(s)