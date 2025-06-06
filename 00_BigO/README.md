# Big O Notation Explained Simply

*Understanding how algorithms perform as data grows.*

---

## 1. O(n) – Linear Time
An operation that goes through each item once.

```python
for item in items:
    process(item)
```

As the number of items increases, the time taken increases proportionally.

---

## 2. Dropping Constants
In Big O, we ignore constant factors.

```python
for item in items:
    process(item)
for item in items:
    process_again(item)
```

Even though there are two loops, each running n times, we simplify O(2n) to O(n).

---

## 3. Nested Loops – O(n²)
When loops are inside loops, time increases rapidly.

```python
for item1 in items:
    for item2 in items:
        process(item1, item2)
```

Here, for each item, we process all items again, leading to O(n²) time.

---

## 4. Dropping Non-Dominant Terms
In expressions like O(n² + n), as n grows, n² dominates.

So, we simplify O(n² + n) to O(n²).

---

## 5. O(1) – Constant Time
Operations that take the same time, regardless of input size.

```python
def get_first_item(items):
    return items[0]
```

Accessing the first item doesn't depend on the number of items.

---

## 6. O(log n) – Logarithmic Time
Efficient algorithms that reduce the problem size each step.

```python
def binary_search(sorted_items, target):
    # Repeatedly divide the list in half to find the target
```

Each step cuts the data size in half, leading to O(log n) time.

---

## 7. O(n log n) – Linearithmic Time
Common in efficient sorting algorithms.

**Examples:**
- Merge Sort
- Quick Sort (average case)

These algorithms divide data and then process each part, resulting in O(n log n) time.

---

## 8. O(a + b) – Multiple Inputs
When dealing with two separate inputs.

```python
for item in list_a:
    process(item)
for item in list_b:
    process(item)
```

If list_a has 'a' items and list_b has 'b' items, the time is O(a + b).

---

## 9. Big O of Lists (Arrays)
Common operations and their time complexities:

- Access by index: O(1)
- Insert/Delete at end: O(1)
- Insert/Delete at beginning or middle: O(n)
- Search (unsorted): O(n)
- Search (sorted): O(log n) with binary search

---

For a comprehensive reference, visit the [Big O Cheat Sheet](https://www.bigocheatsheet.com/).
