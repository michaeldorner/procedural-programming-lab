# Student template
def shopping_cart_total(
    cart: dict[str,
    int],
    prices: dict[str,
    float],
) -> float:
    pass


# Basic solution
def shopping_cart_total(
    cart: dict[str,
    int],
    prices: dict[str,
    float],
) -> float:
    total = 0.0
    for item, quantity in cart.items():
        total += quantity * prices[item]
    return total


# Excellent solution for bonus tests
def shopping_cart_total(
    cart: dict[str,
    int],
    prices: dict[str,
    float],
) -> float:
    total = 0.0
    for item, quantity in cart.items():
        total += quantity * prices[item]
    return total
