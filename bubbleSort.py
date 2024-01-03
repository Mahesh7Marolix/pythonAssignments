def bubble_sort(list_1):
    for i in range(len(list_1)):
        for j in range(len(list_1)-1-i):
            if list_1[j]>list_1[j+1]:
                tempo=list_1[j]
                list_1[j]=list_1[j+1]
                list_1[j+1]=tempo
    print(list_1)

list_1=[2,43,5,7,3]
bubble_sort(list_1)

