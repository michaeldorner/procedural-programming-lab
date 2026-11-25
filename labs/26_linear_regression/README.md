# Lab 26: Linear Regression

**Topics:** Lists, aggregations, tuples, guard clauses  
**Lectures:** 09 (Built-in Collections), 10 (Collection Processing Patterns)

Fit an ordinary least-squares regression line $y = mx + b$ and compute $R^2$.

## Requirements

- Implement `fit_linear_regression` to raise a value error if the input lists differ in length, have fewer than 2 points, or have zero variance in $x$.
- Otherwise return $(m, b, R^2)$ where $m = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$, $b = \bar{y} - m\bar{x}$, and $R^2 = 1.0$ for constant $y$ or $1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}$.

## Worked Examples

- [1.0, 2.0, 3.0] and [3.0, 5.0, 7.0] yields (2.0, 1.0, 1.0).

## Implementation Hints

- Use [`zip(..., strict=True)`](https://docs.python.org/3/library/functions.html#zip) to pair `xs` and `ys`.
- Optional (for pros): Use [`statistics.mean()`](https://docs.python.org/3/library/statistics.html#statistics.mean) and [`zip(..., strict=True)`](https://docs.python.org/3/library/functions.html#zip).

## Run & Test

```bash
python linear_regression.py
python -m unittest
```
