# Exercise 54: Contact Search

## Objective

Find a contact by name.

## Tasks

Implement the following function in `solution.py`:

```python
def contact_search(
    contacts: list[dict[str,
    str]],
    name: str,
) -> dict[str, str] | None:
    pass
```

## Examples

```python
contact_search([{'name': 'Ada', 'phone': '123'}], 'Ada')
```

returns

```python
{'name': 'Ada', 'phone': '123'}
```

## Notes

- Return the requested value.
- Do not print the result inside the function.
- Do not change the function signatures.
