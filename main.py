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

# Application Theme Configuration
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# --- LUXURY BLACK & GOLD PALETTE ---
BG_DARK = "#090A0F"          # Deep Matte Obsidian
CARD_BG = "#12141C"          # Midnight Card Surface
BORDER_GOLD = "#D4AF37"      # Metallic Warm Gold
GOLD_PRIMARY = "#E5C158"     # Bright Premium Gold
GOLD_HOVER = "#C59827"       # Darker Gold for Hover States
TEXT_WHITE = "#FFFFFF"       # Primary Pure White Text
TEXT_GOLD = "#F3E5AB"        # Subtle Champagne Gold Accent
SUBTEXT_MUTED = "#8A8F9E"    # Premium Muted Gray
CARD_INNER_BG = "#1A1D28"    # Contrast Inner Slot Card

# --- SLEEK TYPOGRAPHY & CALLIGRAPHY STYLES ---
FONT_TITLE = ("Cinzel", "Georgia")           # Calligraphic/Serif Luxury Titles
FONT_SERIF = ("Georgia", "Baskerville")      # Elegant Calligraphic Subtitles & Headers
FONT_BODY = ("Segoe UI", "Helvetica")        # Clean Sans-Serif for readable inputs


class AvyroApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AVYRO - Exclusive Nutrition & Wellness")
        self.geometry("540x820")
        self.resizable(False, False)
        self.configure(fg_color=BG_DARK)

        self.user_data = {
            "name": "",
            "email": "",
            "age": 20,
            "gender": "Male",
            "height": 170.0,
            "weight": 65.0,
            "target": "Maintain Weight",
            "activity": "moderate",
            "outside_freq": "a",
            "prep_pref": "a",
            "selected_foods": []
        }

        self.previous_meal_plan = {}

        # Main Scrollable Container
        self.container = ctk.CTkScrollableFrame(
            self,
            fg_color=BG_DARK,
            corner_radius=0
        )
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.show_window_1_registration()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def add_contact_us_footer(self):
        """Adds a sleek, calligraphic 'Contact Us' footer at the end of every page."""
        footer_card = ctk.CTkFrame(
            self.container,
            fg_color=CARD_BG,
            corner_radius=14,
            border_width=1,
            border_color="#2D291E"
        )
        footer_card.pack(fill="x", pady=(20, 10), ipadx=10, ipady=12)

        ctk.CTkLabel(
            footer_card,
            text="- CONTACT US -",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            text_color=GOLD_PRIMARY
        ).pack(pady=(2, 4))

        ctk.CTkLabel(
            footer_card,
            text="📞 +1 (800) 555-AVYRO  |  ✉ support@avyro.com",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11),
            text_color=TEXT_GOLD
        ).pack(pady=(0, 2))

        ctk.CTkLabel(
            footer_card,
            text="Avyro Concierge Wellness • Available 24/7 for Members",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=10, slant="italic"),
            text_color=SUBTEXT_MUTED
        ).pack(pady=(0, 2))

    # ==================================================
    # WINDOW 1: Registration
    # ==================================================
    def show_window_1_registration(self):
        self.clear_container()

        # Header Branding Card
        header_card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=18, border_width=1, border_color=BORDER_GOLD)
        header_card.pack(fill="x", pady=(0, 20), ipady=18)

        ctk.CTkLabel(
            header_card, text="AVYRO",
            font=ctk.CTkFont(family=FONT_TITLE[0], size=38, weight="bold"),
            text_color=GOLD_PRIMARY
        ).pack(pady=(12, 2))

        ctk.CTkLabel(
            header_card, text="E A T  •  M O V E  •  E V O L V E",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold", slant="italic"),
            text_color=TEXT_GOLD
        ).pack(pady=(0, 8))

        # Registration Card
        card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=18, border_width=1, border_color=BORDER_GOLD)
        card.pack(fill="x", pady=10, ipadx=15, ipady=20)

        ctk.CTkLabel(
            card, text="WELCOME TO AVYRO",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=17, weight="bold"),
            text_color=TEXT_WHITE
        ).pack(pady=(5, 18))

        ctk.CTkLabel(card, text="FULL NAME", font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_name = ctk.CTkEntry(
            card, placeholder_text="Enter your full name", width=400, height=42,
            corner_radius=10, fg_color=CARD_INNER_BG, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE,
            font=ctk.CTkFont(family=FONT_BODY[0], size=12)
        )
        self.entry_name.pack(pady=(4, 16))

        ctk.CTkLabel(card, text="EMAIL OR PHONE", font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_email = ctk.CTkEntry(
            card, placeholder_text="Enter email or phone number", width=400, height=42,
            corner_radius=10, fg_color=CARD_INNER_BG, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE,
            font=ctk.CTkFont(family=FONT_BODY[0], size=12)
        )
        self.entry_email.pack(pady=(4, 24))

        ctk.CTkButton(
            card, text="BEGIN MEMBERSHIP ➔", width=400, height=46,
            corner_radius=10, fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER,
            text_color="#000000", font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            command=self.save_w1_and_next
        ).pack(pady=10)

        self.add_contact_us_footer()

    def save_w1_and_next(self):
        self.user_data["name"] = self.entry_name.get().strip() or "User"
        self.user_data["email"] = self.entry_email.get().strip()
        self.show_window_2_metrics()

    # ==================================================
    # WINDOW 2: Physical Metrics
    # ==================================================
    def show_window_2_metrics(self):
        self.clear_container()

        card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=18, border_width=1, border_color=BORDER_GOLD)
        card.pack(fill="x", pady=10, ipadx=15, ipady=20)

        ctk.CTkLabel(card, text="BODY METRICS & PROFILE", font=ctk.CTkFont(family=FONT_SERIF[0], size=16, weight="bold"), text_color=TEXT_WHITE).pack(pady=(5, 18))

        # Age
        ctk.CTkLabel(card, text="AGE (YEARS)", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_age = ctk.CTkEntry(card, width=400, height=40, corner_radius=8, fg_color=CARD_INNER_BG, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE)
        self.entry_age.insert(0, "20")
        self.entry_age.pack(pady=(4, 14))

        # Gender
        ctk.CTkLabel(card, text="GENDER", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.gender_var = ctk.StringVar(value="Male")
        ctk.CTkSegmentedButton(
            card, values=["Male", "Female"], variable=self.gender_var,
            width=400, height=38, selected_color=GOLD_PRIMARY, selected_hover_color=GOLD_HOVER,
            unselected_color=CARD_INNER_BG, text_color=TEXT_WHITE, font=ctk.CTkFont(family=FONT_SERIF[0], size=11)
        ).pack(pady=(4, 14))

        # Height
        ctk.CTkLabel(card, text="HEIGHT (CM)", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_height = ctk.CTkEntry(card, width=400, height=40, corner_radius=8, fg_color=CARD_INNER_BG, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE)
        self.entry_height.insert(0, "170")
        self.entry_height.pack(pady=(4, 14))

        # Weight
        ctk.CTkLabel(card, text="WEIGHT (KG)", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_weight = ctk.CTkEntry(card, width=400, height=40, corner_radius=8, fg_color=CARD_INNER_BG, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE)
        self.entry_weight.insert(0, "65")
        self.entry_weight.pack(pady=(4, 14))

        # Target Goal
        ctk.CTkLabel(card, text="PRIMARY GOAL", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.target_var = ctk.StringVar(value="Maintain Weight")
        ctk.CTkOptionMenu(
            card, values=["Weight Loss", "Maintain Weight", "Weight Gain"],
            variable=self.target_var, width=400, height=40, corner_radius=8,
            fg_color=CARD_INNER_BG, button_color=GOLD_PRIMARY, button_hover_color=GOLD_HOVER,
            text_color=TEXT_WHITE, dropdown_fg_color=CARD_BG, dropdown_hover_color="#2A2415",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12)
        ).pack(pady=(4, 24))

        ctk.CTkButton(
            card, text="SAVE & CONTINUE ➔", width=400, height=46, corner_radius=10,
            fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color="#000000",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            command=self.save_w2_and_next
        ).pack(pady=10)

        self.add_contact_us_footer()

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

    # ==================================================
    # WINDOW 3: Lifestyle Questionnaire
    # ==================================================
    def show_window_3_questionnaire(self):
        self.clear_container()

        card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=18, border_width=1, border_color=BORDER_GOLD)
        card.pack(fill="x", pady=10, ipadx=15, ipady=20)

        ctk.CTkLabel(card, text="LIFESTYLE ASSESSMENTS", font=ctk.CTkFont(family=FONT_SERIF[0], size=16, weight="bold"), text_color=TEXT_WHITE).pack(pady=(5, 18))

        # Q1 Activity
        ctk.CTkLabel(card, text="1. DAILY WORKOUT FREQUENCY", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.activity_var = ctk.StringVar(value="moderate")
        ctk.CTkOptionMenu(
            card, values=["sedentary", "light", "moderate", "active", "N/A"],
            variable=self.activity_var, width=400, height=40, corner_radius=8,
            fg_color=CARD_INNER_BG, button_color=GOLD_PRIMARY, button_hover_color=GOLD_HOVER,
            text_color=TEXT_WHITE, dropdown_fg_color=CARD_BG,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12)
        ).pack(pady=(4, 16))

        # Q2 Mood
        ctk.CTkLabel(card, text="2. DAILY ENERGY & MOOD", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.mood_var = ctk.StringVar(value="Energetic")
        ctk.CTkOptionMenu(
            card, values=["Energetic", "Normal", "Tired", "Stressed"],
            variable=self.mood_var, width=400, height=40, corner_radius=8,
            fg_color=CARD_INNER_BG, button_color=GOLD_PRIMARY, button_hover_color=GOLD_HOVER,
            text_color=TEXT_WHITE, dropdown_fg_color=CARD_BG,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12)
        ).pack(pady=(4, 16))

        # Q3 Outside Eating
        ctk.CTkLabel(card, text="3. OUTSIDE DINING FREQUENCY", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.outside_var = ctk.StringVar(value="a) Once a week")
        ctk.CTkOptionMenu(
            card, values=[
                "a) Once a week",
                "b) Twice/Thrice a week",
                "c) Four times a week",
                "d) 5+ times a week"
            ],
            variable=self.outside_var, width=400, height=40, corner_radius=8,
            fg_color=CARD_INNER_BG, button_color=GOLD_PRIMARY, button_hover_color=GOLD_HOVER,
            text_color=TEXT_WHITE, dropdown_fg_color=CARD_BG,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12)
        ).pack(pady=(4, 24))

        ctk.CTkButton(
            card, text="NEXT STEP ➔", width=400, height=46, corner_radius=10,
            fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color="#000000",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            command=self.save_w3_and_next
        ).pack(pady=10)

        self.add_contact_us_footer()

    def save_w3_and_next(self):
        self.user_data["activity"] = self.activity_var.get()
        self.user_data["outside_freq"] = self.outside_var.get()[0]
        self.show_window_4_meal_prep()

    # ==================================================
    # WINDOW 4: Meal Prep Style
    # ==================================================
    def show_window_4_meal_prep(self):
        self.clear_container()

        card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=18, border_width=1, border_color=BORDER_GOLD)
        card.pack(fill="x", pady=10, ipadx=15, ipady=20)

        ctk.CTkLabel(card, text="PREPARATION PREFERENCE", font=ctk.CTkFont(family=FONT_SERIF[0], size=16, weight="bold"), text_color=TEXT_WHITE).pack(pady=(5, 5))
        ctk.CTkLabel(card, text="Select your preferred meal arrangement strategy", font=ctk.CTkFont(family=FONT_SERIF[0], size=11), text_color=TEXT_GOLD).pack(pady=(0, 15))

        self.prep_var = ctk.StringVar(value="a")
        opts = [
            ("Fresh cooking", "a"),
            ("No-cook / Assembly only", "b"),
            ("Meal delivery / Takeout", "c"),
            ("Grocery store grab & go", "d")
        ]

        for text, val in opts:
            ctk.CTkRadioButton(
                card, text=text, value=val, variable=self.prep_var,
                fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color=TEXT_WHITE,
                font=ctk.CTkFont(family=FONT_SERIF[0], size=13)
            ).pack(anchor="w", padx=30, pady=10)

        ctk.CTkButton(
            card, text="SELECT FOOD CUISINES ➔", width=400, height=46, corner_radius=10,
            fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color="#000000",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            command=self.save_w4_and_next
        ).pack(pady=(24, 10))

        self.add_contact_us_footer()

    def save_w4_and_next(self):
        self.user_data["prep_pref"] = self.prep_var.get()
        self.show_window_5_food_selection()

    # ==================================================
    # WINDOW 5: Food Preferences Checklist
    # ==================================================
    def show_window_5_food_selection(self):
        self.clear_container()

        ctk.CTkLabel(self.container, text="CURATED DIETARY PREFERENCES", font=ctk.CTkFont(family=FONT_SERIF[0], size=16, weight="bold"), text_color=TEXT_WHITE).pack(pady=(5, 2))
        ctk.CTkLabel(self.container, text="Select the items you wish to include in your menu:", font=ctk.CTkFont(family=FONT_SERIF[0], size=11), text_color=TEXT_GOLD).pack(pady=(0, 10))

        scroll_frame = ctk.CTkScrollableFrame(self.container, width=440, height=360, fg_color=CARD_BG, corner_radius=14, border_width=1, border_color=BORDER_GOLD)
        scroll_frame.pack(pady=10)

        self.checkbox_vars = {}

        for category, items in FOOD_DATABASE.items():
            ctk.CTkLabel(scroll_frame, text=f"• {category.upper()} •", font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"), text_color=GOLD_PRIMARY).pack(anchor="w", padx=15, pady=(12, 6))
            for food in items:
                var = ctk.BooleanVar(value=True)
                chk = ctk.CTkCheckBox(
                    scroll_frame, text=food["name"], variable=var,
                    fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color=TEXT_WHITE,
                    border_color=BORDER_GOLD, font=ctk.CTkFont(family=FONT_BODY[0], size=12)
                )
                chk.pack(anchor="w", padx=25, pady=4)
                self.checkbox_vars[food["name"]] = var

        ctk.CTkButton(
            self.container, text="GENERATE EXCLUSIVE MEAL PLAN ✨", width=460, height=46, corner_radius=10,
            fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color="#000000",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            command=self.save_w5_and_next
        ).pack(pady=15)

        self.add_contact_us_footer()

    def save_w5_and_next(self):
        selected = [name for name, var in self.checkbox_vars.items() if var.get()]
        self.user_data["selected_foods"] = selected
        self.show_window_6_daily_plan()

    # ==================================================
    # WINDOW 6: Daily Meal Plan Display
    # ==================================================
    def show_window_6_daily_plan(self):
        self.clear_container()

        bmi, bmi_cat = calculate_bmi(self.user_data["weight"], self.user_data["height"])
        bmr = calculate_bmr(self.user_data["gender"], self.user_data["weight"], self.user_data["height"], self.user_data["age"])
        tdee = calculate_tdee(bmr, self.user_data["activity"])
        target_cal = get_target_calories(tdee, self.user_data["target"])
        split = get_meal_calorie_split(target_cal)

        meal_plan = generate_daily_meal_plan(self.user_data["prep_pref"], self.previous_meal_plan)
        self.previous_meal_plan = meal_plan

        # Header Badge Card
        header_card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=16, border_width=1, border_color=BORDER_GOLD)
        header_card.pack(fill="x", pady=(0, 12), ipadx=12, ipady=12)

        ctk.CTkLabel(header_card, text=f"WELCOME, {self.user_data['name'].upper()}", font=ctk.CTkFont(family=FONT_SERIF[0], size=16, weight="bold"), text_color=TEXT_WHITE).pack(anchor="w", padx=10)
        ctk.CTkLabel(
            header_card,
            text=f"BMI: {bmi} ({bmi_cat})   |   TARGET: {target_cal} kcal/day",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12, weight="bold"), text_color=GOLD_PRIMARY
        ).pack(anchor="w", padx=10, pady=(3, 0))

        # Schedule banner
        sched_card = ctk.CTkFrame(self.container, fg_color=CARD_INNER_BG, corner_radius=10, border_width=1, border_color="#2D291E")
        sched_card.pack(fill="x", pady=6, ipady=6)
        ctk.CTkLabel(
            sched_card,
            text="⏰ TIMING SCHEDULE: Wake: 07:00 AM  •  Sleep: 10:30 PM",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11, slant="italic"), text_color=TEXT_GOLD
        ).pack()

        # Slots Loop
        slots = [
            ("🍳 BREAKFAST", "08:30 AM", "Breakfast"),
            ("🥗 LUNCH", "01:30 PM", "Lunch"),
            ("🥜 SNACKS", "05:00 PM", "Snacks"),
            ("🍽️ DINNER", "08:00 PM", "Dinner"),
        ]

        for code, time_str, slot_key in slots:
            item = meal_plan[slot_key]

            slot_card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=14, border_width=1, border_color=BORDER_GOLD)
            slot_card.pack(fill="x", pady=6, ipadx=12, ipady=12)

            # Top Row
            top_frame = ctk.CTkFrame(slot_card, fg_color="transparent")
            top_frame.pack(fill="x", expand=True)

            ctk.CTkLabel(top_frame, text=f"{code} ({time_str})", font=ctk.CTkFont(family=FONT_SERIF[0], size=12, weight="bold"), text_color=GOLD_PRIMARY).pack(side="left")
            ctk.CTkLabel(top_frame, text=f"~{item['calories']} kcal (Goal: {split[slot_key]})", font=ctk.CTkFont(family=FONT_SERIF[0], size=11), text_color=SUBTEXT_MUTED).pack(side="right")

            # Bottom Row
            bottom_frame = ctk.CTkFrame(slot_card, fg_color="transparent")
            bottom_frame.pack(fill="x", expand=True, pady=(8, 0))

            ctk.CTkLabel(bottom_frame, text=item["name"], font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"), text_color=TEXT_WHITE).pack(side="left")

            # Dynamic button configuration based on prep preference 'c' (Meal delivery / Takeout)
            is_takeout = self.user_data.get("prep_pref") == "c"
            button_label = "RESTAURANTS 📍" if is_takeout else "RECIPE 🔗"

            ctk.CTkButton(
                bottom_frame,
                text=button_label,
                width=110 if is_takeout else 80,
                height=26,
                corner_radius=6,
                fg_color=GOLD_PRIMARY,
                hover_color=GOLD_HOVER,
                text_color="#000000",
                font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"),
                command=lambda url=item["link"]: webbrowser.open(url)
            ).pack(side="right")

        # Regenerate Action Button
        ctk.CTkButton(
            self.container, text="🔄 REGENERATE EXCLUSIVE MENU", width=460, height=46, corner_radius=10,
            fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color="#000000",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            command=self.show_window_6_daily_plan
        ).pack(pady=15)

        self.add_contact_us_footer()


if __name__ == "__main__":
    app = AvyroApp()
    app.mainloop()