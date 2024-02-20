def factorial(num):
    if num!=0:
        fact=num
        for i in range(1,N):
            fact=fact*(num-i)
        return fact
    else:
        return 1
def EvenOrOdd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"


def square(num):
    return num*num
def addition(num1,num2):
    return num1+num2
def substraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1//num2

N=int(input("Enter the number for factorial square and check weather it is even or odd "))
N1=int(input("Enter the number for add,sub,mul and div"))
N2=int(input("Enter the number for add,sub,mul and div"))
print(EvenOrOdd(N))
print(square(N))
print(factorial(N))
print(addition(N1,N2))
print(substraction(N1,N2))
print(multiplication(N1,N2))
print(division(N1,N2))
