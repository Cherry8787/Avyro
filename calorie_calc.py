# ==========================================
# FILE: calorie_calc.py
# DESCRIPTION: Scientific nutrition engine responsible for 
# calculating BMI, BMR, TDEE, calorie targets, and meal splits.
# ==========================================

def calculate_bmi(weight_kg: float, height_cm: float) -> tuple[float, str]:
    """
    Calculates the Body Mass Index (BMI) based on weight in kilograms and height in centimeters,
    and returns a status.
    
    Args:
        weight_kg (float): Weight of the user in kilograms.
        height_cm (float): Height of the user in centimeters.
        
    Returns:
        tuple[float, str]: Calculated BMI rounded to 1 decimal place and descriptive category string.
    """
    # Convert height from centimeters to meters
    height_m = height_cm / 100
    
    # Calculate BMI formula: weight (kg) / [height (m)]^2
    bmi = round(weight_kg / (height_m**2), 1)

    # Assign wellness categories
    if bmi < 18.5:
        category = "Balanced Focus"
    elif 18.5 <= bmi < 24.9:
        category = "Optimal Balance"
    elif 25.0 <= bmi < 29.9:
        category = "Vitality Focus"
    else:
        category = "Wellness Focus"

    return bmi, category


def calculate_bmr(
    gender: str, weight_kg: float, height_cm: float, age: int
) -> float:
    """
    Calculates Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Formula.
    
    Args:
        gender (str): User gender ("Male" or "Female").
        weight_kg (float): Weight in kilograms.
        height_cm (float): Height in centimeters.
        age (int): Age in years.
        
    Returns:
        float: Calculated BMR in calories/day.
    """
    # Apply Mifflin-St Jeor equations differentiated by gender
    if gender.strip().lower() == "male":
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:  # Female equation variant
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    return bmr


def calculate_tdee(bmr: float, activity_level: str) -> float:
    """
    Multiplies BMR by the corresponding physical activity level multiplier.
    
    Args:
        bmr (float): Basal Metabolic Rate.
        activity_level (str): User-selected activity frequency string.
        
    Returns:
        float: Total Daily Energy Expenditure (TDEE).
    """
    # Standard activity multiplier mapping dictionary
    multipliers = {
        "sedentary": 1.2,    # Little to no exercise
        "light": 1.375,      # Light exercise 1-3 days/week
        "moderate": 1.55,    # Moderate exercise 3-5 days/week
        "active": 1.725,     # Hard exercise 6-7 days/week
        "n/a": 1.2,          # Default fallback
    }
    
    key = activity_level.strip().lower()
    factor = multipliers.get(key, 1.2)
    return bmr * factor


def get_target_calories(tdee: float, target_goal: str, medical_condition: str = "General Wellness") -> int:
    """
    Adjusts daily caloric intake based on primary fitness goal and specific medical conditions.
    
    Args:
        tdee (float): Total Daily Energy Expenditure.
        target_goal (str): Weight Loss, Maintain Weight, or Weight Gain.
        medical_condition (str): Specific health focus/condition.
        
    Returns:
        int: Final target daily calories.
    """
    goal = target_goal.strip().lower()

    # Base adjustments according to goal
    if "loss" in goal:
        target = tdee - 400
    elif "gain" in goal:
        target = tdee + 400
    else:
        target = tdee

    # Refine target based on medical condition nutritional standards
    condition = medical_condition.strip().lower()
    if "diabetes" in condition:
        target = min(target, tdee - 150)
    elif "blood pressure" in condition:
        target = target - 100

    return int(round(target))


def get_meal_calorie_split(target_calories: int) -> dict:
    """
    Distributes total daily target calories across 4 meals.
    
    Args:
        target_calories (int): Daily total target calorie goal.
        
    Returns:
        dict: Calorie targets allocated for Breakfast, Lunch, Snacks, and Dinner.
    """
    return {
        "Breakfast": int(round(target_calories * 0.25)),  # 25% allocation
        "Lunch": int(round(target_calories * 0.35)),      # 35% allocation
        "Snacks": int(round(target_calories * 0.10)),     # 10% allocation
        "Dinner": int(round(target_calories * 0.30)),     # 30% allocation
    }