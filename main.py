def bubble_sort(arr):
    n = len(arr)
    swapped = False

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            return arr


list_of_elements = [4, 6, 3, 10, 141, 350, 1, 15, -5, 0]
bubble_sort(list_of_elements)
print(f"Sorted array: {list_of_elements}")

