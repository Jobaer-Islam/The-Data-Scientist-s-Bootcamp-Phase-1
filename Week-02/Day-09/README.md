

# Day 9: Infinite Memory (Python Generators)

## 1. What is a Generator?

> A **generator** is a function that produces values **one at a time** using `yield` instead of returning everything at once.

**Why generators exist**

* Save memory
* Handle large or infinite data
* Process data step-by-step (lazy evaluation)

---

## 2. Basic `yield` (The Core Idea)

 Example Code

```python
def gen():
    yield 1
    yield 2
    yield 3

for value in gen():
    print(value)
```

```
Start
  ↓
yield 1 ──► pause
               ↓ next()
yield 2 ──► pause
               ↓ next()
yield 3 ──► pause
               ↓
StopIteration
```

* `yield` sends a value out
* Function **pauses**, not exits
* Local variables stay in memory
* Execution resumes from where it stopped

---

## 3. List vs Generator (Memory Difference)

### List

```python
numbers = [x for x in range(1_000_000)]
```

```
[1][2][3][4][5]...[1,000,000]
 ↑  ↑  ↑  ↑
All stored in RAM
```

### Generator

```python
numbers = (x for x in range(1_000_000))
```

```
Logic stored
↓
Generate → use → discard → next
```

* Lists store all values in memory
* Generators store only instructions
* Generators are memory-efficient

---

## 4. Infinite Sequence (Fibonacci Generator)

Example Code

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

```
yield 0
yield 1
yield 1
yield 2
yield 3
yield 5
...
(no end)
```

 
* Infinite sequences are impossible with lists
* Generators produce values on demand
* Memory usage stays constant

---

## 5. Generator Exhaustion (One-Time Use)

Example Code

```python
g = gen()
for x in g:
    print(x)

for x in g:
    print(x)  # nothing prints
```

```
Generator created
      ↓
Value 1
      ↓
Value 2
      ↓
END
      ↓
Empty forever
```

* Generators cannot be rewound
* Once exhausted, they stay empty
* Create a new generator to reuse

---

## 6. `next()` and StopIteration

```python
g = gen()
print(next(g))
print(next(g))
print(next(g))
```

```
next(gen) → value
next(gen) → value
next(gen) → StopIteration
```

* `next()` manually pulls values
* When finished, `StopIteration` is raised
* `for` loops handle this automatically

---

## 7. Generator Pipelines (Chaining)

```python
def square(nums):
    for n in nums:
        yield n * n

def even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

nums = range(10)
result = even(square(nums))
```

```
nums
 ↓
square()
 ↓
even()
 ↓
output
```

* Data flows step-by-step
* No intermediate lists created
* Used in real data pipelines

---

## 8. Large File Reader (Big Data Pattern)

```python
def read_file(path):
    with open(path) as f:
        for line in f:
            yield line
```

```
File on disk
 ↓
Read line → process → discard
 ↓
Read next line → process → discard
```

* Only one line in memory
* Handles huge files safely
* Standard big-data technique

---

## 9. `yield from` (Delegation)

```python
def gen_a():
    yield 1
    yield 2

def gen_b():
    yield 3
    yield 4

def main():
    yield from gen_a()
    yield from gen_b()
```

```
Main Generator
 ├─ yield from gen_a → values
 └─ yield from gen_b → values
```

* Delegates generator work
* Cleaner than nested loops
* Flattens outputs automatically

---

## 10. `send()` Method (Two-Way Communication)

```python
def receiver():
    value = yield
    print(value)

g = receiver()
next(g)
g.send(10)
```

 
```
Outside code
   ↓ send(value)
Generator paused at yield
   ↑ receives value
```

 
* Generator can receive data
* Two-way communication
* Foundation of coroutines and async

---

## 11. State Retention (Running Average)

 
```python
def running_average():
    total = 0
    count = 0
    while True:
        num = yield total / count if count else 0
        total += num
        count += 1
```

 
```
total=0 count=0
   ↓
send(10) → total=10 count=1
   ↓
send(20) → total=30 count=2
```

 
* Variables persist between yields
* No global variables required
* Clean state management

---

## Mental Model (Remember This)

```
Generator = Paused Function + Memory + Lazy Execution
```

---

## When to Use Generators

Use generators when:

* Data is large
* Data is infinite
* Memory matters
* Processing streams

Avoid generators when:

* You need random access
* You must reuse values many times

---

## Final Note

Generators are one of Python’s **most powerful features**.
They are essential for:

* Data science
* Machine learning pipelines
* Big data processing
* Async programming

---

Just tell me what to add next.
