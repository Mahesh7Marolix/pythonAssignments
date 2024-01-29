n=int(input())
print("  "*(n-1)+"* ")
for i  in range(n-2):
    s="  "*(n-i-2)+"* "+"  "*(2*i+1)+"* "
    print(s)
print("* "*(2*n-1))
