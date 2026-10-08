# meal_planner.py

import random
from food_db import FOOD_DATABASE


def filter_foods_by_preference(
    meal_category: str, prep_preference: str
) -> list:
    """Filters available foods in a category based on user prep style preference."""
    all_category_foods = FOOD_DATABASE.get(meal_category, [])

    # If user selected "I like cooking fresh meals", match Fresh cooking
    # If user selected "No cook / assembly", match Assembly-only
    # If user selected "Takeout", match Restaurant / Takeout
    # If user selected "Grocery", match Grocery grab & go
    pref_map = {
        "a": "Fresh cooking",
        "b": "Assembly-only",
        "c": "Restaurant / Takeout",
        "d": "Grocery grab & go",
    }

    target_prep = pref_map.get(prep_preference.lower(), "Assembly-only")

    # Filter matching items
    matching_foods = [
        item
        for item in all_category_foods
        if item["prep_type"].lower() == target_prep.lower()
    ]

    # Fallback: if no specific match, return all foods in that category
    return matching_foods if matching_foods else all_category_foods


def generate_daily_meal_plan(
    prep_preference: str, previous_day_plan: dict = None
) -> dict:
    """Generates a random 4-meal plan while preventing consecutive day repeats."""
    if previous_day_plan is None:
        previous_day_plan = {}

    meal_slots = ["Breakfast", "Lunch", "Snacks", "Dinner"]
    daily_plan = {}

    for slot in meal_slots:
        available_options = filter_foods_by_preference(slot, prep_preference)
        last_item_name = previous_day_plan.get(slot, {}).get("name")

        # Exclude yesterday's meal item to satisfy non-consecutive rule
        valid_options = [
            item
            for item in available_options
            if item["name"] != last_item_name
        ]

        # If filtering out yesterday's meal leaves no options, fallback to all available
        if not valid_options:
            valid_options = available_options

        # Pick a random meal from valid choices
        daily_plan[slot] = random.choice(valid_options)

    return daily_plan