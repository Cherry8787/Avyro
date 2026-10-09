# meal_planner.py
import random
from food_db import FOOD_DATABASE

PREP_MAPPING = {
    "a": "Fresh cooking",
    "b": "Assembly-only",
    "c": "Restaurant / Takeout",
    "d": "Grocery grab & go"
}

def generate_daily_meal_plan(prep_pref="a", previous_meal_plan=None):
    if previous_meal_plan is None:
        previous_meal_plan = {}

    target_prep_type = PREP_MAPPING.get(prep_pref, "Fresh cooking")
    daily_plan = {}

    for slot, available_options in FOOD_DATABASE.items():
        # Filter items matching the user's selected prep preference
        filtered_options = [
            item for item in available_options
            if item.get("prep_type") == target_prep_type
        ]

        # If no items match the preference for this slot, fall back to all items
        valid_options = filtered_options if filtered_options else list(available_options)

        # Avoid picking the exact same meal as yesterday if possible
        if slot in previous_meal_plan and len(valid_options) > 1:
            yesterday_meal = previous_meal_plan[slot]["name"]
            valid_options = [item for item in valid_options if item["name"] != yesterday_meal]

        # Pick a random meal option
        chosen_item = random.choice(valid_options).copy()

        # OVERRIDE LINK FOR TAKEOUT PREFERENCE ("c")
        # If user selected takeout ("c"), force link to open a restaurant search on Google Maps
        if prep_pref == "c":
            meal_query = chosen_item['name'].replace(' ', '+')
            chosen_item["link"] = f"https://www.google.com/maps/search/{meal_query}+Restaurants+Near+Me"

        daily_plan[slot] = chosen_item

    return daily_plan