"""Lab 24: Jaccard Similarity."""


def jaccard_similarity(first: set[str], second: set[str]) -> float:
    """Return |first & second| / |first | second| (1.0 if both empty)."""
    union_size: int = len(first | second)
    if union_size == 0:
        return 1.0
    return len(first & second) / union_size


def overlap_coefficient(first: set[str], second: set[str]) -> float:
    """Return |first & second| / min(|first|, |second|)."""
    if not first and not second:
        return 1.0
    if not first or not second:
        return 0.0
    return len(first & second) / min(len(first), len(second))


def symmetric_difference(first: set[str], second: set[str]) -> set[str]:
    """Return elements in either first or second, but not both."""
    return first ^ second


if __name__ == "__main__":
    print("Jaccard:", jaccard_similarity({"a", "b"}, {"b", "c"}))
