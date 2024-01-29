n=int(input("Enter no. of rows required"))
print("* "*n)
for i in range(n-2):
    s="  "*(i+1)+"* "+"  "*(n-3-i)+"* "
    print(s)
print("  "*(n-1)+"* ")