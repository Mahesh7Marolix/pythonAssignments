list_a=[2,7,4,8,9,6,0]
sorted_list=[list_a[0]]
for i in range(1,len(list_a)):
    sorted_list.append(list_a[i])
    for j in range(i):
        if sorted_list[i-j]<sorted_list[i-j-1]:
            tempo= sorted_list[i-j]
            sorted_list[i-j]=sorted_list[i-j-1]
            sorted_list[i-j-1]=tempo
print(sorted_list)
    