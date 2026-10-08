def calculate_bmi(weight_kg: float, height_cm: float) -> tuple[float, str]:
    """Calculates BMI and returns value with category status."""
    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m**2), 1)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25.0 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


def calculate_bmr(
    gender: str, weight_kg: float, height_cm: float, age: int
) -> float:
    """Calculates Base Metabolic Rate using Mifflin-St Jeor Formula."""
    if gender.strip().lower() == "male":
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:  # female
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    return bmr


def calculate_tdee(bmr: float, activity_level: str) -> float:
    """Multiplies BMR by activity factor derived from questionnaire."""
    # Activity multiplier mapping
    multipliers = {
        "sedentary": 1.2,  # Little to no exercise
        "light": 1.375,  # 1-3 days/week
        "moderate": 1.55,  # 3-5 days/week
        "active": 1.725,  # 6-7 days/week
        "n/a": 1.2,  # Default fallback if user selects N/A
    }

    key = activity_level.strip().lower()
    factor = multipliers.get(key, 1.2)
    return bmr * factor


def get_target_calories(tdee: float, target_goal: str) -> int:
    """Adjusts calories based on user goal (Weight Loss / Maintain / Weight Gain)."""
    goal = target_goal.strip().lower()

    if "loss" in goal:
        target = tdee - 400
    elif "gain" in goal:
        target = tdee + 400
    else:  # Maintenance or default
        target = tdee

    return int(round(target))


def get_meal_calorie_split(target_calories: int) -> dict:
    """Splits target calories across 4 meals: Breakfast, Lunch, Snacks, Dinner."""
    return {
        "Breakfast": int(round(target_calories * 0.25)),
        "Lunch": int(round(target_calories * 0.35)),
        "Snacks": int(round(target_calories * 0.10)),
        "Dinner": int(round(target_calories * 0.30)),
    }