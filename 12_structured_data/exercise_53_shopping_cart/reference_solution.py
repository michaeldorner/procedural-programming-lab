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
