"""Unit conversion logic. No web code in here, so it is easy to test."""

LENGTH = {  # how many metres in one unit
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "mi": 1609.344,
    "yd": 0.9144,
}

WEIGHT = {  # how many kilograms in one unit
    "g": 0.001,
    "kg": 1.0,
    "lb": 0.45359237,
    "oz": 0.028349523125,
}

FACTORS = {"length": LENGTH, "weight": WEIGHT}

UNITS = {
    "length": list(LENGTH),
    "weight": list(WEIGHT),
    "temperature": ["C", "F", "K"],
}

ABSOLUTE_ZERO_C = -273.15


def _to_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5 / 9
    return value - 273.15  # Kelvin


def _from_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return value * 9 / 5 + 32
    return value + 273.15  # Kelvin


def convert(category, value, from_unit, to_unit):
    if category not in UNITS:
        raise ValueError(f"Unknown category: {category}")

    for unit in (from_unit, to_unit):
        if unit not in UNITS[category]:
            raise ValueError(f"Unknown {category} unit: {unit}")

    if category == "temperature":
        celsius = _to_celsius(value, from_unit)
        if celsius < ABSOLUTE_ZERO_C - 1e-9:
            raise ValueError("That is below absolute zero")
        result = _from_celsius(celsius, to_unit)
    else:
        factors = FACTORS[category]
        result = value * factors[from_unit] / factors[to_unit]

    return round(result, 6)
