"""Lab 24: Jaccard Similarity."""


def calculate_jaccard_similarity(first: set[str], second: set[str]) -> float:
    """Return |first & second| / |first | second| (1.0 if both empty)."""
    raise NotImplementedError


def calculate_overlap_coefficient(first: set[str], second: set[str]) -> float:
    """Return |first & second| / min(|first|, |second|)."""
    raise NotImplementedError


def find_symmetric_difference(first: set[str], second: set[str]) -> set[str]:
    """Return elements in either first or second, but not both."""
    raise NotImplementedError


if __name__ == "__main__":
    print("Jaccard:", calculate_jaccard_similarity({"a", "b"}, {"b", "c"}))
