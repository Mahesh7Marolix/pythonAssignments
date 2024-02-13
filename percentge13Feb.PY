N=int(input("Enter the number of students in class "))
PercantageList={}
i=1
while i<=N:
    name=input("Enter the name of student ")
    percentage=int(input("Enter the percentage scored by "+str(name)+" "))
    PercantageList[name]=percentage
    i+=1
for i in PercantageList.keys():
    print(i,"secured",str(PercantageList[i])+"%")

