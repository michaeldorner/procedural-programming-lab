# Exercise 41: Game Result

## Objective

Map game results to points.

## Tasks

Implement the following function in `solution.py`:

```python
from enum import Enum


class GameResult(Enum):
    WIN = "win"
    DRAW = "draw"
    LOSS = "loss"

def points_for_result(
    result: GameResult,
) -> int:
    pass
```

## Examples

```python
points_for_result(GameResult.WIN)
```

returns

```python
3
```
```python
points_for_result(GameResult.DRAW)
```

returns

```python
1
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
