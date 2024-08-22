# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):

#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
           
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

input_values=input("Enter numbers: ")

arr = []
for num in input_values.split():
    arr.append(int(num))

print("Unsorted array: ",arr)

bubble_sort(arr)

print("Sorted array: ",arr)