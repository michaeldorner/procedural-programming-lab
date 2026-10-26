# Exercise 55: Group by Category

## Objective

Group item names by category.

## Tasks

Implement the following function in `solution.py`:

```python
def group_by_category(
    items: list[dict[str,
    str]],
) -> dict[str, list[str]]:
    pass
```

## Examples

```python
group_by_category([{'name': 'apple', 'category': 'fruit'}, {'name': 'pear', 'category': 'fruit'}])
```

returns

```python
{'fruit': ['apple', 'pear']}
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
