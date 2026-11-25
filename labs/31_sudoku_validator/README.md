# Lab 31: Sudoku Validator

**Topics:** 2D nested lists, sets, nested loops  
**Lectures:** 08 (Loops), 09 (Built-in Collections)

Verify whether a 9x9 integer grid is a valid completed Sudoku solution.

## Requirements

- Implement `is_valid_sudoku` to ensure the grid is 9x9.
- Verify that every row, every column, and every 3x3 subgrid contains each digit from 1 to 9 exactly once.

## Worked Examples

- A valid completed 9x9 board returns true; swapping two cells in a box returns false.

## Implementation Hints

- Use [`set`](https://docs.python.org/3/library/stdtypes.html#set) equality against `{1, 2, 3, 4, 5, 6, 7, 8, 9}`.

## Run & Test

```bash
python sudoku_validator.py
python -m unittest
```
