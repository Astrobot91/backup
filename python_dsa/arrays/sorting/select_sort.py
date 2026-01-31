# SELECTION SORT:
# Time Complexity: O(n^2) in the average and worst case, O(n^2) in the best case

# METHOD: SELECTING THE MINIMUM ELEMENT FROM THE UNSORTED PART


def select_sort(arr: list) -> list: 
    for i in range(len(arr) - 1):
        min_value = arr[i]
        min_index = 0
        for j in range(i, len(arr)):
            if min_value >= arr[j]:
                min_value = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
      

if __name__ == "__main__":
    print("Enter the list of numbers: ", end="")
    # User Input
    arr = list(map(lambda x: float(x), list(input().strip())))
    # Static Input
    # arr = [6, 5, 78, 3, -1, 53, 7, 0, 100, -56]
    output = select_sort(arr)
    print(output)
