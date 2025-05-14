# water_reminder.py

def calculate_water_intake(weight, age):
    if weight <= 0 or age <= 0:
        raise ValueError("Weight and age must be positive numbers.")
    if age < 30:
        return round(weight * 0.04, 2)
    elif 30 <= age <= 55:
        return round(weight * 0.035, 2)
    else:
        return round(weight * 0.03, 2)

def reminder_interval(water_intake):
    if water_intake < 2:
        return "Remind every 3 hours"
    elif 2 <= water_intake < 3:
        return "Remind every 2 hours"
    else:
        return "Remind every 1 hour"