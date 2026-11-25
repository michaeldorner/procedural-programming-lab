# Lab 29: CPU Round-Robin

**Topics:** Queues, `while` loops, lists, guard clauses  
**Lectures:** 08 (Loops), 09 (Built-in Collections)

Simulate a Round-Robin CPU scheduler with a fixed time quantum for processes arriving at time 0.

## Requirements

- Implement `simulate_round_robin` to raise a value error if the quantum or any burst time is non-positive.
- Execute processes in cyclic order for up to `quantum` time units per turn and return each process's completion time in original order.

## Worked Examples

- Burst times [5, 3, 1] with quantum 2 yield completion times [9, 8, 5].

## Implementation Hints

- Use [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque) for $O(1)$ queue rotations.

## Run & Test

```bash
python cpu_round_robin.py
python -m unittest
```
