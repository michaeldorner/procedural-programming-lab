# Procedural Python Labs

Hands-on, spiral-curriculum lab repository accompanying the **Procedural Programming** course (Python 3.12+, standard library only).


## Requirements

- Python 3.10 or higher (required)
- Git (optional)

## Git Template & Remote Setup

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
