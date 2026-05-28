# 📘 Assignment: Searching & Sorting Fundamentals

## 🎯 Objective

Introduce students to fundamental search and sort algorithms, their implementations in Python, and how to compare their performance on small inputs.

## 📝 Tasks

### 🛠️ Implement Search Algorithms

#### Description
Write Python implementations for linear search and binary search (binary search assumes the input list is sorted). Each function should return the index of the found item or -1 if not found.

#### Requirements
Completed program should:

- Implement `linear_search(arr, target)` that checks each element and counts steps.
- Implement `binary_search(arr, target)` using an iterative or recursive approach and count steps.
- Include example calls and brief comments showing when each algorithm is appropriate.

### 🛠️ Implement Sort Algorithms and Compare

#### Description
Implement bubble sort and insertion sort. Add a simple harness that measures the number of elementary operations (comparisons and swaps) for each algorithm on the same input, and prints a comparison table.

#### Requirements
Completed program should:

- Implement `bubble_sort(arr)` and `insertion_sort(arr)` and return a tuple `(sorted_list, step_count)`.
- Provide a `compare_algorithms(samples)` helper that runs each algorithm on the same input and prints step counts.
- Include at least two example inputs (small random and reversed) and the resulting printed comparison.

### Extension (optional)

- Visualize step counts as simple ASCII bars (e.g., `bubble: #### (24)`).
- Try binary search on a sorted list and discuss why it is faster than linear search for large inputs.

---

Follow the repository assignment conventions and use `starter-code.py` as the starter file for students.
