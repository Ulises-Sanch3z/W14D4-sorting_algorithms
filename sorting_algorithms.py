import time
import random

# Function to measure runtime 
def timer(algo, arr):
    start_time = time.time()
    result = algo(arr.copy())
    end_time = time.time()
    time_taken = end_time - start_time
    return result[0], result[1], result[2], time_taken

# Bubble Sort
def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comparisons, swaps

#Selection Sort
def selection_sort(arr):
    comparisons = 0
    swaps = 0
    current = 0
    while current < len(arr) - 1:
        min_index = current
        i = current + 1
        while i < len(arr):
            comparisons += 1
            if arr[i] < arr[min_index]:
                min_index = i
            i += 1

        if min_index != current:
            arr[current], arr[min_index] = arr[min_index], arr[current]
            swaps += 1
        current += 1
    return arr, comparisons, swaps

#Insertion Sort
def insertion_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        
        if j >= 0:
            comparisons += 1

        arr[j + 1] = key

    return arr, comparisons, swaps

def main():
    # arr = gen_list(10)
    # print(f"Randomly generated list: {arr}")
    # print("_________________________________________________________")
    # print("Testing Bubble Sort")
    # timer(bubble_sort, arr)
    # print("_________________________________________________________")
    # print("Testing Selection Sort")
    # timer(selection_sort, arr)
    # print("_________________________________________________________")
    # print("Testing Insertion Sort")
    # timer(insertion_sort, arr)
    ...

if __name__ == "__main__":
    main()