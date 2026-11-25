"""Lab 27: Checkout Simulator."""


def simulate_checkout(
    customer_times: list[int],
    num_lanes: int,
) -> tuple[list[int], int]:
    """Assign customers to the least-loaded lane and return (lane_loads, total_time).

Raises:
    ValueError: If num_lanes <= 0 or any service time is negative.
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(simulate_checkout([5, 3, 2, 4], 2))
