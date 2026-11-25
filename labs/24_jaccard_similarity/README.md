# Lab 24: Jaccard Similarity

**Topics:** Sets, set operations, guard clauses  
**Lectures:** 09 (Built-in Collections)

Compare two token sets using Jaccard similarity, overlap coefficient, and symmetric difference.

## Requirements

- Implement `jaccard_similarity` as $|A \cap B| / |A \cup B|$ (1.0 when both sets are empty).
- Implement `overlap_coefficient` as $|A \cap B| / \min(|A|, |B|)$ (1.0 if both empty, 0.0 if only one is empty).
- Implement `symmetric_difference` to return elements belonging to exactly one of the two sets.

## Worked Examples

- {"a", "b"} and {"b", "c"} have Jaccard similarity 1/3 and symmetric difference {"a", "c"}.

## Implementation Hints

- Use `&`, `|`, and `^`; see [Set Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).

## Run & Test

```bash
python jaccard_similarity.py
python -m unittest
```
