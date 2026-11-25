import pytest

from converter import convert


@pytest.mark.parametrize(
    "category, value, from_unit, to_unit, expected",
    [
        ("length", 1, "km", "m", 1000),
        ("length", 1, "mi", "km", 1.609344),
        ("length", 12, "in", "ft", 1),
        ("length", 100, "cm", "m", 1),
        ("weight", 1, "kg", "g", 1000),
        ("weight", 1, "kg", "lb", 2.204623),
        ("weight", 16, "oz", "lb", 1),
        ("temperature", 0, "C", "F", 32),
        ("temperature", 100, "C", "F", 212),
        ("temperature", 32, "F", "C", 0),
        ("temperature", 0, "C", "K", 273.15),
        ("temperature", 273.15, "K", "C", 0),
    ],
)
def test_conversions(category, value, from_unit, to_unit, expected):
    result = convert(category, value, from_unit, to_unit)
    assert result == pytest.approx(expected, abs=1e-5)


def test_same_unit_returns_same_value():
    assert convert("length", 5, "m", "m") == 5


def test_unknown_category():
    with pytest.raises(ValueError):
        convert("speed", 1, "kmh", "mph")


def test_unknown_unit():
    with pytest.raises(ValueError):
        convert("length", 1, "km", "parsec")


def test_below_absolute_zero():
    with pytest.raises(ValueError):
        convert("temperature", -300, "C", "K")


def test_negative_kelvin():
    with pytest.raises(ValueError):
        convert("temperature", -1, "K", "C")
