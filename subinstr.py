string=input("enter the string")
sub_string=input("enter the sub string")
if sub_string in string:
    print(sub_string,"is present in",string)
else:
    print(sub_string,"is not present in",string)