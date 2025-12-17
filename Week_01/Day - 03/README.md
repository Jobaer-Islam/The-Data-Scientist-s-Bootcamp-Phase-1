

# Day 3 – Loops & Iteration (Python)

## 1. What is a Loop?


A **loop** is a programming structure that allows you to **repeat a block of code automatically** instead of writing it again and again.

### Why loops are needed

Without loops:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

With loops:

```python
for i in range(4):
    print("Hello")
```

---

## 2. Types of Loops in Python

Python mainly uses **two loops**:

| Loop Type    | When to Use                                                                  |
| ------------ | ---------------------------------------------------------------------------- |
| `for` loop   | When you know **what to loop over** (list, string, range)                    |
| `while` loop | When you don’t know how many times — run **until a condition becomes False** |

---

## 3. FOR Loop (Iterator Protocol – Beginner View)

### Definition

A **for loop** goes through items **one by one** from a collection.

### Common collections

* List
* String
* Range

### Example 1: Loop over numbers

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

### Example 2: Loop over a string

```python
for ch in "DATA":
    print(ch)
```

Output:

```
D
A
T
A
```

---

## 4. WHILE Loop (Condition-Based Loop)

### Definition

A **while loop** keeps running **as long as a condition is True**.

### Structure

```python
while condition:
    code
```

### Example

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

## 5. ⚠ Infinite Loop (Important Warning)

### What is an Infinite Loop?

A loop that **never stops** because the condition never becomes False.

### Example (Dangerous)

```python
while True:
    print("Running forever")
```

This runs forever **unless you stop it manually**.

---

# DEEP DIVE – Micro-Challenges Explained

---

## 6. The Infinite Guardian (Password Checker)

### Goal

Ask the user for a password **repeatedly** until:

* Password length ≥ 6 → accept
* Otherwise → ask again

### Key Concepts Used

* `while True` → infinite loop
* `break` → exit loop safely

### Code

```python
while True:
    pwd = input("Set password (min 6 chars): ")

    if len(pwd) >= 6:
        print("Password set")
        break   # exits the loop
    else:
        print("Too short. Try again.")
```

### How it works (Step-by-Step)

1. `while True` → loop starts and never stops by itself
2. User enters password
3. `len(pwd)` checks length
4. If valid → `break` stops loop
5. If invalid → loop repeats

---

## 7. The Accumulator Pattern (Very Important Concept)

### Definition

An **accumulator** is a variable that **stores and updates a running total** inside a loop.

---

### Goal

Ask user for `N`
Calculate sum from `1` to `N`

Example:

```
N = 5
1 + 2 + 3 + 4 + 5 = 15
```

---

### Rules

* ❌ Do NOT use formula `n(n+1)/2`
* ✅ Use a loop and a variable

---

### Code

```python
n = int(input("Enter a number: "))
total = 0   # accumulator

for i in range(1, n + 1):
    total += i

print("Sum =", total)
```

---

### How it works internally

| Iteration | i | total |
| --------- | - | ----- |
| Start     | – | 0     |
| 1         | 1 | 1     |
| 2         | 2 | 3     |
| 3         | 3 | 6     |
| 4         | 4 | 10    |
| 5         | 5 | 15    |

---

## 8. The Efficient Skipper (`continue`)

### Definition

`continue` **skips the current iteration** and moves to the next one.

### Difference between `break` and `continue`

| Keyword    | Effect                             |
| ---------- | ---------------------------------- |
| `break`    | Stops the loop completely          |
| `continue` | Skips current step, continues loop |

---

### Goal

Print numbers from `1` to `10`, but **skip 5**

### Code

```python
for i in range(1, 11):
    if i == 5:
        continue   # skip 5
    print(i)
```

### Output

```
1
2
3
4
6
7
8
9
10
```

---

### Why this matters

Used heavily in:

* Filtering data
* Ignoring invalid values
* Skipping unwanted cases

---

## 9. The String Walker (Iterator Protocol)

### Definition

Strings are **iterable**, meaning Python can read them **character by character**.

---

### Goal

Print each letter of `"DATA"` on a new line

### Code

```python
word = "DATA"

for ch in word:
    print(ch)
```

---

### What Python does internally

1. Takes first character → `'D'`
2. Prints
3. Takes next → `'A'`
4. Continues until string ends

---

### Why this is important

This concept is used in:

* Text processing
* Password validation
* Parsing files
* NLP (Natural Language Processing)

---

## 10. Summary Table (Quick Revision)

| Concept          | Meaning                            |
| ---------------- | ---------------------------------- |
| Loop             | Repeat code automatically          |
| `for` loop       | Iterate over items                 |
| `while` loop     | Run until condition becomes False  |
| Infinite loop    | Loop without end                   |
| `break`          | Exit loop immediately              |
| `continue`       | Skip current iteration             |
| Accumulator      | Variable that stores running total |
| String iteration | Loop through characters            |

---
