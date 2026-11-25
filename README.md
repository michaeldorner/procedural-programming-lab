# Procedural Python Labs

Hands-on, spiral-curriculum lab repository accompanying the **Procedural Programming** course (Python 3.12+, standard library only).

## 1. Setup & Running Tests

1. **Python 3.12+:** Verify your installation with `python --version`.
2. **VS Code Extensions:** Install **Python**, **Pylance**, and **Ruff**.
3. **Run a Lab:** Navigate into any lab folder (`labs/<NN>_<name>/`), implement `<name>.py`, and run:

```bash
cd labs/03_temperature_scales
python temperature_scales.py
python -m unittest
```

4. **Static Analysis:** Check style and strict type annotations from the repository root:

```bash
ruff check labs
```

## 2. Git Template & Remote Setup

This repository is a GitHub **template** located at `https://github.com/michaeldorner/procedural-programming-lab.git`.

1. **Create your private repository:** Open [the course template repository](https://github.com/michaeldorner/procedural-programming-lab) and click **Use this template** $\rightarrow$ **Create a new repository** (set visibility to **Private**).
2. **Clone your private repository:**

```bash
git clone <your-private-repository-url>
cd procedural-programming-lab
```

3. **Add the course template as `upstream` remote** so you can pull updates and new labs:

```bash
git remote add upstream https://github.com/michaeldorner/procedural-programming-lab.git
git remote -v
```

4. **Pull future updates from `upstream`:**

```bash
git fetch upstream
git merge upstream/main
```

