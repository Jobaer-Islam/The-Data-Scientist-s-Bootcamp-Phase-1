
# DAY 5 — DICTIONARIES (HASH MAPS)

---

## 1. What is a Dictionary? 

### Definition

A **dictionary** is a data structure that stores data as **key–value pairs**.

Think of it like:

* A **real dictionary**:
  word → meaning
* A **phone contact list**:
  name → phone number

### Example

```python
user = {
    "id": 1,
    "name": "Admin"
}
```

Here:

* `"id"` → key
* `1` → value
* `"name"` → key
* `"Admin"` → value

---

## 2. Why Dictionaries Exist (Important)

### List problem

Searching a list is **slow** for large data.

```python
nums = [10, 20, 30, 40]
print(30 in nums)   # Python checks one by one
```

This is **O(N)** (slow).

---

### Dictionary advantage

Dictionary search is **O(1)** (very fast).

```python
user = {"id": 1}
print(user["id"])   # Direct memory access
```

Even with **1 million items**, lookup is fast.

---

## 3. Hash Table 

### What happens internally

1. Python takes the **key**
2. Runs a **hash function**
3. Finds the **exact memory address**
4. Reads value instantly

You don’t see this — Python handles it.

---

# MICRO-CHALLENGES EXPLAINED

---

## 4. The Safe Vault (`.get()`)

### Problem

Accessing a missing key **crashes the program**.

```python
user = {"id": 1}
print(user["email"])   #  KeyError
```

---

### Solution: `.get()`

### Definition

`.get()` safely retrieves a value.

* If key exists → return value
* If key missing → return `None` or default value

---

### Code

```python
user = {"id": 1}

email = user.get("email")
print(email)
```

Output:

```
None
```

---

### With default value

```python
email = user.get("email", "No Email Found")
print(email)
```

Output:

```
No Email Found
```

---

### When to use `.get()`

* User input
* API responses
* Database data
* Any uncertain data source

---

## 5. Dictionary Iteration

### Looping through dictionary

```python
user = {"id": 1, "name": "Admin"}

for key, value in user.items():
    print(key, ":", value)
```

Output:

```
id : 1
name : Admin
```

---

## 6. The Frequency Counter 

### Goal

Count how many times each letter appears in `"banana"`.

---

### Mental Model

* If character not seen before → start count at 1
* If already seen → increase count

---

### Code 
```python
word = "banana"
freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
```

Output:

```
{'b': 1, 'a': 3, 'n': 2}
```

---

### Why this is important

Used in:

* Text analysis
* NLP
* Interview questions
* Data science preprocessing

---

## 7. Dynamic Key Insertion (Concept)

### What happened above?

Python:

* Created keys **on the fly**
* Updated values dynamically
* Used hash table internally

You didn’t predefine keys — Python handled it.

---

## 8. The Database Merger (Merging Dictionaries)

### Goal

Merge two dictionaries:

* Defaults
* User preferences
* User preferences override defaults

---

### Data

```python
defaults = {"theme": "light", "audio": "on"}
user_pref = {"theme": "dark"}
```

---

### Method 1: `.update()`

```python
defaults.update(user_pref)
print(defaults)
```

Output:

```
{'theme': 'dark', 'audio': 'on'}
```

---

### Method 2: `|` operator (Python 3.9+)

```python
merged = defaults | user_pref
print(merged)
```

---

### Important Rule

If key exists in both:

* **Right dictionary wins**

---

## 9. Why Merge Works This Way

Python:

1. Iterates through second dictionary
2. Hashes each key
3. If key exists → overwrite
4. If missing → keep original

---

## 10. The Speed Trap (List vs Dict vs Set)

### Problem

Check if `-1` exists in:

* A list of 1 million numbers
* A set of same numbers

---

### List Search (Slow)

```python
nums = list(range(1000000))
print(-1 in nums)
```

* Python checks item by item
* **O(N)**

---

### Set Search (Fast)

```python
nums = set(range(1000000))
print(-1 in nums)
```

* Python hashes `-1`
* Goes to exact memory location
* **O(1)**

---

### Summary Table

| Structure  | Lookup Speed |
| ---------- | ------------ |
| List       | O(N)         |
| Dictionary | O(1)         |
| Set        | O(1)         |

---

## 11. When to Use What

| Use Case               | Structure  |
| ---------------------- | ---------- |
| Ordered data           | List       |
| Key-value data         | Dictionary |
| Fast existence check   | Set        |
| Counting frequency     | Dictionary |
| Configuration settings | Dictionary |

---

## 12. One-Page Summary (Beginner Friendly)

* Dictionary = key → value store
* Fast lookup using hashing
* `.get()` prevents crashes
* Keys are unique
* Values can be anything
* Frequency counter is a core pattern
* Dict/set search is faster than lists

* Data science use cases

Just say **next**.
