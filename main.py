
import os
import pandas as pd
import numpy as np

import streamlit as st

# Set theme configuration
os.makedirs(".streamlit", exist_ok=True)
with open(".streamlit/config.toml", "w") as f:
    f.write("""
[theme]
primaryColor="#893f71"
backgroundColor="#381a2f"
secondaryBackgroundColor="#874e5f"
textColor="#f3d0a4"
font="sans serif"
""")


# Extract weight (w) and bias (b)
w = 0.6918389034467243
b = 46.97175858156635

st.title("BMI & Blood Pressure Health Checker")

# Inputs
user_bmi = st.number_input(
    f"Enter your {FEATURE_COLUMN}:",
    min_value=float(X[FEATURE_COLUMN].min()),
    max_value=float(X[FEATURE_COLUMN].max()),
    value=float(X[FEATURE_COLUMN].mean()),
    step=0.1
)

user_bp = st.number_input(
    "Enter your Actual Blood Pressure (mmHg):",
    min_value=40.0,
    max_value=180.0,
    value=70.0,
    step=1.0
)

if st.button("Run Analysis"):
    st.write("---")
    
    # --- 1. BMI CATEGORY ANALYSIS ---
    st.markdown("### 📊 BMI Range Evaluation")
    
    if user_bmi < 18.5:
        st.info(f"**BMI Category:** Underweight (`{user_bmi:.1f}`)")
        st.markdown("**BMI Recommendations:**")
        st.markdown("* 🥑 **Nutrient Intake:** Focus on calorie-dense, nutrient-rich foods (nuts, whole grains, healthy oils).")
        st.markdown("* 🏋️ **Strength Training:** Incorporate light resistance exercise to build muscle volume.")
        
    elif 18.5 <= user_bmi <= 24.9:
        st.success(f"**BMI Category:** Standard / Normal Weight (`{user_bmi:.1f}`)")
        st.markdown("**BMI Recommendations:**")
        st.markdown("* 🎯 **Consistency:** Maintain current physical activity levels and balanced nutritional habits.")
        
    else:
        st.warning(f"**BMI Category:** Elevated / Overweight (`{user_bmi:.1f}`)")
        st.markdown("**BMI Recommendations:**")
        st.markdown("* 🥗 **Whole Foods:** Prioritize high-fiber vegetables, lean proteins, and portion awareness.")
        st.markdown("* 🏃 **Regular Movement:** Aim for 150 minutes of moderate cardiovascular exercise per week.")

    st.write("---")

    # --- 2. MODEL BP COMPARISON ---
    st.markdown("### 🩺 Blood Pressure vs. Model Expectation")
    
    # Manual equation: y = w * x + b
    predicted_bp = (w * user_bmi) + b
    margin = 5.0
    lower_bound = predicted_bp - margin
    upper_bound = predicted_bp + margin
    
    st.write(f"**Model Predicted BP:** `{predicted_bp:.2f} mmHg`")
    st.write(f"**Your Actual BP:** `{user_bp:.2f} mmHg`")
    
    if lower_bound <= user_bp <= upper_bound:
        st.success("🎯 **BP In Range:** Your actual blood pressure matches expected predictions for your BMI.")
    elif user_bp > upper_bound:
        st.warning("⚠️ **BP Above Expected:** Your reading is higher than projected for your BMI.")
        st.markdown("* 🧂 **Reduce Sodium:** Limit processed meals and added table salt.")
        st.markdown("* 🧘 **Stress Reduction:** Practice relaxation techniques or light exercise.")
        st.markdown("* 🩺 **Medical Guidance:** Consult a physician for accurate cardiovascular checks.")
    else:
        st.info("ℹ️ **BP Below Expected:** Your reading is lower than projected for your BMI.")
        st.markdown("* 💧 **Hydration:** Increase liquid intake throughout the day.")
        st.markdown("* 🚶 **Pace Stance:** Rise slowly from sitting positions to avoid dizziness.")
        st.markdown("* 🩺 **Medical Guidance:** Seek expert advice if experiencing fatigue or lightheadedness.")
