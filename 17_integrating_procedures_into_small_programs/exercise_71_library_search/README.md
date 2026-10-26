# Exercise 71: Library Search

## Objective

Find a book by title.

## Tasks

Implement the following function in `solution.py`:

```python
def library_search(
    books: list[dict[str,
    str]],
    title: str,
) -> dict[str, str] | None:
    pass
```

## Examples

```python
library_search([{'title': 'Dune', 'author': 'Frank Herbert'}], 'Dune')
```

returns

```python
{'title': 'Dune', 'author': 'Frank Herbert'}
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
