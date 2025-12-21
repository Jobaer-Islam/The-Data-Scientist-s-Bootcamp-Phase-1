
# DAY 7 — ERROR HANDLING (EXCEPTIONS)

---

## 1. What Is an Error (Exception)?

### Definition

An **exception** is a runtime error that occurs **while the program is running**, not while writing code.

Examples:

* Dividing by zero
* Converting text to a number
* Accessing a missing key

When an exception happens and **nobody handles it**, the program **crashes**.

---

## 2. Exception Bubbling (Core Idea)

### What does “bubbling” mean?

When an error occurs:

1. Python looks for a handler (`except`) in the current function
2. If not found, it moves **up the call stack**
3. If nobody catches it → program crashes

This upward movement is called **exception bubbling**.

---

## 3. try / except (Safety Net)

### Definition

`try/except` lets you **catch errors** and **handle them gracefully** instead of crashing.

### Basic Structure

```python
try:
    # risky code
except SomeError:
    # recovery code
```

---

## 4. Example: Multiple Errors (From Your Slide)

```python
while True:
    try:
        val = int(input("Enter number: "))
        print(100 / val)
        break
    except ValueError:
        print("Text is not allowed.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
```

---

### Step-by-step logic

1. User enters input
2. `int()` may fail → `ValueError`
3. `100 / val` may fail → `ZeroDivisionError`
4. Correct input → calculation → `break`

This is **defensive programming**.

---

## 5. The Input Guard (User Input Safety)

### Goal

Ask for age. If user types text → show message, don’t crash.

### Code

```python
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Numbers only")
```

---

### Why this works

* `int("twenty")` raises `ValueError`
* `except ValueError` catches it
* Program continues safely

This pattern is **mandatory** for:

* User input
* Forms
* APIs
* Data pipelines

---

## 6. The Math Safety Net (ZeroDivisionError)

### Problem

```python
x = 0
print(100 / x)
```

This crashes.

---

### Safe version

```python
try:
    x = 0
    print(100 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

### Why this matters in real life

In Data Science:

* One bad row should **not stop a 10-hour job**
* You skip bad rows, not crash the pipeline

---

## 7. finally Block (The Cleanup Crew)

### Definition

`finally` runs **no matter what**:

* Error or no error
* Return or crash

---

### Example

```python
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution complete")
```

---

### Why `finally` exists

Used for:

* Closing files
* Closing database connections
* Releasing resources
* Preventing memory leaks

---

## 8. Custom Errors (`raise`)

### Definition

You can **manually trigger errors** using `raise`.

This lets you **enforce your own rules**.

---

### Example: No Negative Numbers

```python
num = int(input("Enter number: "))

if num < 0:
    raise ValueError("No negatives allowed")

print("Number accepted:", num)
```

---

### What happens internally

* You create an exception object
* Python stops normal execution
* Python looks for an exception handler
* If none → crash (by design)

This is how **professional validation** works.

---

## 9. Types of Common Exceptions (Beginner Must-Know)

| Exception           | Cause                   |
| ------------------- | ----------------------- |
| `ValueError`        | Wrong value type        |
| `ZeroDivisionError` | Divide by zero          |
| `TypeError`         | Wrong data type         |
| `KeyError`          | Missing dictionary key  |
| `IndexError`        | List index out of range |

---

## 10. Best Practices (Important)

- Catch **specific exceptions**
- Don’t use `except:` blindly
- Validate inputs early
- Use `finally` for cleanup
- Don’t hide bugs silently

---

## 11. How This Connects to `03_boolean_logic_gate.py`

📄 **03_boolean_logic_gate.py**

```python
def is_even(num):
    return num % 2 == 0
```

### Why this is relevant

* This function **assumes valid input**
* If someone passes `"abc"` → `TypeError`
* In real systems, you combine:

  * **Boolean logic** (Day 6)
  * **Error handling** (Day 7)

---

### Safe version (advanced)

```python
def is_even(num):
    try:
        return num % 2 == 0
    except TypeError:
        return False
```

Now the function is **robust**.

---

## 12. One-Page Summary

| Concept               | Meaning                |
| --------------------- | ---------------------- |
| Exception             | Runtime error          |
| Bubbling              | Error travels up stack |
| try/except            | Safety net             |
| ValueError            | Invalid conversion     |
| ZeroDivisionError     | Divide by zero         |
| finally               | Always runs            |
| raise                 | Manual error trigger   |
| Defensive programming | Don’t trust input      |

---

