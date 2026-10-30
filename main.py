# ==========================================
# FILE: main.py
# DESCRIPTION: CustomTkinter GUI featuring unboxed side-by-side affirmation & exercise text,
# increased title size & spacing for the meal planner header, and strict validation.
# ==========================================

import webbrowser
import customtkinter as ctk

from calorie_calc import (
    calculate_bmr,
    calculate_tdee,
    get_meal_calorie_split,
    get_target_calories,
)
from food_db import FOOD_DATABASE, generate_daily_meal_plan

# Configure Theme Settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# --- LUXURY OMBRE & GOLD PALETTE ---
BG_DARK = "#090A0F"          # Deep Obsidian Base
BG_GRADIENT_ALT = "#10131D"  # Ombre Card/Frame Layer
CARD_BG = "#151824"          # Rich Midnight Surface
BORDER_GOLD = "#D4AF37"      # Metallic Gold
GOLD_PRIMARY = "#E5C158"     # Bright Accent Gold
GOLD_HOVER = "#C59827"       # Hover Gold
TEXT_WHITE = "#FFFFFF"       # White Text
TEXT_GOLD = "#F3E5AB"        # Champagne Accent Text
SUBTEXT_MUTED = "#8A8F9E"    # Muted Gray
ERROR_RED = "#E06D6D"        # Validation Error Text

# --- CALLIGRAPHY & TYPOGRAPHY ---
FONT_SCRIPT = ("Lucida Handwriting", "Brush Script MT", "Georgia")  # Cursive/Calligraphic styling
FONT_SERIF = ("Georgia", "Baskerville")
FONT_BODY = ("Segoe UI", "Helvetica")


class AvyroApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AVŸRO - Exclusive Nutrition & Wellness")
        self.geometry("580x920")
        self.resizable(True, True)
        self.configure(fg_color=BG_DARK)

        self.user_data = {
            "name": "",
            "email": "",
            "age": 25,
            "gender": "Male",
            "height": 170.0,
            "weight": 65.0,
            "target": "Maintain Weight",
            "medical_condition": "General Wellness",
            "activity": "moderate",
            "outside_freq": "a",
            "prep_pref": "a",
            "selected_foods": []
        }

        self.previous_meal_plan = {}

        # Master Scrollable Frame with Ombre Texture Effect
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
            text="- C O N T A C T   U S -",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            text_color=GOLD_PRIMARY
        ).pack(pady=(2, 4))

        ctk.CTkLabel(
            footer_card,
            text="📞 +1 (800) 555-AVŸRO  |  ✉ support@avyro.com",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11),
            text_color=TEXT_GOLD
        ).pack(pady=(0, 2))

        ctk.CTkLabel(
            footer_card,
            text="Avyro Concierge Wellness • Exclusive Member Support 24/7",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=10, slant="italic"),
            text_color=SUBTEXT_MUTED
        ).pack(pady=(0, 2))

    # ==================================================
    # WINDOW 1: Registration
    # ==================================================
    def show_window_1_registration(self):
        self.clear_container()

        header_card = ctk.CTkFrame(self.container, fg_color=BG_GRADIENT_ALT, corner_radius=20, border_width=2, border_color=BORDER_GOLD)
        header_card.pack(fill="x", pady=(0, 15), ipady=22)

        ctk.CTkLabel(
            header_card, text="Avÿro",
            font=ctk.CTkFont(family=FONT_SCRIPT[0], size=46, weight="bold", slant="italic"),
            text_color=GOLD_PRIMARY
        ).pack(pady=(12, 2))

        ctk.CTkLabel(
            header_card, text="◆  E a t  •  M o v e  •  E v o l v e  ◆",
            font=ctk.CTkFont(family=FONT_SCRIPT[0], size=12, slant="italic"),
            text_color=TEXT_GOLD
        ).pack(pady=(0, 8))

        card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=18, border_width=1, border_color=BORDER_GOLD)
        card.pack(fill="x", pady=10, ipadx=15, ipady=20)

        ctk.CTkLabel(
            card, text="MEMBER ACCESS PORTAL",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=16, weight="bold"),
            text_color=TEXT_WHITE
        ).pack(pady=(5, 18))

        ctk.CTkLabel(card, text="FULL NAME", font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_name = ctk.CTkEntry(
            card, placeholder_text="Enter your full name", width=420, height=42,
            corner_radius=10, fg_color=BG_DARK, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE,
            font=ctk.CTkFont(family=FONT_BODY[0], size=12)
        )
        self.entry_name.pack(pady=(4, 16))
        self.entry_name.bind("<KeyRelease>", self.check_w1_inputs)

        ctk.CTkLabel(card, text="EMAIL OR PHONE", font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_email = ctk.CTkEntry(
            card, placeholder_text="Enter email or phone number", width=420, height=42,
            corner_radius=10, fg_color=BG_DARK, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE,
            font=ctk.CTkFont(family=FONT_BODY[0], size=12)
        )
        self.entry_email.pack(pady=(4, 24))
        self.entry_email.bind("<KeyRelease>", self.check_w1_inputs)

        self.btn_begin = ctk.CTkButton(
            card, text="BEGIN MEMBERSHIP ➔", width=420, height=46,
            corner_radius=10, fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER,
            text_color="#000000", font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            command=self.save_w1_and_next,
            state="disabled"
        )
        self.btn_begin.pack(pady=10)

        self.add_contact_us_footer()

    def check_w1_inputs(self, event=None):
        if self.entry_name.get().strip() and self.entry_email.get().strip():
            self.btn_begin.configure(state="normal")
        else:
            self.btn_begin.configure(state="disabled")

    def save_w1_and_next(self):
        self.user_data["name"] = self.entry_name.get().strip() or "User"
        self.user_data["email"] = self.entry_email.get().strip()
        self.show_window_2_metrics()

    # ==================================================
    # WINDOW 2: Physical Metrics with Strict Input Validation
    # ==================================================
    def show_window_2_metrics(self):
        self.clear_container()

        card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=18, border_width=1, border_color=BORDER_GOLD)
        card.pack(fill="x", pady=10, ipadx=15, ipady=20)

        ctk.CTkLabel(card, text="BODY METRICS & HEALTH FOCUS", font=ctk.CTkFont(family=FONT_SERIF[0], size=16, weight="bold"), text_color=TEXT_WHITE).pack(pady=(5, 18))

        self.error_label = ctk.CTkLabel(card, text="", font=ctk.CTkFont(family=FONT_BODY[0], size=11, weight="bold"), text_color=ERROR_RED)
        self.error_label.pack(pady=(0, 5))

        ctk.CTkLabel(card, text="AGE (YEARS)", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_age = ctk.CTkEntry(card, placeholder_text="Enter numeric age (e.g., 25)", width=420, height=40, corner_radius=8, fg_color=BG_DARK, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE)
        self.entry_age.pack(pady=(4, 14))

        ctk.CTkLabel(card, text="GENDER", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.gender_var = ctk.StringVar(value="Male")
        ctk.CTkSegmentedButton(
            card, values=["Male", "Female"], variable=self.gender_var,
            width=420, height=38, selected_color=GOLD_PRIMARY, selected_hover_color=GOLD_HOVER,
            unselected_color=BG_DARK, text_color=TEXT_WHITE, font=ctk.CTkFont(family=FONT_SERIF[0], size=11)
        ).pack(pady=(4, 14))

        ctk.CTkLabel(card, text="HEIGHT (CM)", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_height = ctk.CTkEntry(card, placeholder_text="Enter numeric height in cm (e.g., 170)", width=420, height=40, corner_radius=8, fg_color=BG_DARK, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE)
        self.entry_height.pack(pady=(4, 14))

        ctk.CTkLabel(card, text="WEIGHT (KG)", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.entry_weight = ctk.CTkEntry(card, placeholder_text="Enter numeric weight in kg (e.g., 65)", width=420, height=40, corner_radius=8, fg_color=BG_DARK, border_color=BORDER_GOLD, border_width=1, text_color=TEXT_WHITE)
        self.entry_weight.pack(pady=(4, 14))

        ctk.CTkLabel(card, text="MEDICAL CONDITION / HEALTH FOCUS", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.condition_var = ctk.StringVar(value="General Wellness")
        ctk.CTkOptionMenu(
            card, values=["General Wellness", "Diabetes", "Thyroid", "Blood Pressure"],
            variable=self.condition_var, width=420, height=40, corner_radius=8,
            fg_color=BG_DARK, button_color=GOLD_PRIMARY, button_hover_color=GOLD_HOVER,
            text_color=TEXT_WHITE, dropdown_fg_color=CARD_BG,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12)
        ).pack(pady=(4, 14))

        ctk.CTkLabel(card, text="PRIMARY GOAL", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.target_var = ctk.StringVar(value="Maintain Weight")
        ctk.CTkOptionMenu(
            card, values=["Weight Loss", "Maintain Weight", "Weight Gain"],
            variable=self.target_var, width=420, height=40, corner_radius=8,
            fg_color=BG_DARK, button_color=GOLD_PRIMARY, button_hover_color=GOLD_HOVER,
            text_color=TEXT_WHITE, dropdown_fg_color=CARD_BG,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12)
        ).pack(pady=(4, 24))

        ctk.CTkButton(
            card, text="SAVE & CONTINUE ➔", width=420, height=46, corner_radius=10,
            fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color="#000000",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"),
            command=self.save_w2_and_next
        ).pack(pady=10)

        self.add_contact_us_footer()

    def save_w2_and_next(self):
        try:
            age_val = float(self.entry_age.get().strip())
            height_val = float(self.entry_height.get().strip())
            weight_val = float(self.entry_weight.get().strip())

            if age_val <= 0 or height_val <= 0 or weight_val <= 0:
                raise ValueError()

            self.user_data["age"] = int(age_val)
            self.user_data["height"] = height_val
            self.user_data["weight"] = weight_val
            self.user_data["medical_condition"] = self.condition_var.get()
            self.user_data["target"] = self.target_var.get()

            self.show_window_3_questionnaire()
        except ValueError:
            self.error_label.configure(text="⚠️ Error: Please enter valid numbers for Age, Height, and Weight!")

    # ==================================================
    # WINDOW 3: Lifestyle Questionnaire
    # ==================================================
    def show_window_3_questionnaire(self):
        self.clear_container()

        card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=18, border_width=1, border_color=BORDER_GOLD)
        card.pack(fill="x", pady=10, ipadx=15, ipady=20)

        ctk.CTkLabel(card, text="LIFESTYLE ASSESSMENTS", font=ctk.CTkFont(family=FONT_SERIF[0], size=16, weight="bold"), text_color=TEXT_WHITE).pack(pady=(5, 18))

        ctk.CTkLabel(card, text="1. DAILY WORKOUT FREQUENCY", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.activity_var = ctk.StringVar(value="moderate")
        ctk.CTkOptionMenu(
            card, values=["sedentary", "light", "moderate", "active", "N/A"],
            variable=self.activity_var, width=420, height=40, corner_radius=8,
            fg_color=BG_DARK, button_color=GOLD_PRIMARY, button_hover_color=GOLD_HOVER,
            text_color=TEXT_WHITE, dropdown_fg_color=CARD_BG,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12)
        ).pack(pady=(4, 16))

        ctk.CTkLabel(card, text="2. DAILY ENERGY & MOOD", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.mood_var = ctk.StringVar(value="Energetic")
        ctk.CTkOptionMenu(
            card, values=["Energetic", "Normal", "Tired", "Stressed"],
            variable=self.mood_var, width=420, height=40, corner_radius=8,
            fg_color=BG_DARK, button_color=GOLD_PRIMARY, button_hover_color=GOLD_HOVER,
            text_color=TEXT_WHITE, dropdown_fg_color=CARD_BG,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12)
        ).pack(pady=(4, 16))

        ctk.CTkLabel(card, text="3. OUTSIDE DINING FREQUENCY", font=ctk.CTkFont(family=FONT_SERIF[0], size=10, weight="bold"), text_color=TEXT_GOLD).pack(anchor="w", padx=25)
        self.outside_var = ctk.StringVar(value="a) Once a week")
        ctk.CTkOptionMenu(
            card, values=[
                "a) Once a week",
                "b) Twice/Thrice a week",
                "c) Four times a week",
                "d) 5+ times a week"
            ],
            variable=self.outside_var, width=420, height=40, corner_radius=8,
            fg_color=BG_DARK, button_color=GOLD_PRIMARY, button_hover_color=GOLD_HOVER,
            text_color=TEXT_WHITE, dropdown_fg_color=CARD_BG,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12)
        ).pack(pady=(4, 24))

        ctk.CTkButton(
            card, text="NEXT STEP ➔", width=420, height=46, corner_radius=10,
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
            card, text="SELECT FOOD CUISINES ➔", width=420, height=46, corner_radius=10,
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
        ctk.CTkLabel(self.container, text=f"Focus: {self.user_data['medical_condition']} • Select items to include:", font=ctk.CTkFont(family=FONT_SERIF[0], size=11), text_color=TEXT_GOLD).pack(pady=(0, 10))

        scroll_frame = ctk.CTkScrollableFrame(self.container, width=460, height=360, fg_color=CARD_BG, corner_radius=14, border_width=1, border_color=BORDER_GOLD)
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
            self.container, text="GENERATE EXCLUSIVE MEAL PLAN ✨", width=480, height=46, corner_radius=10,
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

        bmr = calculate_bmr(self.user_data["gender"], self.user_data["weight"], self.user_data["height"], self.user_data["age"])
        tdee = calculate_tdee(bmr, self.user_data["activity"])
        target_cal = get_target_calories(tdee, self.user_data["target"], self.user_data["medical_condition"])
        split = get_meal_calorie_split(target_cal)

        meal_plan = generate_daily_meal_plan(self.user_data["prep_pref"], self.user_data["medical_condition"], self.previous_meal_plan)
        self.previous_meal_plan = meal_plan

        # Header Badge Card
        header_card = ctk.CTkFrame(self.container, fg_color=BG_GRADIENT_ALT, corner_radius=16, border_width=1, border_color=BORDER_GOLD)
        header_card.pack(fill="x", pady=(0, 10), ipadx=12, ipady=12)

        ctk.CTkLabel(header_card, text=f"WELCOME, {self.user_data['name'].upper()}", font=ctk.CTkFont(family=FONT_SERIF[0], size=16, weight="bold"), text_color=TEXT_WHITE).pack(anchor="w", padx=10)
        ctk.CTkLabel(
            header_card,
            text=f"HEALTH FOCUS: {self.user_data['medical_condition'].upper()}   |   TARGET: {target_cal} kcal/day",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12, weight="bold"), text_color=GOLD_PRIMARY
        ).pack(anchor="w", padx=10, pady=(3, 0))

        # ==========================================
        # UNBOXED SIDE-BY-SIDE AFFIRMATION & EXERCISE TEXT
        # ==========================================
        duo_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        duo_frame.pack(fill="x", pady=6)

        # 1. Affirmation Side (Left)
        aff_side = ctk.CTkFrame(duo_frame, fg_color="transparent")
        aff_side.pack(side="left", fill="both", expand=True, padx=(0, 5))
        
        ctk.CTkLabel(
            aff_side, text="✨ AFFIRMATION", 
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold"), 
            text_color=GOLD_PRIMARY
        ).pack(anchor="w", padx=4)
        
        ctk.CTkLabel(
            aff_side, text="\"Today, I honor my body with balanced choices & calm energy.\"", 
            font=ctk.CTkFont(family=FONT_SCRIPT[0], size=10, slant="italic"), 
            text_color=TEXT_WHITE,
            wraplength=230,
            justify="left"
        ).pack(anchor="w", padx=4, pady=(2, 0))

        # 2. Exercise Side (Right)
        ex_side = ctk.CTkFrame(duo_frame, fg_color="transparent")
        ex_side.pack(side="right", fill="both", expand=True, padx=(5, 0))
        
        ctk.CTkLabel(
            ex_side, text=f"🏋️‍♂️ EXERCISE ({self.user_data['medical_condition']})", 
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold"), 
            text_color=GOLD_PRIMARY
        ).pack(anchor="w", padx=4)
        
        ctk.CTkLabel(
            ex_side, text="30-Min Low-Impact Cardio or Adaptive Joint Mobility Stretching session.", 
            font=ctk.CTkFont(family=FONT_BODY[0], size=10), 
            text_color=TEXT_WHITE,
            wraplength=230,
            justify="left"
        ).pack(anchor="w", padx=4, pady=(2, 0))

        # ==========================================

        # Schedule banner
        sched_card = ctk.CTkFrame(self.container, fg_color=BG_GRADIENT_ALT, corner_radius=10, border_width=1, border_color="#2D291E")
        sched_card.pack(fill="x", pady=6, ipady=6)
        ctk.CTkLabel(
            sched_card,
            text="⏰ TIMING SCHEDULE: Wake: 07:00 AM  •  Sleep: 10:30 PM",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11, slant="italic"), text_color=TEXT_GOLD
        ).pack()

        # ==========================================
        # MEAL PLANNER SECTION TITLE (Increased Font & Spacing)
        # ==========================================
        title_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        title_frame.pack(fill="x", pady=(20, 10))  # Increased top and bottom padding
        
        ctk.CTkLabel(
            title_frame, 
            text="—   Y O U R   D A I L Y   M E A L   P L A N N E R   —", 
            font=ctk.CTkFont(family=FONT_SERIF[0], size=15, weight="bold"),  # Increased font size
            text_color=GOLD_PRIMARY
        ).pack(anchor="center")
        # ==========================================

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

            top_frame = ctk.CTkFrame(slot_card, fg_color="transparent")
            top_frame.pack(fill="x", expand=True)

            ctk.CTkLabel(top_frame, text=f"{code} ({time_str})", font=ctk.CTkFont(family=FONT_SERIF[0], size=12, weight="bold"), text_color=GOLD_PRIMARY).pack(side="left")
            ctk.CTkLabel(top_frame, text=f"~{item['calories']} kcal (Goal: {split[slot_key]})", font=ctk.CTkFont(family=FONT_SERIF[0], size=11), text_color=SUBTEXT_MUTED).pack(side="right")

            bottom_frame = ctk.CTkFrame(slot_card, fg_color="transparent")
            bottom_frame.pack(fill="x", expand=True, pady=(8, 0))

            ctk.CTkLabel(bottom_frame, text=item["name"], font=ctk.CTkFont(family=FONT_SERIF[0], size=13, weight="bold"), text_color=TEXT_WHITE).pack(side="left")

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

        # Action Buttons Section
        btn_action_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        btn_action_frame.pack(fill="x", pady=12)

        ctk.CTkButton(
            btn_action_frame, text="🔄 REGENERATE", width=150, height=42, corner_radius=10,
            fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color="#000000",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold"),
            command=self.show_window_6_daily_plan
        ).pack(side="left", padx=3, expand=True)

        ctk.CTkButton(
            btn_action_frame, text="📋 RESELECT MEALS", width=150, height=42, corner_radius=10,
            fg_color=BG_GRADIENT_ALT, border_color=BORDER_GOLD, border_width=1, hover_color="#2A2415", text_color=TEXT_WHITE,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold"),
            command=self.show_window_5_food_selection
        ).pack(side="left", padx=3, expand=True)

        ctk.CTkButton(
            btn_action_frame, text="👤 VIEW PROFILE", width=150, height=42, corner_radius=10,
            fg_color=BG_GRADIENT_ALT, border_color=BORDER_GOLD, border_width=1, hover_color="#2A2415", text_color=TEXT_WHITE,
            font=ctk.CTkFont(family=FONT_SERIF[0], size=11, weight="bold"),
            command=self.show_profile_view
        ).pack(side="left", padx=3, expand=True)

        self.add_contact_us_footer()

    # ==================================================
    # VIEW PROFILE SCREEN
    # ==================================================
    def show_profile_view(self):
        self.clear_container()

        card = ctk.CTkFrame(self.container, fg_color=CARD_BG, corner_radius=18, border_width=1, border_color=BORDER_GOLD)
        card.pack(fill="x", pady=10, ipadx=15, ipady=20)

        ctk.CTkLabel(card, text="MEMBER PROFILE SUMMARY", font=ctk.CTkFont(family=FONT_SERIF[0], size=18, weight="bold"), text_color=GOLD_PRIMARY).pack(pady=(5, 15))

        profile_details = [
            ("Full Name", self.user_data["name"]),
            ("Email / Phone", self.user_data["email"] or "Not provided"),
            ("Age", f"{self.user_data['age']} years"),
            ("Gender", self.user_data["gender"]),
            ("Height", f"{self.user_data['height']} cm"),
            ("Weight", f"{self.user_data['weight']} kg"),
            ("Health Focus", self.user_data["medical_condition"]),
            ("Primary Goal", self.user_data["target"]),
            ("Activity Level", self.user_data["activity"].title()),
        ]

        for label, val in profile_details:
            row = ctk.CTkFrame(card, fg_color=BG_GRADIENT_ALT, corner_radius=8)
            row.pack(fill="x", padx=20, pady=4, ipady=6)
            ctk.CTkLabel(row, text=label, font=ctk.CTkFont(family=FONT_SERIF[0], size=12, weight="bold"), text_color=TEXT_GOLD).pack(side="left", padx=15)
            ctk.CTkLabel(row, text=str(val), font=ctk.CTkFont(family=FONT_BODY[0], size=12), text_color=TEXT_WHITE).pack(side="right", padx=15)

        ctk.CTkButton(
            card, text="← BACK TO MEAL PLAN", width=420, height=44, corner_radius=10,
            fg_color=GOLD_PRIMARY, hover_color=GOLD_HOVER, text_color="#000000",
            font=ctk.CTkFont(family=FONT_SERIF[0], size=12, weight="bold"),
            command=self.show_window_6_daily_plan
        ).pack(pady=(20, 10))

        self.add_contact_us_footer()


if __name__ == "__main__":
    app = AvyroApp()
    app.mainloop()