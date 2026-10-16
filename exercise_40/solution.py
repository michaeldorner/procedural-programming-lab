from enum import Enum


class OrderStatus(Enum):
    OPEN = "open"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


# Student template
def is_final(
    status: OrderStatus,
) -> bool:
    pass


# Basic solution
def is_final(
    status: OrderStatus,
) -> bool:
    return status == OrderStatus.SHIPPED


# Excellent solution for bonus tests
def is_final(
    status: OrderStatus,
) -> bool:
    return status in (OrderStatus.SHIPPED, OrderStatus.CANCELLED)
