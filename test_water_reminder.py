from water_reminder import calculate_water_intake, reminder_interval

def test_calculate_water_intake():
    assert calculate_water_intake(60, 25) == (2.4, "Cool water is recommended.")
    assert calculate_water_intake(70, 40) == (2.45, "Room temperature water is recommended.")
    assert calculate_water_intake(80, 60) == (2.4, "Lukewarm water is recommended for elders.")

def test_calculate_water_intake_invalid():
    import pytest
    with pytest.raises(ValueError):
        calculate_water_intake(-50, 25)
    with pytest.raises(ValueError):
        calculate_water_intake(60, -10)
    with pytest.raises(ValueError):
        calculate_water_intake(0, 0)

def test_reminder_interval():
    assert reminder_interval(1.5) == "Remind every 3 hours"
    assert reminder_interval(2.5) == "Remind every 2 hours"
    assert reminder_interval(3.5) == "Remind every 1 hour"
