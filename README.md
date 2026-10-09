# Avyro
A Nutrition Focused Platform

# 🥗 Avyro — Eat. Move. Evolve.

> A modern, personalized Python GUI application that calculates daily energy targets and generates customized, non-repetitive meal plans based on individual physical metrics and lifestyle preferences.

---

## ✨ Features

- 👤 **Personalized Onboarding:** Tailored setup capturing user profile metrics (age, gender, height, weight, activity levels, and health goals).
- 🧮 **Scientific Calorie Engine:** Calculates **BMR** (Mifflin-St Jeor Equation) and **TDEE** to deliver customized daily calorie targets.
- 🎯 **Meal Calorie Distribution:** Automatically splits daily caloric goals across 4 primary meals (Breakfast, Lunch, Snacks, Dinner).
- 🥦 **Food Option Selection:** Interactively select and filter preferred food choices across multiple prep styles (Fresh, No-cook, Takeout, Grab & Go).
- 🔄 **Smart Non-Consecutive Randomization:** Ensures variety by avoiding repeated consecutive meal plans.
- ⏰ **Integrated Schedule & Timings:** Recommends structured daily meal windows alongside optimal sleep and wake-up schedules.
- 🔗 **Direct Recipe Links:** Built-in web integration to open step-by-step recipes with a single click.
- Takeout Options: For those who dont have the time or the mood to cook

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **GUI Framework:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **Version Control:** Git & GitHub

---

## 📂 Project Architecture

```text
Avyro/
│
├── main.py            # CustomTkinter Multi-Window GUI App Flow
├── calorie_calc.py    # Mifflin-St Jeor BMR, TDEE, & Calorie Logic
├── food_db.py         # Structured Food Database & External Recipe Links
├── meal_planner.py    # Randomized, Non-Consecutive Meal Allocation
├── requirements.txt   # Project Dependencies
└── README.md          # Project Documentation
