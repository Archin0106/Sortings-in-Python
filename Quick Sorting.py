def quick_sort(arr,start,end):
    if start<end:
        partition_index=partition(arr,start,end)
        quick_sort(arr,start,partition_index-1)
        quick_sort(arr,partition_index+1,end)
        
def partition(arr,start,end):
    temp=arr[end]
    i=start-1
    
    for j in range(start,end):
        if arr[j]<=temp:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1

input_values=input("Enter numbers: ")

arr = []
for num in input_values.split():
    arr.append(int(num))

print("Unsorted array: ",arr)
quick_sort(arr,0,len(arr)-1)
print("Sorted array: ",arr)