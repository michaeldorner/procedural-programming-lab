# Exercise 40: Order Status

## Objective

Determine whether an order status is final.

## Tasks

Implement the following function in `solution.py`:

```python
from enum import Enum


class OrderStatus(Enum):
    OPEN = "open"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

def is_final(
    status: OrderStatus,
) -> bool:
    pass
```

## Examples

```python
is_final(OrderStatus.OPEN)
```

returns

```python
False
```
```python
is_final(OrderStatus.SHIPPED)
```

returns

```python
True
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
