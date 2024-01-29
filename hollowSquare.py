n=int(input("No of sides"))
for i in range(n):
    s=""
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            s=s+"* "
        else:
            s=s+"  "
    print(s)