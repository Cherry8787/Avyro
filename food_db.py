# food_db.py

# Meal Prep Categories:
# "Fresh cooking"
# "Assembly-only"
# "Restaurant / Takeout"
# "Grocery grab & go"

FOOD_DATABASE = {
    "Breakfast": [
        # --- FRESH COOKING ---
        {
            "name": "Scrambled Eggs with Whole Wheat Toast",
            "calories": 400,
            "prep_type": "Fresh cooking",
            "link": "https://www.bbcgoodfood.com/recipes/perfect-scrambled-eggs"
        },
        {
            "name": "Avocado Toast & Boiled Egg",
            "calories": 380,
            "prep_type": "Fresh cooking",
            "link": "https://www.gimmesomeoven.com/avocado-toast-recipe/"
        },
        {
            "name": "Protein Pancake Stack with Maple Syrup",
            "calories": 480,
            "prep_type": "Fresh cooking",
            "link": "https://www.eatwell101.com/protein-pancakes-recipe"
        },
        {
            "name": "Spinach & Mushroom Egg White Omelette",
            "calories": 320,
            "prep_type": "Fresh cooking",
            "link": "https://www.skinnytaste.com/spinach-and-feta-egg-white-omelet/"
        },
        {
            "name": "Classic Masala Dosa with Sambhar",
            "calories": 390,
            "prep_type": "Fresh cooking",
            "link": "https://www.cookwithmanali.com/dosa-recipe/"
        },
        {
            "name": "High-Protein Tofu Scramble with Veggies",
            "calories": 360,
            "prep_type": "Fresh cooking",
            "link": "https://minimalistbaker.com/switched-up-tofu-scramble/"
        },

        # --- ASSEMBLY-ONLY ---
        {
            "name": "Oatmeal with Almonds & Berries",
            "calories": 350,
            "prep_type": "Assembly-only",
            "link": "https://www.allrecipes.com/recipe/245228/overnight-oats-with-berries/"
        },
        {
            "name": "Peanut Butter & Banana Chia Pudding",
            "calories": 370,
            "prep_type": "Assembly-only",
            "link": "https://www.eatingwell.com/recipe/268388/peanut-butter-banana-chia-pudding/"
        },
        {
            "name": "Cottage Cheese & Honey Fruit Bowl",
            "calories": 310,
            "prep_type": "Assembly-only",
            "link": "https://www.thepioneerwoman.com/food-cooking/recipes/a36224328/cottage-cheese-fruit-bowl/"
        },
        {
            "name": "Greek Yogurt Bowl with Granola & Flaxseeds",
            "calories": 340,
            "prep_type": "Assembly-only",
            "link": "https://www.eatthis.com/greek-yogurt-granola-bowl/"
        },
        {
            "name": "Overnight Mango & Coconut Oats",
            "calories": 380,
            "prep_type": "Assembly-only",
            "link": "https://www.loveandlemons.com/overnight-oats-recipe/"
        },

        # --- GROCERY GRAB & GO ---
        {
            "name": "Greek Yogurt Parfait with Honey",
            "calories": 300,
            "prep_type": "Grocery grab & go",
            "link": "https://www.eatingwell.com/recipe/261623/easy-yogurt-parfait/"
        },
        {
            "name": "Ready-to-Drink High Protein Shake",
            "calories": 280,
            "prep_type": "Grocery grab & go",
            "link": "https://www.healthline.com/nutrition/best-protein-shakes"
        },
        {
            "name": "Bakery Whole Grain Breakfast Muffin",
            "calories": 340,
            "prep_type": "Grocery grab & go",
            "link": "https://www.sparkpeople.com/myspark/nutrition/ready_breakfast_muffins.asp"
        },
        {
            "name": "Store-Bought Hard Boiled Eggs & Protein Pack",
            "calories": 260,
            "prep_type": "Grocery grab & go",
            "link": "https://www.eatthis.com/protein-snack-packs/"
        },

        # --- RESTAURANT / TAKEOUT ---
        {
            "name": "Cafe Breakfast Bagel & Coffee Combo",
            "calories": 420,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Breakfast+Bagel+Cafe+Near+Me"
        },
        {
            "name": "Diner Omelette & Hashbrown Combo",
            "calories": 520,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/Diner+Breakfast+Omelette+Near+Me"
        },
        {
            "name": "South Indian Idli Sambhar Takeout",
            "calories": 330,
            "prep_type": "Restaurant / Takeout",
            "link": "https://www.google.com/maps/search/South+Indian+Idli+Restaurant+Near+Me"
        }
    ],

    "Lunch": [
        # --- FRESH COOKING ---
        {
            "name": "Grilled Chicken & Rice Bowl",
            "calories": 550,
            "prep_type": "Fresh cooking",
            "link": "https://www.budgetbytes.com/chicken-burrito-bowls/"
        },
        {
            "name": "Pan-Seared Salmon & Quinoa Salad",
            "calories": 520,
            "prep_type": "Fresh cooking",
            "link": "https://www.cookingclassy.com/pan-seared-salmon-with-lemon-butter-pan-sauce/"
        },
        {
            "name": "Lentil Curry (Dal) with Brown Rice",
            "calories": 480,
            "prep_type": "Fresh cooking",
            "link": "https://www.thekitchn.com/how-to-make-lentil-dal-241517"
        },
        {
            "name": "Grilled Turkey Burger with Sweet Potato Wedges",
            "calories": 580,
            "prep_type": "Fresh cooking",
            "link": "https://www.skinnytaste.com/turkey-burgers/"
        },

        # --- ASSEMBLY-ONLY ---
        {
            "name": "Chickpea & Avocado Salad",
            "calories": 450,
            "prep_type": "Assembly-only",
            "link": "https://www.skinnytaste.com/chickpea-avocado-salad/"
        },
        {
            "name": "Turkey, Avocado & Spinach Wrap",
            "calories": 460,
            "prep_type": "Assembly-only",
            "link": "https://www.spendwithpennies.com/turkey-wrap/"
        },
        {
            "name": "Mediterranean Tuna & White Bean Salad",
            "calories": 430,
            "prep_type": "Assembly-only",
            "link": "https://www.themediterraneandish.com/tuna-salad-recipe/"
        },
        {
            "name": "Smoked Salmon & Cream Cheese Bagel",
            "calories": 470,
            "prep_type": "Assembly-only",
            "link": "https://www.epicurious.com/recipes/food/views/smoked-salmon-and-cream-cheese-bagel"
        },

        # --- GROCERY GRAB & GO ---
        {
            "name": "Readymade Quinoa & Veggie Bowl",
            "calories": 420,
            "prep_type": "Grocery grab & go",
            "link": "https://www.loveandlemons.com/quinoa-salad/"
        },
        {
            "name": "Deli Protein Bento Box (Egg, Cheese, Fruit)",
            "calories": 440,
            "prep_type": "Grocery grab & go",
            "link": "https://www.eatthis.com/healthy-snack-boxes/"
        },
        {
            "name": "Pre-Packaged Salmon Sushi Set",
            "calories": 490,
            "prep_type": "Grocery grab & go",
            "link": "https://www.healthline.com/nutrition/is-sushi-healthy"
        },
        {
            "name": "Store-Bought Chicken Caesar Salad Bowl",
            "calories": 450,
            "prep_type": "Grocery grab & go",
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
            "name": "Apple Slices with Peanut Butter",
            "calories": 220,
            "prep_type": "Assembly-only",
            "link": "https://www.eatingwell.com/recipe/250269/apple-with-peanut-butter/"
        },
        {
            "name": "Hummus with Carrot Sticks & Pita",
            "calories": 240,
            "prep_type": "Assembly-only",
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
            "link": "https://www.healthline.com/nutrition/healthy-nuts"
        },
        {
            "name": "High-Protein Energy Bar & Almonds",
            "calories": 250,
            "prep_type": "Grocery grab & go",
            "link": "https://www.eatthis.com/best-protein-bars/"
        },
        {
            "name": "Roasted Chickpeas Snack Pack",
            "calories": 210,
            "prep_type": "Grocery grab & go",
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
            "link": "https://www.delish.com/cooking/recipe-ideas/a22510250/sheet-pan-salmon-recipe/"
        },
        {
            "name": "Tofu & Stir-Fry Veggies with Rice",
            "calories": 500,
            "prep_type": "Fresh cooking",
            "link": "https://minimalistbaker.com/crispy-peanut-tofu-stir-fry/"
        },
        {
            "name": "Grilled Steak & Garlic Mashed Potatoes",
            "calories": 650,
            "prep_type": "Fresh cooking",
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
            "name": "Mediterranean Couscous & Feta Bowl",
            "calories": 480,
            "prep_type": "Assembly-only",
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