

# DAY 6 — FUNCTIONS & MODULARITY

---

## 1. What is a Function? 

### Definition

A **function** is a reusable block of code that:

* Takes input (optional)
* Performs some work
* Returns output (optional)

Think of it like a **machine**:

```
Input → Process → Output
```

---

### Simple Example

```python
def greet():
    print("Hello")
```

Calling the function:

```python
greet()
```

Output:

```
Hello
```

---

## 2. The Pure Return (Print vs Return)

### Important Rule

* `print()` → shows something on the screen
* `return` → sends a value back to the caller

They are **NOT the same**.

---

###  Wrong Design (Pure Print, No Return)

```python
def add(a, b):
    print(a + b)

res = add(5, 5)
print(res)
```

### Output

```
10
None
```

---

### Why `None`?

* Every Python function **must return something**
* If you don’t write `return`, Python does:

```python
return None
```

So:

```python
res = None
```

---

###  Correct Design (Best Practice)

```python
def add(a, b):
    return a + b

res = add(5, 5)
print(res)
```

Output:

```
10
```

---

### Best Practice Rule

> **Functions should calculate and return values.
> Printing should be done outside the function.**

This is critical for:

* Testing
* Reusability
* Data science pipelines
* Production code

---

## 3. Default Arguments (The Default Gateway)

### Definition

A **default argument** is a value that is used **only if no argument is passed**.

---

### Example

```python
def connect(port=3306):
    print(f"Connecting to {port}")
```

---

### Calling the function

```python
connect()
connect(5432)
```

Output:

```
Connecting to 3306
Connecting to 5432
```

---

### What Python Does Internally

* Stores `3306` when function is defined
* If no argument → uses stored default
* If argument provided → overrides default

---

### Where This Is Used

* Database connections
* API configs
* Optional parameters
* Frameworks (Flask, Django, FastAPI)

---

## 4. The Logic Gate (One-Line Boolean Return)

### Goal

Return `True` if number is even, `False` otherwise
 No `if/else`
 One line only

---

### Beginner Mistake

```python
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
```

Correct but **unnecessary**.

---

### Correct & Clean Way

```python
def is_even(num):
    return num % 2 == 0
```

---

### Why This Works

* `num % 2 == 0` already evaluates to `True` or `False`
* Python comparisons **return booleans**

---

### Example

```python
print(is_even(4))  # True
print(is_even(7))  # False
```

---

## 5. What is Modularity?

### Definition

**Modularity** means:

> Breaking large programs into small, independent functions.

---

### Why Modularity Matters

* Easier to read
* Easier to test
* Easier to debug
* Easier to reuse

This is **mandatory** in:

* Data Science
* Backend systems
* AI pipelines
* Industry projects

---

## 6. Stack Scope (Very Important Concept)

### What Happens When a Function Is Called?

1. Python creates a **Stack Frame**
2. Local variables live inside it
3. Function finishes
4. Stack frame is destroyed

---

### Example

```python
def calculate_area(radius):
    area = 3.14 * radius * radius
    return area

print(calculate_area(5))
```

Here:

* `radius` and `area` exist **only inside the function**
* They disappear after return

---

## 7. LEGB Rule (Variable Lookup Order)

Python looks for variables in this order:

| Level | Meaning                         |
| ----- | ------------------------------- |
| L     | Local (inside function)         |
| E     | Enclosing (nested functions)    |
| G     | Global                          |
| B     | Built-in (`print`, `len`, etc.) |

---

## 8. Type Hints & Docstrings (Professional Practice)

```python
def calculate_area(radius: float) -> float:
    """Returns area of a circle."""
    if radius < 0:
        return 0
    return 3.14 * radius * radius
```

### Why use this?

* Improves readability
* Helps IDEs
* Used in production code
* Required in many teams

---

## 9. The Scope Fortress (Local vs Global Scope)

### Problem

```python
x = 10

def change_x():
    x = 20

change_x()
print(x)
```

### Output

```
10
```

---

### Why?

* `x = 20` creates a **new local variable**
* Global `x` remains untouched

---

### Visual Explanation

```
Global x = 10

Function Stack Frame:
    local x = 20   (temporary)
```

After function ends → local `x` disappears

---

### Can We Change Global x?

Yes, but **DON’T in production**.

```python
def change_x():
    global x
    x = 20
```

Avoid this — it causes bugs and confusion.

---

## 10. Best Practices

 Functions should:

* Take inputs
* Return outputs
* Avoid printing
* Avoid global variables

 Avoid:

* Modifying globals
* Mixing logic + printing
* Hidden side effects

---

## 11. One-Page Summary

| Concept        | Meaning                 |
| -------------- | ----------------------- |
| Function       | Reusable block of logic |
| return         | Sends value back        |
| print          | Displays output         |
| Default args   | Optional parameters     |
| Boolean return | Comparison result       |
| Stack frame    | Function memory         |
| Scope          | Where variable lives    |
| LEGB           | Lookup order            |
| Modularity     | Clean program design    |


