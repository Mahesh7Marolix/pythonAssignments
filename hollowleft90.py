n=int(input("Enter no. of rows required"))
print("* "*n)
for i in range(n-2):
    s="* "+"  "*(n-i-3)+"* "
    print(s)
print("* ")