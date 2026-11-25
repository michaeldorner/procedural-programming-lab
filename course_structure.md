# Procedural Python (7 ECTS) – Course Architecture

## Core Pedagogy & Technical Stack

* **Language & Runtime:** Python 3.12+ (Standard Library only; zero external dependencies).
* **Tooling:** VS Code (`Shift+Enter` scratchpads and built-in Debugger), plain Git (`main` vs. `solutions` branches), and Typst (for lecture slides).
* **Coding Standards:** Mandatory PEP 484 type annotations, PEP 8 casing, intent-revealing domain names, and verb-first function naming introduced progressively across every part.

## Course Terminology & Ecosystem

To maintain clear boundaries across different tools and platforms, the course strictly adheres to the following decoupled terminology:

* **Syllabus (Typst & Markdown):**
  * **Part** (`Part I`–`Part VI`): Major thematic sections of the curriculum.
  * **Block** (`01`–`20`): Individual conceptual lecture units.
* **Moodle (Theory & Mental Tracing):**
  * **Concept Check**: A self-paced, auto-graded quiz activity to practice mental tracing before coding.
  * **Question**: An individual item (e.g., Short Answer, Multiple Choice) within a Concept Check.
* **Git Repository (Hands-on Coding):**
  * **Lab** (`XX_<topic>/`): The top-level folder matching a lecture Block 1-to-1.
  * **Task** (`YY_<domain_topic>/`): A problem folder containing its own `README.md`, a domain-named starter module (`<module>.py`), and a matching test suite (`test_<module>.py`).
  * **Step** (`Step 1`, `Step 2`, ...): Sequential sub-problems within a single task's `README.md`.

## Lab & Testing Mechanics

* **Integrated Onboarding:** Environment setup, VS Code workflow, and a minimal Git guide live directly in the root repository `README.md` so the first lecture focuses purely on programming concepts.
* **Clean Imports:** Task folders explicitly omit `__init__.py` to ensure standard library `unittest` suites can cleanly resolve domain-named modules (`from <module> import ...`).
* **Task Progression:**
  * **Block 01:** Running `import this` interactively.
  * **Blocks 02–03:** Module-level variable assignments. `unittest` inspects module attributes and `__annotations__` directly.
  * **Blocks 04–16:** Function implementation. `unittest` verifies return values and side effects.
  * **Blocks 17–20:** Multi-file modular architecture, student-authored `unittest` suites, and `argparse` CLIs.
* **Lecture-Only Benchmarks:** Empirical runtime measurements (`time.perf_counter()`) in Blocks 09, 10, and 15 are purely for lecture demonstration to build intuition. Automated tests do not assert execution times.

---

## Part I: Foundations (Blocks 01–05)

*Focus: Computational thinking, Python's execution model, types, functions, scope, and foundational naming habits.*

* **01 Introduction to Programming & Python**
  * The power of software: automation at scale, computational thinking, and why programming matters in the LLM era.
  * Formal, unambiguous programming languages vs. flexible human language.
  * Code is written for humans first (Abelson & Sussman); Python's design philosophy and *The Zen of Python* (PEP 20 / `import this`).
  
* **02 Data Types, Variables & Expressions**
  * Scalar base types (`int`, `float`, `bool`, `str`) and `NoneType`.
  * Explicit type conversions (`int()`, `float()`, `str()`, `bool()`) and mandatory PEP 484 type annotations (`age: int = 20`).
  * Naming Conventions: `snake_case` for variables, intent-revealing domain names (`monthly_income`), avoiding generic names (`data`), **never encoding types in names** (`name_str` $\rightarrow$ `name`), and phrasing booleans like yes/no questions (`is_valid`, `has_passed_exam`).

* **03 Operators & Expressions**
  * Arithmetic, floor division (`//`), modulo (`%`), exponentiation (`**`), comparison, and boolean operators.
  * Assignment (`=`) vs. equality (`==`), top-to-bottom sequential execution, variable reassignment state traces (`x = x + 1`), operator precedence, and floating-point precision awareness.
  * Naming Conventions: PEP 8 line breaks before binary operators.

* **04 Functions**
  * The Input $\rightarrow$ Processing $\rightarrow$ Output mental model formalized via `def`, parameters, arguments, and `return`.
  * Naming Conventions: Verb-first `snake_case` function names (`calculate_rectangle_area`, `validate_isbn`) and predicate prefixes (`is_`, `has_`) for `bool`-returning functions.

* **05 Scope**
  * Local vs. Global scope (`L -> G -> B`), call frames, `UnboundLocalError`, and banning mutable global variables.
  * Naming Conventions: `UPPER_SNAKE_CASE` for module-level constants (`TAX_RATE`) and avoiding reserved Python keywords.

---

## Part II: Control Flow (Blocks 06–08)

*Focus: Routing execution, defensive error handling, and iteration.*

* **06 Branching**
  * `if`, `elif`, `else`, truthiness, and conditional expressions.
  * Naming Conventions: Idiomatic boolean conditions (`if is_valid:` instead of `if is_valid == True:`).

* **07 Validation & Exceptions**
  * `try`, `except`, `else`, `finally`, and `raise`. Handling `ValueError`, `TypeError`, `ZeroDivisionError`.
  * Naming Conventions: `PascalCase` for built-in exception types and descriptive names for caught exceptions (`except ValueError as error:`).

* **08 Loops**
  * `while` and `for` loops, `range()`, `break`, and `continue`.
  * Naming Conventions: Naming loop targets after a singular element of the iterable (`for grade in grades:`), reserving `i`/`j` strictly for numeric indices.

---

## Part III: Collections & Memory (Blocks 09–12)

*Focus: General-purpose containers, traversal patterns, and object-reference semantics in RAM.*

* **09 Built-in Collections**
  * Sequences (`list`, `tuple`, `str`), sets (`set`), and mappings (`dict`).
  * Naming Conventions: Plural nouns for homogeneous sequences (`valid_isbns`) and key-to-value relationship names for dictionaries (`grades_by_student`).

* **10 Collection Processing Patterns**
  * Accumulators, filtering, transforming, searching, and frequency counting/grouping.
  * Pythonic iteration (`enumerate()`, `zip()`) and built-in aggregations (`sum`, `min`, `max`, `any`, `all`).

* **11 Mutability & Memory**
  * Value equality vs. object identity (`==` vs. `is`).
  * Aliasing, copies, and rebinding local parameters vs. mutating shared objects.

* **12 Symbolic Constants & Enums**
  * Constants and Enums as the only acceptable module-level (global) values.
  * Naming Conventions: `PascalCase` for `Enum` types (`OrderStatus`) and `UPPER_SNAKE_CASE` for members (`OrderStatus.PENDING`).

---

## Part IV: Text & Time Processing (Blocks 13–14)

*Focus: Parsing, normalizing, and formatting domain values purely in memory.*

* **13 Text Processing**
  * String methods (`strip`, `split`, `join`, `replace`), `string` module, f-strings, and Unicode vs. UTF-8 `bytes`.
  * Naming Conventions: Distinguishing raw vs. normalized strings (`raw_line` vs. `cleaned_email`).

* **14 Time-Based Data**
  * `datetime`, `date`, `time`, `timedelta`, ISO 8601 parsing, and timezone-aware timestamps with `zoneinfo`.
  * Naming Conventions: Encoding physical units in numeric durations (`timeout_seconds`, `elapsed_ms`).

---

## Part V: External I/O (Blocks 15–16)

*Focus: Crossing the OS and network boundary, persistence, and external failure modes.*

* **15 File Processing**
  * `pathlib.Path`, context managers, plain text, `csv`, `json`, and handling I/O exceptions.
  * Naming Conventions: Distinguishing `pathlib.Path` handles (`report_file`) from parsed contents (`csv_rows`).

* **16 Consuming Web APIs**
  * `urllib.parse`, `urllib.request`, decoding JSON payloads, and network failures.
  * Naming Conventions: Separating network verbs (`fetch_forecast`) from payload parsing verbs (`parse_weather_payload`).

---

## Part VI: Program Design & Console Application (Blocks 17–20)

*Focus: Multi-file architecture, CLI ergonomics, software testing, and building a complete application.*

* **17 Modular Decomposition**
  * Splitting scripts into cohesive `.py` modules, `import` mechanics, and `def main() -> None:`.
  * Naming Conventions: Short `snake_case` filenames (`pricing.py`) and a leading underscore (`_parse_row`) for internal helpers.

* **18 Command-Line Interfaces (`argparse`)**
  * Unix-style CLIs with `argparse`, `sys.exit`, and environment configuration.
  * Naming Conventions: Mapping kebab-case terminal flags (`--output-file`) to matching `snake_case` attributes.

* **19 Unit Testing**
  * Standard library `unittest`, core assertions (`assertEqual`, `assertRaises`).
  * Naming Conventions: `PascalCase` `Test<Target>` classes and descriptive `test_<function>_<scenario>` methods.

* **20 First Full Console Application**
  * End-to-end integration: multi-file decomposition, subcommands, text/time parsing, file persistence, and complete student-authored tests.