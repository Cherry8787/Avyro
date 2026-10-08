# main.py

import webbrowser
import customtkinter as ctk

from calorie_calc import (
    calculate_bmi,
    calculate_bmr,
    calculate_tdee,
    get_meal_calorie_split,
    get_target_calories,
)
from food_db import FOOD_DATABASE
from meal_planner import generate_daily_meal_plan

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class AvyroApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Avyro - Eat. Move. Evolve.")
        self.geometry("550x720")
        self.resizable(False, False)

        self.user_data = {
            "name": "",
            "email": "",
            "age": 20,
            "gender": "Male",
            "height": 170.0,
            "weight": 65.0,
            "target": "Maintenance",
            "activity": "moderate",
            "outside_freq": "a",
            "prep_pref": "a",
            "selected_foods": [],
        }

        self.previous_meal_plan = {}

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.show_window_1_registration()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # ==========================================
    # WINDOW 1: Registration
    # ==========================================
    def show_window_1_registration(self):
        self.clear_container()

        ctk.CTkLabel(
            self.container,
            text="Avyro",
            font=ctk.CTkFont(size=30, weight="bold"),
        ).pack(pady=(20, 5))
        ctk.CTkLabel(
            self.container,
            text="Eat. Move. Evolve.",
            font=ctk.CTkFont(size=14, slant="italic"),
        ).pack(pady=(0, 20))

        frame = ctk.CTkFrame(self.container)
        frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            frame,
            text="Welcome! Let's get started.",
            font=ctk.CTkFont(size=16, weight="bold"),
        ).pack(pady=15)

        self.entry_name = ctk.CTkEntry(
            frame, placeholder_text="Full Name", width=300
        )
        self.entry_name.pack(pady=10)

        self.entry_email = ctk.CTkEntry(
            frame, placeholder_text="Email or Phone Number", width=300
        )
        self.entry_email.pack(pady=10)

        ctk.CTkButton(
            self.container,
            text="Next Step ➔",
            width=200,
            height=40,
            command=self.save_w1_and_next,
        ).pack(pady=30)

    def save_w1_and_next(self):
        self.user_data["name"] = self.entry_name.get().strip() or "User"
        self.user_data["email"] = self.entry_email.get().strip()
        self.show_window_2_metrics()

    # ==========================================
    # WINDOW 2: Physical Metrics
    # ==========================================
    def show_window_2_metrics(self):
        self.clear_container()

        ctk.CTkLabel(
            self.container,
            text="Physical Metrics",
            font=ctk.CTkFont(size=22, weight="bold"),
        ).pack(pady=(15, 15))

        ctk.CTkLabel(self.container, text="Age (years):").pack(anchor="w", padx=40)
        self.entry_age = ctk.CTkEntry(self.container, width=300)
        self.entry_age.insert(0, "20")
        self.entry_age.pack(pady=(0, 10))

        ctk.CTkLabel(self.container, text="Gender:").pack(anchor="w", padx=40)
        self.gender_var = ctk.StringVar(value="Male")
        ctk.CTkSegmentedButton(
            self.container,
            values=["Male", "Female"],
            variable=self.gender_var,
            width=300,
        ).pack(pady=(0, 10))

        ctk.CTkLabel(self.container, text="Height (cm):").pack(
            anchor="w", padx=40
        )
        self.entry_height = ctk.CTkEntry(self.container, width=300)
        self.entry_height.insert(0, "170")
        self.entry_height.pack(pady=(0, 10))

        ctk.CTkLabel(self.container, text="Weight (kg):").pack(
            anchor="w", padx=40
        )
        self.entry_weight = ctk.CTkEntry(self.container, width=300)
        self.entry_weight.insert(0, "65")
        self.entry_weight.pack(pady=(0, 10))

        ctk.CTkLabel(self.container, text="Your Target Goal:").pack(
            anchor="w", padx=40
        )
        self.target_var = ctk.StringVar(value="Maintain Weight")
        ctk.CTkOptionMenu(
            self.container,
            values=["Weight Loss", "Maintain Weight", "Weight Gain"],
            variable=self.target_var,
            width=300,
        ).pack(pady=(0, 15))

        ctk.CTkButton(
            self.container,
            text="Continue ➔",
            width=200,
            height=40,
            command=self.save_w2_and_next,
        ).pack(pady=15)

    def save_w2_and_next(self):
        try:
            self.user_data["age"] = int(self.entry_age.get())
            self.user_data["gender"] = self.gender_var.get()
            self.user_data["height"] = float(self.entry_height.get())
            self.user_data["weight"] = float(self.entry_weight.get())
            self.user_data["target"] = self.target_var.get()
        except ValueError:
            pass

        self.show_window_3_questionnaire()

    # ==========================================
    # WINDOW 3: Questionnaire
    # ==========================================
    def show_window_3_questionnaire(self):
        self.clear_container()

        ctk.CTkLabel(
            self.container,
            text="Lifestyle Questionnaire",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(pady=(10, 15))

        ctk.CTkLabel(
            self.container, text="1. Daily Activity / Workout Frequency:"
        ).pack(anchor="w", padx=30)
        self.activity_var = ctk.StringVar(value="moderate")
        ctk.CTkOptionMenu(
            self.container,
            values=["sedentary", "light", "moderate", "active", "N/A"],
            variable=self.activity_var,
            width=300,
        ).pack(pady=(0, 15))

        ctk.CTkLabel(
            self.container, text="2. How is your energy/mood today?"
        ).pack(anchor="w", padx=30)
        self.mood_var = ctk.StringVar(value="Energetic")
        ctk.CTkOptionMenu(
            self.container,
            values=["Energetic", "Normal", "Tired", "Stressed"],
            variable=self.mood_var,
            width=300,
        ).pack(pady=(0, 15))

        ctk.CTkLabel(
            self.container, text="3. How often do you eat outside?"
        ).pack(anchor="w", padx=30)
        self.outside_var = ctk.StringVar(value="a) Once a week")
        ctk.CTkOptionMenu(
            self.container,
            values=[
                "a) Once a week",
                "b) Twice/Thrice a week",
                "c) Four times a week",
                "d) 5+ times a week",
            ],
            variable=self.outside_var,
            width=300,
        ).pack(pady=(0, 20))

        ctk.CTkButton(
            self.container,
            text="Next Step ➔",
            width=200,
            height=40,
            command=self.save_w3_and_next,
        ).pack(pady=10)

    def save_w3_and_next(self):
        self.user_data["activity"] = self.activity_var.get()
        self.user_data["outside_freq"] = self.outside_var.get()[0]
        self.show_window_4_meal_prep()

    # ==========================================
    # WINDOW 4: Meal Prep Style
    # ==========================================
    def show_window_4_meal_prep(self):
        self.clear_container()

        ctk.CTkLabel(
            self.container,
            text="Meal Preparation Style",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(pady=(15, 10))

        ctk.CTkLabel(
            self.container,
            text="How do you prefer to get your meals mostly?",
            font=ctk.CTkFont(size=13),
        ).pack(pady=(0, 15))

        self.prep_var = ctk.StringVar(value="a")

        opts = [
            ("a) Fresh cooking", "a"),
            ("b) No-cook / Assembly only", "b"),
            ("c) Meal delivery / Takeout", "c"),
            ("d) Grocery store grab & go", "d"),
        ]

        for text, val in opts:
            ctk.CTkRadioButton(
                self.container,
                text=text,
                value=val,
                variable=self.prep_var,
            ).pack(anchor="w", padx=50, pady=10)

        ctk.CTkButton(
            self.container,
            text="Select Food Options ➔",
            width=200,
            height=40,
            command=self.save_w4_and_next,
        ).pack(pady=30)

    def save_w4_and_next(self):
        self.user_data["prep_pref"] = self.prep_var.get()
        self.show_window_5_food_selection()

    # ==========================================
    # WINDOW 5: Food Preferences Checklist (NEW)
    # ==========================================
    def show_window_5_food_selection(self):
        self.clear_container()

        ctk.CTkLabel(
            self.container,
            text="Preferred Food Options",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            self.container,
            text="Check the items you enjoy eating:",
            font=ctk.CTkFont(size=12),
        ).pack(pady=(0, 10))

        # Scrollable area for checkable food items
        scroll_frame = ctk.CTkScrollableFrame(
            self.container, width=450, height=380
        )
        scroll_frame.pack(pady=10)

        self.checkbox_vars = {}

        for category, items in FOOD_DATABASE.items():
            cat_label = ctk.CTkLabel(
                scroll_frame,
                text=f"--- {category} ---",
                font=ctk.CTkFont(size=14, weight="bold"),
            )
            cat_label.pack(anchor="w", pady=(10, 5))

            for food in items:
                var = ctk.BooleanVar(value=True)  # Default checked
                chk = ctk.CTkCheckBox(
                    scroll_frame, text=food["name"], variable=var
                )
                chk.pack(anchor="w", padx=20, pady=3)
                self.checkbox_vars[food["name"]] = var

        ctk.CTkButton(
            self.container,
            text="Generate Meal Plan ➔",
            width=200,
            height=40,
            command=self.save_w5_and_next,
        ).pack(pady=15)

    def save_w5_and_next(self):
        # Store user's checked foods
        selected = [
            name for name, var in self.checkbox_vars.items() if var.get()
        ]
        self.user_data["selected_foods"] = selected
        self.show_window_6_daily_plan()

    # ==========================================
    # WINDOW 6: Daily Meal Plan Display
    # ==========================================
    def show_window_6_daily_plan(self):
        self.clear_container()

        bmi, bmi_cat = calculate_bmi(
            self.user_data["weight"], self.user_data["height"]
        )
        bmr = calculate_bmr(
            self.user_data["gender"],
            self.user_data["weight"],
            self.user_data["height"],
            self.user_data["age"],
        )
        tdee = calculate_tdee(bmr, self.user_data["activity"])
        target_cal = get_target_calories(tdee, self.user_data["target"])
        split = get_meal_calorie_split(target_cal)

        meal_plan = generate_daily_meal_plan(
            self.user_data["prep_pref"], self.previous_meal_plan
        )
        self.previous_meal_plan = meal_plan

        header_text = f"Hello, {self.user_data['name']}! | BMI: {bmi} ({bmi_cat})\nTarget Calories: {target_cal} kcal/day"
        ctk.CTkLabel(
            self.container,
            text=header_text,
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(pady=(5, 10))

        schedule_frame = ctk.CTkFrame(self.container, fg_color="#2b2b2b")
        schedule_frame.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(
            schedule_frame,
            text="⏰ Recommended Timings: Wake Up: 07:00 AM | Sleep: 10:30 PM",
            font=ctk.CTkFont(size=11),
        ).pack(pady=5)

        slots = [
            ("B - Breakfast", "08:30 AM", "Breakfast"),
            ("L - Lunch", "01:30 PM", "Lunch"),
            ("S - Snacks", "05:00 PM", "Snacks"),
            ("D - Dinner", "08:00 PM", "Dinner"),
        ]

        for code, time, slot_key in slots:
            item = meal_plan[slot_key]
            slot_frame = ctk.CTkFrame(self.container)
            slot_frame.pack(fill="x", padx=10, pady=4)

            left_text = f"{code} ({time}):\n{item['name']}"
            ctk.CTkLabel(
                slot_frame,
                text=left_text,
                justify="left",
                font=ctk.CTkFont(size=12, weight="bold"),
            ).pack(side="left", padx=10, pady=5)

            right_text = f"~{item['calories']} kcal\n(Goal: {split[slot_key]})"
            ctk.CTkLabel(
                slot_frame,
                text=right_text,
                justify="right",
                font=ctk.CTkFont(size=11),
            ).pack(side="right", padx=10, pady=5)

            ctk.CTkButton(
                slot_frame,
                text="🔗 Recipe",
                width=70,
                height=24,
                font=ctk.CTkFont(size=10),
                command=lambda url=item["link"]: webbrowser.open(url),
            ).pack(side="right", padx=5)

        ctk.CTkButton(
            self.container,
            text="🔄 Regenerate Plan (No Consecutive Repeats)",
            width=250,
            height=35,
            command=self.show_window_6_daily_plan,
        ).pack(pady=15)


if __name__ == "__main__":
    app = AvyroApp()
    app.mainloop()