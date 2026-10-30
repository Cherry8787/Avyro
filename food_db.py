# ==========================================
# FILE: food_db.py
# DESCRIPTION: Comprehensive structured database containing all meal options 
# mapped strictly to medical conditions (General Wellness, Diabetes, Thyroid, Blood Pressure) and prep styles.
# ==========================================

import random

FOOD_DATABASE = {
    "Breakfast": [
        # --- FRESH COOKING ---
        {
            "name": "Scrambled Eggs with Whole Wheat Toast",
            "calories": 400,
            "prep_type": "Fresh cooking",
            "condition": "General Wellness",
            "link": "https://www.bbcgoodfood.com/recipes/perfect-scrambled-eggs"
        },
        {
            "name": "Avocado Toast & Boiled Egg",
            "calories": 380,
            "prep_type": "Fresh cooking",
            "condition": "General Wellness",
            "link": "https://www.gimmesomeoven.com/avocado-toast-recipe/"
        },
        {
            "name": "Protein Pancake Stack with Maple Syrup",
            "calories": 480,
            "prep_type": "Fresh cooking",
            "condition": "General Wellness",
            "link": "https://www.eatwell101.com/protein-pancakes-recipe"
        },
        {
            "name": "Low-Sodium Spinach & Mushroom Egg White Omelette",
            "calories": 320,
            "prep_type": "Fresh cooking",
            "condition": "Blood Pressure",
            "link": "https://www.skinnytaste.com/spinach-and-feta-egg-white-omelet/"
        },
        {
            "name": "Classic Masala Dosa with Sambhar",
            "calories": 390,
            "prep_type": "Fresh cooking",
            "condition": "General Wellness",
            "link": "https://www.cookwithmanali.com/dosa-recipe/"
        },
        {
            "name": "High-Protein Tofu Scramble with Veggies",
            "calories": 360,
            "prep_type": "Fresh cooking",
            "condition": "Diabetes",
            "link": "https://minimalistbaker.com/switched-up-tofu-scramble/"
        },

        # --- ASSEMBLY-ONLY ---
        {
            "name": "Steel-Cut Oats with Cinnamon & Walnuts",
            "calories": 350,
            "prep_type": "Assembly-only",
            "condition": "Diabetes",
            "link": "https://www.allrecipes.com/recipe/245228/overnight-oats-with-berries/"
        },
        {
            "name": "Peanut Butter & Banana Chia Pudding",
            "calories": 370,
            "prep_type": "Assembly-only",
            "condition": "General Wellness",
            "link": "https://www.eatingwell.com/recipe/268388/peanut-butter-banana-chia-pudding/"
        },
        {
            "name": "Cottage Cheese & Honey Fruit Bowl",
            "calories": 310,
            "prep_type": "Assembly-only",
            "condition": "General Wellness",
            "link": "https://www.thepioneerwoman.com/food-cooking/recipes/a36224328/cottage-cheese-fruit-bowl/"
        },
        {
            "name": "Selenium-Rich Brazil Nut & Greek Yogurt Parfait",
            "calories": 340,
            "prep_type": "Assembly-only",
            "condition": "Thyroid",
            "link": "https://www.eatthis.com/greek-yogurt-granola-bowl/"
        },
        {
            "name": "Overnight Mango & Coconut Oats",
            "calories": 380,
            "prep_type": "Assembly-only",
            "condition": "General Wellness",
            "link": "https://www.loveandlemons.com/overnight-oats-recipe/"
        },

        # --- GROCERY GRAB & GO ---
        {
            "name": "Greek Yogurt Parfait with Honey",
            "calories": 300,
            "prep_type": "Grocery grab & go",
            "condition": "General Wellness",
            "link": "https://www.eatingwell.com/recipe/261623/easy-yogurt-parfait/"
        },
        {
            "name": "Ready-to-Drink High Protein Shake",
            "calories": 280,
            "prep_type": "Grocery grab & go",
            "condition": "General Wellness",
            "link": "https://www.healthline.com/nutrition/best-protein-shakes"
        },
        {
            "name": "Bakery Whole Grain Breakfast Muffin",
            "calories": 340,
            "prep_type": "Grocery grab & go",
            "condition": "General Wellness",
            "link": "https://www.sparkpeople.com/myspark/nutrition/ready_breakfast_muffins.asp"
        },
        {
            "name": "Store-Bought Hard Boiled Eggs & Protein Pack",
            "calories": 260,
            "prep_type": "Grocery grab & go",
            "condition": "General Wellness",
            "link": "https://www.eatthis.com/protein-snack-packs/"
        },

        # --- RESTAURANT / TAKEOUT ---
        {
            "name": "Cafe Breakfast Bagel & Coffee Combo",
            "calories": 420,
            "prep_type": "Restaurant / Takeout",
            "condition": "General Wellness",
            "link": "https://www.google.com/maps/search/Breakfast+Bagel+Cafe+Near+Me"
        },
        {
            "name": "Diner Omelette & Hashbrown Combo",
            "calories": 520,
            "prep_type": "Restaurant / Takeout",
            "condition": "General Wellness",
            "link": "https://www.google.com/maps/search/Diner+Breakfast+Omelette+Near+Me"
        },
        {
            "name": "South Indian Idli Sambhar Takeout",
            "calories": 330,
            "prep_type": "Restaurant / Takeout",
            "condition": "General Wellness",
            "link": "https://www.google.com/maps/search/South+Indian+Idli+Restaurant+Near+Me"
        }
    ],

    "Lunch": [
        # --- FRESH COOKING ---
        {
            "name": "Grilled Chicken & Rice Bowl",
            "calories": 550,
            "prep_type": "Fresh cooking",
            "condition": "General Wellness",
            "link": "https://www.budgetbytes.com/chicken-burrito-bowls/"
        },
        {
            "name": "DASH-Diet Herb Grilled Salmon & Asparagus",
            "calories": 520,
            "prep_type": "Fresh cooking",
            "condition": "Blood Pressure",
            "link": "https://www.cookingclassy.com/pan-seared-salmon-with-lemon-butter-pan-sauce/"
        },
        {
            "name": "Low-Glycemic Lentil Dal with Brown Rice",
            "calories": 480,
            "prep_type": "Fresh cooking",
            "condition": "Diabetes",
            "link": "https://www.thekitchn.com/how-to-make-lentil-dal-241517"
        },
        {
            "name": "Grilled Turkey Burger with Sweet Potato Wedges",
            "calories": 580,
            "prep_type": "Fresh cooking",
            "condition": "General Wellness",
            "link": "https://www.skinnytaste.com/turkey-burgers/"
        },

        # --- ASSEMBLY-ONLY ---
        {
            "name": "Iodine-Support Seaweed & Tofu Salad Bowl",
            "calories": 450,
            "prep_type": "Assembly-only",
            "condition": "Thyroid",
            "link": "https://www.skinnytaste.com/chickpea-avocado-salad/"
        },
        {
            "name": "Turkey, Avocado & Spinach Wrap",
            "calories": 460,
            "prep_type": "Assembly-only",
            "condition": "General Wellness",
            "link": "https://www.spendwithpennies.com/turkey-wrap/"
        },
        {
            "name": "Mediterranean Tuna & White Bean Salad",
            "calories": 430,
            "prep_type": "Assembly-only",
            "condition": "General Wellness",
            "link": "https://www.themediterraneandish.com/tuna-salad-recipe/"
        },
        {
            "name": "Smoked Salmon & Cream Cheese Bagel",
            "calories": 470,
            "prep_type": "Assembly-only",
            "condition": "General Wellness",
            "link": "https://www.epicurious.com/recipes/food/views/smoked-salmon-and-cream-cheese-bagel"
        },

        # --- GROCERY GRAB & GO ---
        {
            "name": "Readymade Quinoa & Veggie Bowl",
            "calories": 420,
            "prep_type": "Grocery grab & go",
            "condition": "General Wellness",
            "link": "https://www.loveandlemons.com/quinoa-salad/"
        },
        {
            "name": "Deli Protein Bento Box (Egg, Cheese, Fruit)",
            "calories": 440,
            "prep_type": "Grocery grab & go",
            "condition": "General Wellness",
            "link": "https://www.eatthis.com/healthy-snack-boxes/"
        },
        {
            "name": "Pre-Packaged Salmon Sushi Set",
            "calories": 490,
            "prep_type": "Grocery grab & go",
            "condition": "General Wellness",
            "link": "https://www.healthline.com/nutrition/is-sushi-healthy"
        },
        {
            "name": "Store-Bought Chicken Caesar Salad Bowl",
            "calories": 450,
            "prep_type": "Grocery grab & go",
            "condition": "General Wellness",
            "link": "https://www.eatthis.com/best-store-bought-salads/"
        },

        # --- RESTAURANT / TAKEOUT ---
        {
            "name": "Paneer Tikka Wrap",
            "calories": 500,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Paneer+Tikka+Wrap+Restaurants+Near+Me"
        },
        {
            "name": "Chipotle-Style Chicken Burrito Bowl",
            "calories": 620,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Burrito+Bowl+Restaurants+Near+Me"
        },
        {
            "name": "Artisan Bakery Club Sandwich",
            "calories": 540,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Sandwich+Cafe+Near+Me"
        },
        {
            "name": "Japanese Teriyaki Chicken Rice Bowl",
            "calories": 580,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Teriyaki+Chicken+Bowl+Near+Me"
        }
    ],

    "Snacks": [
        # --- FRESH COOKING ---
        {
            "name": "Air-Fried Sweet Potato Wedges",
            "calories": 230,
            "prep_type": "Fresh cooking",
            "link": "https://www.gimmesomeoven.com/baked-sweet-potato-fries/"
        },
        {
            "name": "Crispy Baked Garlic Parmesan Chickpeas",
            "calories": 210,
            "prep_type": "Fresh cooking",
            "link": "https://www.delish.com/cooking/recipe-ideas/a28629233/roasted-chickpeas-recipe/"
        },

        # --- ASSEMBLY-ONLY ---
        {
            "name": "Roasted Pumpkin Seeds & Cinnamon Apple Slices",
            "calories": 220,
            "prep_type": "Assembly-only",
            "condition": "Thyroid",
            "link": "https://www.eatingwell.com/recipe/250269/apple-with-peanut-butter/"
        },
        {
            "name": "Low-Sodium Hummus with Carrot Sticks & Pita",
            "calories": 240,
            "prep_type": "Assembly-only",
            "condition": "Blood Pressure",
            "link": "https://www.inspiredtaste.net/15938/easy-smooth-hummus-recipe/"
        },
        {
            "name": "Guacamole with Whole Grain Tortilla Chips",
            "calories": 260,
            "prep_type": "Assembly-only",
            "link": "https://www.downshiftology.com/recipes/best-ever-guacamole/"
        },

        # --- GROCERY GRAB & GO ---
        {
            "name": "Mixed Nuts & Dark Chocolate",
            "calories": 200,
            "prep_type": "Grocery grab & go",
            "condition": "General Wellness",
            "link": "https://www.healthline.com/nutrition/healthy-nuts"
        },
        {
            "name": "High-Protein Energy Bar & Almonds",
            "calories": 250,
            "prep_type": "Grocery grab & go",
            "link": "https://www.eatthis.com/best-protein-bars/"
        },
        {
            "name": "Cinnamon Spiced Roasted Chickpeas Snack Pack",
            "calories": 210,
            "prep_type": "Grocery grab & go",
            "condition": "Diabetes",
            "link": "https://www.healthline.com/nutrition/roasted-chickpeas"
        },
        {
            "name": "Low-Fat String Cheese & Whole Grain Crackers",
            "calories": 180,
            "prep_type": "Grocery grab & go",
            "link": "https://www.verywellfit.com/healthy-cheese-snacks-4161102"
        },

        # --- RESTAURANT / TAKEOUT ---
        {
            "name": "Fresh Smoothie / Juice Bar Special",
            "calories": 230,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Juice+Bar+Smoothie+Near+Me"
        },
        {
            "name": "Artisan Espresso & Almond Croissant",
            "calories": 310,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Bakery+Cafe+Near+Me"
        }
    ],

    "Dinner": [
        # --- FRESH COOKING ---
        {
            "name": "Baked Salmon with Roasted Vegetables",
            "calories": 600,
            "prep_type": "Fresh cooking",
            "condition": "General Wellness",
            "link": "https://www.delish.com/cooking/recipe-ideas/a22510250/sheet-pan-salmon-recipe/"
        },
        {
            "name": "Low-Carb Tofu & Leafy Greens Stir-Fry",
            "calories": 500,
            "prep_type": "Fresh cooking",
            "condition": "Diabetes",
            "link": "https://minimalistbaker.com/crispy-peanut-tofu-stir-fry/"
        },
        {
            "name": "Potassium-Rich Roasted Turkey & Sweet Potato Mash",
            "calories": 650,
            "prep_type": "Fresh cooking",
            "condition": "Blood Pressure",
            "link": "https://www.cafedelites.com/garlic-butter-steak-steaks/"
        },
        {
            "name": "Shrimp & Asparagus Lemon Pasta",
            "calories": 530,
            "prep_type": "Fresh cooking",
            "link": "https://www.cookingclassy.com/lemon-garlic-butter-shrimp-pasta/"
        },

        # --- ASSEMBLY-ONLY ---
        {
            "name": "Lentil Soup with Multigrain Roll",
            "calories": 460,
            "prep_type": "Assembly-only",
            "link": "https://www.cookieandkate.com/best-lentil-soup-recipe/"
        },
        {
            "name": "Zinc-Boosted Mediterranean Couscous & Feta Bowl",
            "calories": 480,
            "prep_type": "Assembly-only",
            "condition": "Thyroid",
            "link": "https://www.mediterraneanliving.com/mediterranean-couscous-bowl/"
        },
        {
            "name": "Caprese Pita Pocket with Pesto",
            "calories": 440,
            "prep_type": "Assembly-only",
            "link": "https://www.eatingwell.com/recipe/251348/caprese-pita-pockets/"
        },

        # --- GROCERY GRAB & GO ---
        {
            "name": "Rotisserie Chicken & Salad Meal Kit",
            "calories": 550,
            "prep_type": "Grocery grab & go",
            "link": "https://www.eatthis.com/rotisserie-chicken-meals/"
        },
        {
            "name": "Pre-Made Tortellini with Marinara Sauce",
            "calories": 510,
            "prep_type": "Grocery grab & go",
            "link": "https://www.verywellfit.com/store-bought-pasta-guide"
        },
        {
            "name": "Store-Bought Creamy Tomato Soup & Grilled Cheese",
            "calories": 520,
            "prep_type": "Grocery grab & go",
            "link": "https://www.eatthis.com/best-canned-soups/"
        },

        # --- RESTAURANT / TAKEOUT ---
        {
            "name": "Store-Bought Whole Wheat Veggie Pizza",
            "calories": 580,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Veggie+Pizza+Restaurants+Near+Me"
        },
        {
            "name": "Authentic Indian Curry & Garlic Naan",
            "calories": 640,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Indian+Restaurant+Curry+Near+Me"
        },
        {
            "name": "Thai Basil Chicken & Jasmine Rice",
            "calories": 590,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Thai+Restaurant+Near+Me"
        },
        {
            "name": "Greek Gyro Platter with Rice & Tzatziki",
            "calories": 610,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Greek+Gyro+Restaurant+Near+Me"
        }
    ]
}


def generate_daily_meal_plan(prep_pref="a", medical_condition="General Wellness", previous_meal_plan=None):
    """
    Generates daily meal plans strictly filtered by the user's selected medical condition 
    to ensure personalized condition-based dining.
    """
    if previous_meal_plan is None:
        previous_meal_plan = {}

    PREP_MAPPING = {
        "a": "Fresh cooking",
        "b": "Assembly-only",
        "c": "Restaurant / Takeout",
        "d": "Grocery grab & go"
    }
    target_prep_type = PREP_MAPPING.get(prep_pref, "Fresh cooking")
    daily_plan = {}

    for slot, available_options in FOOD_DATABASE.items():
        condition_filtered = [
            item for item in available_options
            if item.get("condition", "").lower() == medical_condition.lower()
        ]

        if not condition_filtered:
            condition_filtered = [item for item in available_options if item.get("condition") == "General Wellness"]

        filtered_options = [
            item for item in condition_filtered
            if item.get("prep_type") == target_prep_type
        ]

        valid_options = filtered_options if filtered_options else condition_filtered

        if slot in previous_meal_plan and len(valid_options) > 1:
            yesterday_meal = previous_meal_plan[slot]["name"]
            valid_options = [item for item in valid_options if item["name"] != yesterday_meal]

        chosen_item = random.choice(valid_options).copy()

        if prep_pref == "c":
            meal_query = chosen_item['name'].replace(' ', '+')
            chosen_item["link"] = f"https://www.google.com/maps/search/{meal_query}+Restaurants+Near+Me"

        daily_plan[slot] = chosen_item

    return daily_plan