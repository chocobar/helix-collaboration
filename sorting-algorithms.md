# A Guide to Sorting Algorithms

Sorting is one of the most fundamental operations in computer science. Whether you're organizing a list of names, ranking search results, or preparing data for binary search, sorting is everywhere. Understanding how different sorting algorithms work — and when to use each one — is essential knowledge for any programmer.

In this post, we'll walk through six common comparison-based sorting algorithms. We'll start with three simpler O(n^2) algorithms, then move on to three efficient O(n log n) algorithms. For each one, you'll get a plain-English explanation, a Python implementation, and a complexity breakdown.

Let's dive in.

---

## Bubble Sort

Bubble Sort is the simplest sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order. Larger elements "bubble up" to the end of the list with each pass.

The algorithm makes multiple passes through the array. On each pass, it compares each pair of adjacent elements and swaps them if the left one is greater than the right one. After the first pass, the largest element is guaranteed to be at the end. After the second pass, the second-largest is in place, and so on.

An optimization is to track whether any swaps occurred during a pass. If no swaps happened, the array is already sorted, and we can stop early. This gives Bubble Sort its best-case O(n) time on already-sorted input.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

| Case    | Time Complexity | Space Complexity |
|---------|-----------------|------------------|
| Best    | O(n)            | O(1)             |
| Average | O(n^2)          | O(1)             |
| Worst   | O(n^2)          | O(1)             |

---

## Selection Sort

Selection Sort works by dividing the array into a sorted portion and an unsorted portion. It repeatedly finds the minimum element from the unsorted portion and moves it to the end of the sorted portion.

On each iteration, the algorithm scans the unsorted section to find the smallest element, then swaps it with the first unsorted element. The boundary between sorted and unsorted shifts one position to the right after each iteration.

Selection Sort always makes O(n^2) comparisons regardless of the input, so it has no best-case advantage over its average case. However, it makes at most O(n) swaps, which can be useful when write operations are expensive.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

| Case    | Time Complexity | Space Complexity |
|---------|-----------------|------------------|
| Best    | O(n^2)          | O(1)             |
| Average | O(n^2)          | O(1)             |
| Worst   | O(n^2)          | O(1)             |

---

## Insertion Sort

Insertion Sort builds the sorted array one element at a time. It takes each element and inserts it into its correct position within the already-sorted portion of the array, much like how you might sort a hand of playing cards.

The algorithm iterates from left to right. For each element, it compares it with the elements to its left, shifting them one position to the right until it finds the correct spot. Then it inserts the element there.

Insertion Sort is efficient on small arrays and nearly-sorted data. Its best case is O(n) when the array is already sorted, because each element only needs one comparison. Many real-world sorting implementations use Insertion Sort as a subroutine for small partitions (e.g., Python's Timsort and Java's Arrays.sort).

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

| Case    | Time Complexity | Space Complexity |
|---------|-----------------|------------------|
| Best    | O(n)            | O(1)             |
| Average | O(n^2)          | O(1)             |
| Worst   | O(n^2)          | O(1)             |

---

## Merge Sort

Merge Sort is a divide-and-conquer algorithm. It splits the array in half, recursively sorts each half, and then merges the two sorted halves back together.

The key insight is that merging two sorted arrays into one sorted array is an O(n) operation. By recursively dividing the problem, we get O(log n) levels of recursion, each doing O(n) work — giving us O(n log n) total time.

Merge Sort guarantees O(n log n) performance in all cases, which makes it predictable and reliable. The tradeoff is that it requires O(n) extra space for the temporary arrays used during merging. It's also a stable sort, meaning equal elements maintain their relative order.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

| Case    | Time Complexity | Space Complexity |
|---------|-----------------|------------------|
| Best    | O(n log n)      | O(n)             |
| Average | O(n log n)      | O(n)             |
| Worst   | O(n log n)      | O(n)             |

---

## Quick Sort

Quick Sort is another divide-and-conquer algorithm. It picks a "pivot" element, partitions the array so that everything less than the pivot is on the left and everything greater is on the right, and then recursively sorts the two partitions.

The partitioning step is where the real work happens. We walk through the array, moving elements smaller than the pivot to the left side. After partitioning, the pivot is in its final sorted position. We then recursively apply the same process to the left and right sub-arrays.

Quick Sort's average case is O(n log n), and it's typically faster in practice than Merge Sort due to better cache performance and lower constant factors. However, its worst case is O(n^2), which occurs when the pivot is consistently the smallest or largest element (e.g., an already-sorted array with a naive pivot choice). Good pivot selection strategies — like choosing the median of three elements — mitigate this.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
```

| Case    | Time Complexity | Space Complexity |
|---------|-----------------|------------------|
| Best    | O(n log n)      | O(log n)         |
| Average | O(n log n)      | O(log n)         |
| Worst   | O(n^2)          | O(n)             |

---

## Heap Sort

Heap Sort uses a binary heap data structure to sort elements. It first builds a max-heap from the array, then repeatedly extracts the maximum element and places it at the end of the sorted portion.

A max-heap is a complete binary tree where each parent node is greater than or equal to its children. Building one from an unsorted array takes O(n) time. Once the heap is built, we swap the root (the maximum) with the last element, reduce the heap size by one, and restore the heap property. We repeat this until the heap is empty.

Heap Sort guarantees O(n log n) time in all cases and sorts in-place with O(1) extra space. However, it's not stable, and its constant factors are typically larger than Quick Sort's due to poor cache locality — the heap's tree structure means we jump around in memory rather than accessing elements sequentially.

```python
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

| Case    | Time Complexity | Space Complexity |
|---------|-----------------|------------------|
| Best    | O(n log n)      | O(1)             |
| Average | O(n log n)      | O(1)             |
| Worst   | O(n log n)      | O(1)             |

---

## Comparison Table

| Algorithm      | Best        | Average     | Worst       | Space    | Stable | In-Place |
|----------------|-------------|-------------|-------------|----------|--------|----------|
| Bubble Sort    | O(n)        | O(n^2)      | O(n^2)      | O(1)     | Yes    | Yes      |
| Selection Sort | O(n^2)      | O(n^2)      | O(n^2)      | O(1)     | No     | Yes      |
| Insertion Sort | O(n)        | O(n^2)      | O(n^2)      | O(1)     | Yes    | Yes      |
| Merge Sort     | O(n log n)  | O(n log n)  | O(n log n)  | O(n)     | Yes    | No       |
| Quick Sort     | O(n log n)  | O(n log n)  | O(n^2)      | O(log n) | No     | Yes      |
| Heap Sort      | O(n log n)  | O(n log n)  | O(n log n)  | O(1)     | No     | Yes      |

---

## Conclusion: Choosing the Right Algorithm

There's no single "best" sorting algorithm — the right choice depends on your situation:

- **Small arrays (< ~50 elements):** Use **Insertion Sort**. Its low overhead and good cache performance make it faster than the O(n log n) algorithms on small inputs.
- **Nearly sorted data:** Use **Insertion Sort**. It runs in nearly O(n) time when the data is almost in order.
- **Guaranteed O(n log n) with stability:** Use **Merge Sort**. It's predictable and preserves the relative order of equal elements, which matters when sorting by multiple keys.
- **General-purpose, fast in practice:** Use **Quick Sort**. With a good pivot strategy, it's the fastest comparison-based sort on average due to cache-friendly access patterns.
- **Guaranteed O(n log n) with O(1) space:** Use **Heap Sort**. It's the go-to when you need worst-case guarantees without extra memory.
- **Learning or teaching:** Start with **Bubble Sort** — it's the easiest to understand and reason about, even if you'd never use it in production.

In practice, most standard library sort functions use hybrid algorithms. Python's built-in `sorted()` uses Timsort, which combines Merge Sort and Insertion Sort. Java's `Arrays.sort()` uses a dual-pivot Quick Sort for primitives and Timsort for objects. These hybrids pick the best strategy based on the data, giving you the best of multiple worlds.

Understanding these fundamental algorithms gives you the foundation to appreciate those hybrid approaches — and to make informed choices when performance matters.
