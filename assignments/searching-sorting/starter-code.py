import random
from typing import List, Tuple


def linear_search(arr: List[int], target: int) -> Tuple[int, int]:
    """Return (index, steps) where steps counts comparisons."""
    steps = 0
    for i, v in enumerate(arr):
        steps += 1
        if v == target:
            return i, steps
    return -1, steps


def binary_search(arr: List[int], target: int) -> Tuple[int, int]:
    """Assumes `arr` is sorted. Returns (index, steps)."""
    lo, hi = 0, len(arr) - 1
    steps = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        steps += 1
        if arr[mid] == target:
            return mid, steps
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, steps


def bubble_sort(arr: List[int]) -> Tuple[List[int], int]:
    a = arr.copy()
    n = len(a)
    steps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                steps += 1  # count swap as extra step
    return a, steps


def insertion_sort(arr: List[int]) -> Tuple[List[int], int]:
    a = arr.copy()
    steps = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            steps += 1
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        steps += 1
    return a, steps


def compare_algorithms(samples: List[int]) -> None:
    print("Input:", samples)
    b_sorted, b_steps = bubble_sort(samples)
    i_sorted, i_steps = insertion_sort(samples)
    print(f"bubble_sort: steps={b_steps}")
    print(f"insertion_sort: steps={i_steps}")
    print("Results equal:", b_sorted == i_sorted)


def demo():
    small = [5, 1, 4, 2, 8]
    rev = list(range(10, 0, -1))

    print("--- Small list ---")
    compare_algorithms(small)

    print("--- Reversed list ---")
    compare_algorithms(rev)

    # Search demo
    arr = sorted(random.sample(range(1, 21), 10))
    target = arr[len(arr) // 2]
    print("\nSearch demo on sorted array:", arr)
    idx_l, steps_l = linear_search(arr, target)
    idx_b, steps_b = binary_search(arr, target)
    print(f"linear_search: index={idx_l}, steps={steps_l}")
    print(f"binary_search: index={idx_b}, steps={steps_b}")


if __name__ == "__main__":
    demo()
