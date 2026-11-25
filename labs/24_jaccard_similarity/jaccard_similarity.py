"""Lab 24: Jaccard Similarity."""


def jaccard_similarity(first: set[str], second: set[str]) -> float:
    """Return |first & second| / |first | second| (1.0 if both empty)."""
    raise NotImplementedError


def overlap_coefficient(first: set[str], second: set[str]) -> float:
    """Return |first & second| / min(|first|, |second|)."""
    raise NotImplementedError


def symmetric_difference(first: set[str], second: set[str]) -> set[str]:
    """Return elements in either first or second, but not both."""
    raise NotImplementedError


if __name__ == "__main__":
    print("Jaccard:", jaccard_similarity({"a", "b"}, {"b", "c"}))
