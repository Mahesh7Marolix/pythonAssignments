def selection_sort(arr):
    for i in range(len(arr)-1):
        minim=arr[i]
    
        for j in range(i+1,len(arr)):
            if minim>arr[j]:
                temp=arr[j]
                arr[j]=minim
                minim=temp
                arr[i]=temp
    print(arr) 
selection_sort([4,7,3,1,8])
            
        