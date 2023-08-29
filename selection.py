def selectionSort(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        loc=i
        for j in range(i+1,len(arr)):
            if arr[j]< min:
                min=arr[j]
                loc=j
        if loc != i:
            temp=arr[i]
            arr[i]=arr[loc]
            arr[loc]=temp
            
    return arr

print(selectionSort([9,1,6,2,90]))
        