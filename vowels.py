vowels_list=["a","e","i","o","u"]
input=input("enter the input")
c=0
for i in input:
    if i.lower() in vowels_list:
        print("vowels are present in the given input")
        c+=1
        break
    else:
        continue
if c==0:
    print("vowels are not present in the given input")
