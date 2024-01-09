a="String slicing in python"
print(a[:])#if  start and end index are not given it takes start index as 0 and end index as length of the string
print(a[:7])#if no start index is given it takes start index as 0 
print(a[7:])#if no end index is given it takes start index as length of  the given string
print(a[:15:2])#here 2 is given so it jumps,and slices only if  the diff btw indexes equals to 2
print(a[::-1])#here it goes in negative direction and prints the reverse of the string
print(a[:-1])