"""Lab 04: Battery Pack Sizing."""


def pack_voltage(cell_voltage: float, series_count: int) -> float:
    """Return total pack voltage for series_count cells in series."""
    if cell_voltage <= 0.0 or series_count <= 0:
        raise ValueError("cell_voltage and series_count must be positive")
    return cell_voltage * series_count


def pack_energy_wh(
    cell_voltage: float,
    cell_ah: float,
    series_count: int,
    parallel_count: int,
) -> float:
    """Return total pack energy capacity in Watt-hours."""
    if cell_voltage <= 0.0 or cell_ah <= 0.0 or series_count <= 0 or parallel_count <= 0:
        raise ValueError("cell_voltage, cell_ah, series_count, and parallel_count must be positive")
    return cell_voltage * cell_ah * series_count * parallel_count


def charge_time_hours(energy_wh: float, charger_watts: float, efficiency: float) -> float:
    """Return estimated charge duration in hours accounting for efficiency."""
    if energy_wh < 0.0 or charger_watts <= 0.0 or not (0.0 < efficiency <= 1.0):
        raise ValueError("Invalid energy_wh, charger_watts, or efficiency in (0, 1]")
    return energy_wh / (charger_watts * efficiency)


if __name__ == "__main__":
    wh = pack_energy_wh(3.6, 2.5, 10, 4)
    print("Pack Wh:", wh, "Charge h:", charge_time_hours(wh, 100.0, 0.9))
