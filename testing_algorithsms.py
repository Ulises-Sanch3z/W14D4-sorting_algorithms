import unittest
import sorting_algorithms as sa

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        print("Starting Bubble Sort tests")
        cases = [
            ("Small Random List", [3, 1, 2]),
            ("Medium Random List", [3, 1, 2, 4, 5]),
            ("Large Random List", [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]),
            ("Small Sorted List", [1, 2, 3]),
            ("Medium Sorted List", [1, 2, 3, 4, 5]),
            ("Large Sorted List", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ("Small Reverse List", [3, 2, 1]),
            ("Medium Reverse List", [5, 4, 3, 2, 1]),
            ("Large Reverse List", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        ]

        for case_name, arr in cases:
            print(f"Testing Bubble Sort with {case_name}...")
            sorted_list, comparisons, swaps, time_taken = sa.timer(sa.bubble_sort, arr)
            print(f"Sorted List: {sorted_list}")
            print(f"Comparisons: {comparisons}")
            print(f"Swaps: {swaps}")
            print(f"Time taken: {time_taken} seconds")
            self.assertTrue(isinstance(sorted_list, list), "sorted_list is not a list")
            self.assertTrue(isinstance(comparisons, int), "comparisons is not an int")
            self.assertTrue(isinstance(swaps, int), "swaps is not an int")
            self.assertTrue(isinstance(time_taken, float), "time_taken is not a float")
            self.assertEqual(sorted_list, sorted(arr), f"Bubble Sort failed on {case_name}")
            print(f"Bubble Sort passed on {case_name}\n")

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        print("Starting Selection Sort tests")
        cases = [
            ("Small Random List", [3, 1, 2]),
            ("Medium Random List", [3, 1, 2, 4, 5]),
            ("Large Random List", [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]),
            ("Small Sorted List", [1, 2, 3]),
            ("Medium Sorted List", [1, 2, 3, 4, 5]),
            ("Large Sorted List", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ("Small Reverse List", [3, 2, 1]),
            ("Medium Reverse List", [5, 4, 3, 2, 1]),
            ("Large Reverse List", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        ]

        for case_name, arr in cases:
            print(f"Testing Selection Sort with {case_name}...")
            sorted_list, comparisons, swaps, time_taken = sa.timer(sa.selection_sort, arr)
            print(f"Sorted List: {sorted_list}")
            print(f"Comparisons: {comparisons}")
            print(f"Swaps: {swaps}")
            print(f"Time taken: {time_taken} seconds")
            self.assertTrue(isinstance(sorted_list, list), "sorted_list is not a list")
            self.assertTrue(isinstance(comparisons, int), "comparisons is not an int")
            self.assertTrue(isinstance(swaps, int), "swaps is not an int")
            self.assertTrue(isinstance(time_taken, float), "time_taken is not a float")
            self.assertEqual(sorted_list, sorted(arr), f"Selection Sort failed on {case_name}")
            print(f"Selection Sort passed on {case_name}\n")

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        print("Starting Insertion Sort tests")
        cases = [
            ("Small Random List", [3, 1, 2]),
            ("Medium Random List", [3, 1, 2, 4, 5]),
            ("Large Random List", [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]),
            ("Small Sorted List", [1, 2, 3]),
            ("Medium Sorted List", [1, 2, 3, 4, 5]),
            ("Large Sorted List", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ("Small Reverse List", [3, 2, 1]),
            ("Medium Reverse List", [5, 4, 3, 2, 1]),
            ("Large Reverse List", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        ]

        for case_name, arr in cases:
            print(f"Testing Insertion Sort with {case_name}...")
            sorted_list, comparisons, swaps, time_taken = sa.timer(sa.insertion_sort, arr)
            print(f"Sorted List: {sorted_list}")
            print(f"Comparisons: {comparisons}")
            print(f"Swaps: {swaps}")
            print(f"Time taken: {time_taken} seconds")
            self.assertTrue(isinstance(sorted_list, list), "sorted_list is not a list")
            self.assertTrue(isinstance(comparisons, int), "comparisons is not an int")
            self.assertTrue(isinstance(swaps, int), "swaps is not an int")
            self.assertTrue(isinstance(time_taken, float), "time_taken is not a float")
            self.assertEqual(sorted_list, sorted(arr), f"Insertion Sort failed on {case_name}")
            print(f"Insertion Sort passed on {case_name}\n")

if __name__ == "__main__":
    unittest.main()
