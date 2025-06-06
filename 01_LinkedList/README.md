# <p align="center">Understanding Linked Lists</p>

<p align="center"><i>A beginner-friendly guide to how Linked Lists work and how fast (or slow) they are.</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/Data%20Structure-Linked%20List-0f0f0f?style=for-the-badge" />
</p>

---

## What is a Linked List?
A **Linked List** is a data structure where elements (called nodes) are connected using pointers.
Each node contains:
- A **value**
- A **pointer** to the next node in the list

Unlike arrays (lists), the data is not stored in one block of memory.

---

## Big O of Common Operations

| Operation                            | Time Complexity | Explanation |
|-------------------------------------|------------------|-------------|
| Add to the end                      | O(1)* or O(n)    | Fast if tail is tracked, else we must traverse to the end |
| Remove from the end                 | O(n)             | Need to go through all nodes to reach the one before last |
| Add to the head                     | O(1)             | Just point the new node to the old head |
| Remove from the head                | O(1)             | Just move head to the next node |
| Insert in the middle                | O(n)             | Need to find the exact position first |
| Delete from the middle              | O(n)             | Again, must find the node before it |
| Lookup by index or value            | O(n)             | No direct access like arrays |

> 💡 *O(1) add-to-end is only true when the tail reference is maintained.*

---

## Linked List vs List (Array)

| Operation                | Linked List | Python List (Array) |
|--------------------------|-------------|----------------------|
| Access by Index         | O(n)        | O(1)                 |
| Add at End              | O(1)*       | O(1) Amortized       |
| Add at Start            | O(1)        | O(n)                 |
| Insert in Middle        | O(n)        | O(n)                 |
| Delete at Start         | O(1)        | O(n)                 |
| Delete at End           | O(n)        | O(1)                 |
| Delete in Middle        | O(n)        | O(n)                 |
| Search by Value         | O(n)        | O(n)                 |

---

## When to Use Linked Lists?
- You need fast insertions/deletions at the start
- You don’t need fast access by index
- You’re dealing with large datasets where memory reallocation is expensive
