"""Lab 27: Checkout Simulator."""


def simulate_checkout(
    customer_times: list[int],
    num_lanes: int,
) -> tuple[list[int], int]:
    """Assign customers to the least-loaded lane and return (lane_loads, total_time).

    Raises:
        ValueError: If num_lanes <= 0 or any service time is negative.
    """
    if num_lanes <= 0 or any(t < 0 for t in customer_times):
        raise ValueError("num_lanes must be positive and customer_times non-negative")
    lanes: list[int] = [0] * num_lanes
    for duration in customer_times:
        best_idx: int = 0
        for idx in range(1, num_lanes):
            if lanes[idx] < lanes[best_idx]:
                best_idx = idx
        lanes[best_idx] += duration
    return (lanes, max(lanes))


if __name__ == "__main__":
    print(simulate_checkout([5, 3, 2, 4], 2))
