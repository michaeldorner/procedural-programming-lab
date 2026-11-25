"""Lab 04: Battery Pack Sizing."""


def pack_voltage(cell_voltage: float, series_count: int) -> float:
    """Return total pack voltage for series_count cells in series."""
    raise NotImplementedError


def pack_energy_wh(
    cell_voltage: float,
    cell_ah: float,
    series_count: int,
    parallel_count: int,
) -> float:
    """Return total pack energy capacity in Watt-hours."""
    raise NotImplementedError


def charge_time_hours(energy_wh: float, charger_watts: float, efficiency: float) -> float:
    """Return estimated charge duration in hours accounting for efficiency."""
    raise NotImplementedError


if __name__ == "__main__":
    wh = pack_energy_wh(3.6, 2.5, 10, 4)
    print("Pack Wh:", wh, "Charge h:", charge_time_hours(wh, 100.0, 0.9))
