
#Given an integer n, for every integer i <= n,
 #the task is to 
#print “FizzBuzz” 
#if i is divisible by 3 and 5
# “Fizz” if i is divisible by 3, 
#“Buzz” if i is divisible by 5 or i (as a string) 

N=int(input("Enter the number"))
result=""
if N%3==0:
    result=result+"Fizz"
if N%5==0:
    result=result+"Buzz"
if N%3==0 and N%5==0:
    result=result
else:
    result=result+str(N)
print(result)

