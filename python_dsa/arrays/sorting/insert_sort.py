# INSERTION SORT:
# Time Complexity: O(n^2) in the average and worst case, O(n) in the best case (when the array is already sorted)

# METHOD: BUILDING THE SORTED ARRAY ONE ELEMENT AT A TIME
# NOTE: Insertion sort is more suited for linked lists than arrays due to the nature of insertions and deletions.
# In arrays, shifting elements can be costly, whereas linked lists allow for efficient insertions and deletions.


def insert_sort(arr: list) -> list:
    # inserting 1st index:
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            



if __name__ == "__main__":
    print("Enter the list of numbers: ", end="")
    # User Input
    arr = list(map(lambda x: float(x), list(input().strip())))
    # Static Input
    # arr = [6, 5, 78, 3, -1, 53, 7, 0, 100, -56]
    output = insert_sort(arr)
    print(output)
