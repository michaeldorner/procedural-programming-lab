# Exercise 51: List of Students

## Objective

Count students by grade label.

## Tasks

Implement the following function in `solution.py`:

```python
def count_by_grade(
    students: list[dict[str,
    str]],
) -> dict[str, int]:
    pass
```

## Examples

```python
count_by_grade([{'name': 'A', 'grade': 'A'}, {'name': 'B', 'grade': 'B'}, {'name': 'C', 'grade': 'A'}])
```

returns

```python
{'A': 2, 'B': 1}
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
