# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        temp = key
        
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

input_values=input("Enter numbers: ")

arr = []
for num in input_values.split():
    arr.append(int(num))

print("Unsorted array: ",arr)

insertion_sort(arr)

print("Sorted array: ",arr)