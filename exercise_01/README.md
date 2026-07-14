# Exercise 01: Rectangles

## Objective

Implement two functions that calculate the area and perimeter of a rectangle.

## Tasks

Implement the following functions in `solution.py`:

```python
def rectangle_area(
    width: float,
    height: float,
) -> float:
    pass


def rectangle_perimeter(
    width: float,
    height: float,
) -> float:
    pass
```

## Examples

### Area

```python
rectangle_area(3.0, 4.0)
```

returns

```python
12.0
```

### Perimeter

```python
rectangle_perimeter(3.0, 4.0)
```

returns

```python
14.0
```

## Required Tests

Your solution must pass all tests in:

```text
tests/required/
```

Run the required tests with:

```bash
python -m unittest discover tests/required -v
```

## Bonus Tests

You can earn distinction by passing the bonus tests in:

```text
tests/bonus/
```

Run the bonus tests with:

```bash
python -m unittest discover tests/bonus -v
```

## Run All Tests

Run all tests for this exercise:

```bash
python -m unittest discover tests -v
```

## Coding Guidelines

- Follow PEP 8.
- Use meaningful variable names.
- Do not modify the test files.
- Do not change the function signatures.

## Expected Results

### Passed

All required tests pass.

```text
✅ exercise_01
```

### Passed with Distinction

All required and bonus tests pass.

```text
🌟 exercise_01
```

## Submission

Commit and push your solution:

```bash
git add .
git commit -m "Solve exercise_01"
git push
```
