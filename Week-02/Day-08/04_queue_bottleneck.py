"""
O(N) Queue Bottleneck
list.pop(0) shifts all elements.
"""

queue = list(range(10_000))
queue.pop(0)

print("Popped from front")


# Fix (real-world):

from collections import deque

queue = deque(range(10_000))
queue.popleft()
