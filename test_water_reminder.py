# test_water_reminder.py

import pytest
from water_reminder import calculate_water_intake, reminder_interval

def test_calculate_water_intake():
    assert calculate_water_intake(60, 25) == 2.4  # young adult
    assert calculate_water_intake(70, 40) == 2.45  # middle-aged
    assert calculate_water_intake(80, 60) == 2.4  # senior

def test_calculate_water_intake_invalid():
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