
# DAY 4 — LISTS (Data Structures I)

## 1. What is a List? (Foundation)

### Definition

A **list** is a container that stores **multiple values in order**.

Example:

```python
data = [10, 20, 30, 40, 50]
```

### Key properties of a list

* Ordered (position matters)
* Indexed (starts from index `0`)
* Mutable (can be changed)

---

## 2. Mutability & Memory (Very Important Concept)

### What does *mutable* mean?

**Mutable** means:

> You can change the object **after it is created**.

Example:

```python
a = [1, 2, 3]
a[0] = 99
print(a)
```

Output:

```
[99, 2, 3]
```

The list itself changed — this is mutability.

---

## 3. The Aliasing / Reference Trap (Critical Beginner Trap)

### The mistake

```python
a = [1, 2, 3]
b = a
```

You might think:

> “b is a copy of a”

 **Wrong**

### What actually happens

* `a` and `b` point to the **same memory location**
* Changing one changes the other

### Proof

```python
a = [1, 2, 3]
b = a
b[0] = 99

print(a)
```

Output:

```
[99, 2, 3]
```

### Why?

You copied the **reference**, not the data.

---

## 4. The Fix: Proper Copying

### Correct way

```python
b = a.copy()
```

OR

```python
b = a[:]
```

### Now this works safely

```python
a = [1, 2, 3]
b = a.copy()

b[0] = 99
print(a)
print(b)
```

Output:

```
[1, 2, 3]
[99, 2, 3]
```

---

# DEEP DIVE — MICRO-CHALLENGES

---

## 5. The Slicing Surgeon (List Slicing)

### Goal

Create a new list containing:

* The **last 3 items**
* In **reverse order**

Original:

```python
data = [10, 20, 30, 40, 50]
```

Expected:

```
[50, 40, 30]
```

---

### Slicing Syntax

```python
list[start : stop : step]
```

### Solution

```python
result = data[-1:-4:-1]
```

OR

```python
result = data[: -4 : -1]
```

### Explanation

| Part | Meaning              |
| ---- | -------------------- |
| `-1` | Start from last item |
| `-4` | Stop before index -4 |
| `-1` | Move backward        |

---

### Key Concept: Shallow Copy

Slicing creates a **new list object**.

```python
new_list = data[:]
```

* Original list remains unchanged
* New memory is allocated

---

## 6. The Stack Emulator (append + pop)

### What is a Stack?

A **Stack** follows:

> **LIFO — Last In, First Out**

Example:

* Push 1
* Push 2
* Push 3
* Pop → 3 comes out

---

### Python Implementation

```python
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

last = stack.pop()
print(last)
```

Output:

```
3
```

---

### Why use append & pop?

* Both are **O(1)** → very fast
* Python lists are **dynamic arrays**

### Why not `insert(0, x)`?

* That is **O(n)** → slow
* Python must shift all elements in memory

---

## 7. Time Complexity (Beginner Version)

| Operation      | Speed  |
| -------------- | ------ |
| `append()`     | Fast   |
| `pop()`        | Fast   |
| `insert(0, x)` | Slow   |
| `remove(x)`    | Slower |

---

## 8. The One-Line Architect (List Comprehension)

### Goal

* Numbers from 1 to 10
* Only **even numbers**
* Square them
* Do it in **one line**

---

### Normal (Long Way)

```python
result = []
for i in range(1, 11):
    if i % 2 == 0:
        result.append(i*i)
```

---

### One-Line Version (List Comprehension)

```python
result = [x**2 for x in range(1, 11) if x % 2 == 0]
```

### Output

```
[4, 16, 36, 64, 100]
```

---

### General Pattern

```python
[expression for item in iterable if condition]
```

---

### Why list comprehension is better

* Cleaner
* Faster
* Used everywhere in:

  * Data Science
  * Machine Learning
  * Python interviews

---

## 9. Combined Code (From Your Slide)

```python
data = [10, 20, 30, 40, 50]

# slicing
subset = data[1:4]       # [20, 30, 40]
reverse = data[::-1]     # [50, 40, 30, 20, 10]

# list comprehension
squares = [x**2 for x in data]
```

---

## 10. Final Mental Model (Very Important)

### Think like this:

* Variables store **references**
* Lists live in **memory**
* Assignment copies **address**
* Slicing / `.copy()` copies **data**
* Loops & comprehensions **build new lists**
* `append + pop` = Stack
* Slicing = Safe extraction

---

## 11. One-Page Summary

| Concept            | Meaning                    |
| ------------------ | -------------------------- |
| List               | Ordered, mutable container |
| Mutability         | Can change after creation  |
| Reference          | Memory address             |
| Copy               | New memory allocation      |
| Slicing            | Extract parts safely       |
| Stack              | LIFO behavior              |
| append/pop         | Fast stack operations      |
| List comprehension | Compact loop               |


