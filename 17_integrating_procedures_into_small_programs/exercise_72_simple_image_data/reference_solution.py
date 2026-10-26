def _read_pixel_brightness_values(
    filename: str,
) -> list[float]:
    with open(filename, encoding="utf-8") as file:
        tokens = file.read().split()
    width = int(tokens[1])
    height = int(tokens[2])
    max_value = int(tokens[3])
    values = [int(token) for token in tokens[4:]]
    brightness_values = []
    for index in range(0, width * height * 3, 3):
        red = values[index]
        green = values[index + 1]
        blue = values[index + 2]
        brightness_values.append((red + green + blue) / 3 / max_value)
    return brightness_values


def average_brightness(
    filename: str,
) -> float:
    brightness_values = _read_pixel_brightness_values(filename)
    return sum(brightness_values) / len(brightness_values)


def count_dark_pixels(
    filename: str,
    threshold: float,
) -> int:
    count = 0
    for brightness in _read_pixel_brightness_values(filename):
        if brightness < threshold:
            count += 1
    return count
