import sys
import os
import time

sys.setrecursionlimit(10000)  # Increase the recursion limit to avoid RecursionError

# Sortieralgorithmen
def heapsort(arr):
    comparisons = [0]  # Use a list to pass by reference

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        comps = 0

        if left < n:
            comps += 1
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            comps += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            sub_comps = heapify(arr, n, largest)
            comps += sub_comps

        return comps

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        comparisons[0] += heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        comparisons[0] += heapify(arr, i, 0)

    return arr, comparisons[0]

def quicksort(arr):
    comparisons = [0]  # Use a list to pass by reference

    def _quicksort(arr, low, high):
        if low < high:
            pi, comps = partition(arr, low, high)
            comparisons[0] += comps
            _quicksort(arr, low, pi-1)
            _quicksort(arr, pi+1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        comps = 0
        for j in range(low, high):
            comps += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1, comps

    _quicksort(arr, 0, len(arr)-1)
    return arr, comparisons[0]

def timsort(arr):
    return sorted(arr), 0  # Python's built-in Timsort

def read_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return list(map(int, contents.split()))

def write_file(file_path, arr):
    with open(file_path, 'w') as file:
        for item in arr:
            file.write(f"{item}\n")

def write_file(file_path, arr):
    with open(file_path, 'w') as file:
        for item in arr:
            file.write(f"{item}\n")

def main():
    file_path = input("Enter the path to the file to be sorted: ")
    if not os.path.isfile(file_path):
        print("File not found.")
        return

    arr = read_file(file_path)
    print("Choose a sorting algorithm:")
    print("1. Heapsort")
    print("2. Quicksort")
    print("3. Timsort")

    choice = input("Enter the number of the sorting algorithm: ")
    start_time = time.time()
    if choice == '1':
        sorted_arr, comparisons = heapsort(arr)
    elif choice == '2':
        sorted_arr, comparisons = quicksort(arr)
    elif choice == '3':
        sorted_arr, comparisons = timsort(arr)
    else:
        print("Invalid choice.")
        return
    end_time = time.time()

    elapsed_time = end_time - start_time

    output_choice = input("\nDo you want to output the sorted array in the console?\nWARNING: Writing the file in console can take very long for large files!\n\nPlease type Y for Yes and N for No:\n").strip().lower()
    if output_choice == 'y':
        print("Sorted array:", sorted_arr)
    
    print("Number of comparisons:", comparisons)
    print(f"Time taken: {elapsed_time:.6f} seconds")

    save_choice = input("Do you want to save the sorted file? (Y/N): ").strip().lower()
    if save_choice == 'y':
        save_path = input("Enter the path to save the sorted file: ")
        write_file(save_path, sorted_arr)
        print(f"Sorted array saved to {save_path}")
    else:
        print("Sorted array not saved.")

if __name__ == "__main__":
    main()