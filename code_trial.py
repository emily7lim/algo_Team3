import random
import time

# Function to perform the Insertion Sort
def insertion_sort(arr, left, right):
    key_comparisons = 0
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            key_comparisons += 1

        arr[j + 1] = key

    return key_comparisons

# Function to merge two sorted subarrays
def merge(arr, left, mid, right):
    key_comparisons = 0
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
        key_comparisons += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return key_comparisons

# Function to perform hybrid Mergesort
def hybrid_mergesort(arr, left, right, threshold):
    key_comparisons = 0
    if left < right:
        if right - left + 1 <= threshold:
            key_comparisons += insertion_sort(arr, left, right)
        else:
            mid = left + (right - left) // 2

            key_comparisons += hybrid_mergesort(arr, left, mid, threshold)
            key_comparisons += hybrid_mergesort(arr, mid + 1, right, threshold)

            key_comparisons += merge(arr, left, mid, right)

    return key_comparisons

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    threshold = 124  # Set your threshold here

    print("Original array:", arr)

    key_comparisons = hybrid_mergesort(arr, 0, n - 1, threshold)

    print("Sorted array:", arr)

    for i in range(1000,10000000,100000):
        arr = [random.randint(1, i * 10) for _ in range(i)]

        start_time = time.time()
        key_comparisons = hybrid_mergesort(arr, 0, i - 1, threshold)
        end_time = time.time()

        cpu_time_used = end_time - start_time
        print(f"Size: {i}, Key Comparisons: {key_comparisons}, Time: {cpu_time_used} seconds")
