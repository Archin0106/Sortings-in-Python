# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

input_values=input("Enter numbers: ")

arr = []
for num in input_values.split():
    arr.append(int(num))

print("Unsorted array: ",arr)

selection_sort(arr)

print("Sorted array: ",arr)