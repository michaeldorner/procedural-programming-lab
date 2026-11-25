# Lab 30: Course Prerequisite Checker

**Topics:** Sets, dictionaries, set difference  
**Lectures:** 09 (Built-in Collections), 10 (Collection Processing Patterns)

Determine missing prerequisites, enrollment eligibility, and newly unlocked courses from a prerequisite mapping.

## Requirements

- Implement `find_missing_prerequisites` to return prerequisites required for a course that have not been completed.
- Implement `can_enroll` to indicate whether all prerequisites for a course are satisfied.
- Implement `find_unlocked_courses` to return all uncompleted courses whose prerequisites are satisfied.

## Worked Examples

- With CS102 requiring CS101 and CS101 completed, CS102 is unlocked.

## Implementation Hints

- Use [`dict.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get) with an empty set default and set difference `-`.
- Optional (for pros): Use a set comprehension for `find_unlocked_courses`.

## Run & Test

```bash
python course_prerequisite_checker.py
python -m unittest
```
