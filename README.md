# Procedural Programming

This repository contains small, testable exercises for a course on procedural programming in Python.

## Exercise Overview

```text
exercise_01 - exercise_05    Basic calculations and functions
exercise_06 - exercise_10    Conditionals and decision logic
exercise_11 - exercise_16    Loops and algorithmic patterns
exercise_17 - exercise_24    Lists
exercise_25 - exercise_28    Tuples
exercise_29 - exercise_32    Sets
exercise_33 - exercise_38    Dictionaries
exercise_39 - exercise_42    Enums and named states
exercise_43 - exercise_49    Strings and text processing
exercise_50 - exercise_55    Combined data structures
exercise_56 - exercise_60    Files and simple CSV data
exercise_61 - exercise_66    Dates and times
exercise_67 - exercise_71    Small console-program building blocks
exercise_72                  Simple image data
```

## Repository Structure

```text
procedural-programming/
├── README.md            # Course information and workflow
├── run_tests.py         # Runs all tests and shows overall progress
│
├── exercise_01/
│   ├── README.md        # Exercise description and examples
│   ├── solution.py      # Student template, basic solution, excellent solution
│   └── tests/
│       ├── required/
│       │   └── ...      # Required tests
│       └── bonus/
│           └── ...      # Bonus tests
└── ...
```

## Important Note About `solution.py`

Each `solution.py` contains three versions of the same functions:

1. a student template,
2. a basic solution,
3. an excellent solution for the bonus tests.

Python keeps the last definition of a function name. Therefore, the excellent solution is the active implementation in these files.

For student distribution, remove the basic and excellent solution sections and keep only the student template.

## Workflow

```bash
python run_tests.py

git add .
git commit -m "Complete exercise_01"
git push
```

## Running Tests

Run tests for a single exercise:

```bash
cd exercise_01
python -m unittest discover tests -v
```

Run all exercises:

```bash
python run_tests.py
```

## Scope

This course focuses on procedural programming.

The exercises use variables, data types, control structures, functions, built-in data structures, `Enum`, dates, times, files, and simple text-based image data.

Object-oriented programming is not part of this course.
