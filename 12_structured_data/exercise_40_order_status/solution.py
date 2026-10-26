from enum import Enum


class OrderStatus(Enum):
    OPEN = "open"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

def is_final(
    status: OrderStatus,
) -> bool:
    pass
