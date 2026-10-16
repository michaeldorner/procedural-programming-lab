# Procedural Programming

This repository contains small, testable exercises for a course on procedural programming in Python at Technische Hochschule Nürnberg Georg Simon Ohm.

## Exercise Overview

```text
Procedural Programming
├── 01 Organisation
│
├── PART I — Foundations
│   ├── 02 Why do we need programming?
│   ├── 03 Values, Variables, and Expressions
│   ├── 04 Thinking in Procedures
│   └── 05 Functions as Procedures
│       ├── Rectangle Area
│       ├── Temperature Conversion
│       ├── Total Price
│       ├── Fuel Efficiency
│       ├── Loan Affordability
│       └── Valid Triangle
│
├── PART II — Control Flow
│   ├── 06 Decisions and Branching
│   │   ├── Even or Odd
│   │   ├── Maximum of Two Numbers
│   │   ├── Maximum of Three Numbers
│   │   ├── Grade Classification
│   │   ├── Leap Year
│   │   └── Rock-Paper-Scissors Outcome
│   │
│   ├── 07 Validation and Defensive Programming
│   │   ├── Valid Age
│   │   ├── Valid Examination Score
│   │   ├── Valid Triangle Sides
│   │   ├── Validate Rectangle Dimensions
│   │   ├── Validate Loan Parameters
│   │   └── ISBN-10 Format Validation
│   │
│   ├── 08 Repetition and Loops
│   │   ├── Count from 1 to n
│   │   ├── Count Down to Zero
│   │   ├── Sum from 1 to n
│   │   ├── Multiplication Table
│   │   ├── Factorial
│   │   └── Chessboard Pattern
│   │
│   └── 09 Accumulating, Counting, and Searching
│       ├── Count Even Numbers
│       ├── Find Maximum
│       ├── Find First Occurrence
│       ├── Count Occurrences
│       ├── Sum of Positive Numbers
│       └── Prime Number Test
│
├── PART III — Data
│   ├── 10 Working with Collections
│   │   ├── List Sum
│   │   ├── List Average
│   │   ├── Smallest Element
│   │   ├── Largest Element
│   │   ├── Reverse a List
│   │   └── Remove Duplicates
│   │
│   ├── 11 Mutability, References, and Side Effects
│   │   ├── Append In-Place
│   │   ├── Remove In-Place
│   │   ├── Modify a Shared List
│   │   ├── Copy and Modify
│   │   ├── Swap First and Last Element
│   │   └── Normalize Values In-Place
│   │
│   ├── 12 Structured Data
│   │   ├── Student Record
│   │   ├── Course Catalog
│   │   ├── Phone Book Lookup
│   │   ├── Inventory Item
│   │   ├── Frequency Table
│   │   └── Student Grade Analysis
│   │
│   ├── 13 Working with Time-Based Data
│   │   ├── Days Until a Deadline
│   │   ├── Age in Days
│   │   ├── Duration Between Times
│   │   ├── Working Hours Calculation
│   │   ├── Appointment Conflict Detection
│   │   └── Weekly Schedule Analysis
│   │
│   ├── 14 Processing Text
│   │   ├── Count Characters
│   │   ├── Count Vowels
│   │   ├── Reverse a String
│   │   ├── Palindrome Check
│   │   ├── Word Frequency Analysis
│   │   └── ISBN-10 Checksum Validation
│   │
│   └── 15 Processing Files
│       ├── Count Lines in a File
│       ├── Count Words in a File
│       ├── Sum Numbers from a File
│       ├── CSV Grade Statistics
│       ├── JSON Student Records
│       └── File-Based Inventory Analysis
│
└── PART IV — Building Programs
    ├── 16 Decomposing
    │   ├── Geometry Helper Library
    │   ├── Grade Management System
    │   ├── Contact Search Application
    │   ├── Expense Analysis Tool
    │   ├── Library Catalog
    │   └── Refactor a Monolithic Program
    │
    └── 17 Integrating Procedures into Small Programs
        ├── To-Do List Manager
        ├── Student Record System
        ├── Personal Expense Tracker
        ├── Appointment Scheduler
        ├── Library Management System
        └── Mini Information System
```

## Repository Structure

```text
procedural-programming/
├── README.md            # Course information and workflow
├── run_tests.py         # Runs all tests and shows overall progress
│
├── exercise_01/
│   ├── README.md        # Exercise description and examples
│   ├── solution.py      # Implement your solution here
│   └── tests/
│       ├── required/
│       │   └── ...      # Required tests
│       └── bonus/
│           └── ...      # Bonus tests
└── ...
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

## Notes

- Follow PEP8 styleguidelines.
- Do not print the result inside the function.
- Do not change the function signatures.

## How to submit

```bash
python run_tests.py

git add .
git commit -m "Complete exercise_01" # update the excercise number
git push
```

