# BUBBLE SORT:
# Time Complexity: O(n^2) in the average and worst case, O(n) in the best case (when the array is already sorted)

# METHOD: SWAPPING ADJACENT ELEMENTS


def bubble_sort(arr: list) -> list: 
    for _ in range(len(arr) - 1):
        for j in range(1, len(arr)):
            if arr[j] <= arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                pass
    return arr
      

if __name__ == "__main__":
    print("Enter the list of numbers: ", end="")
    # User Input
    arr = list(map(lambda x: float(x), list(input().strip())))
    # Static Input
    # arr = [6, 5, 78, 3, -1, 53, 7, 0, 100, -56]
    output = bubble_sort(arr)
    print(output)
