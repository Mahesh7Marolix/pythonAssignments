n=int(input())
for i in range(n):
    s="  "*(n-i-1)
    for j in range(i+1):

        s=s+" "+chr(65+j)
    for k in range(i):
        s=s+" "+chr(65+j+k+1)

    print(s)