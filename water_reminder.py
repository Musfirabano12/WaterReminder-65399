def calculate_water_intake(weight, age):
    if weight <= 0 or age <= 0:
        raise ValueError("Weight and age must be positive numbers.")

    if age < 30:
        water_intake = round(weight * 0.04, 2)
        temp_recommendation = "Cool water is recommended."
    elif 30 <= age <= 55:
        water_intake = round(weight * 0.035, 2)
        temp_recommendation = "Room temperature water is recommended."
    else:
        water_intake = round(weight * 0.03, 2)
        temp_recommendation = "Lukewarm water is recommended for elders."

    return water_intake, temp_recommendation

def reminder_interval(water_intake):
    if water_intake < 2:
        return "Remind every 3 hours"
    elif 2 <= water_intake < 3:
        return "Remind every 2 hours"
    else:
        return "Remind every 1 hour"

if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kg: "))
        age = int(input("Enter your age: "))

        intake, temp_suggestion = calculate_water_intake(weight, age)
        reminder = reminder_interval(intake)

        print(f"\nRecommended daily water intake: {intake} liters")
        print(f"{temp_suggestion}")
        print(f"{reminder}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception:
        print("Something went wrong. Please check your input.")
