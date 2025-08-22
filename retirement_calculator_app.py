import streamlit as st

def calculate_monthly_investment(current_age, retirement_age, income_goal, income_type):
    annual_income = income_goal * 12 if income_type == "monthly" else income_goal
    required_investment = annual_income / 0.04
    years_to_grow = retirement_age - current_age
    n = years_to_grow * 12
    r = 0.07 / 12
    monthly_investment = required_investment / (((1 + r)**n - 1) / r)
    return monthly_investment, required_investment, years_to_grow

# --- UI ---
st.title("🧮 Retirement Calculator")

name = st.text_input("What is your name?")
current_age = st.number_input("What is your current age?", min_value=14, max_value=98, step=1)
retirement_age = st.number_input("At what age would you like to retire?", min_value=18, max_value=99, step=1)
income_goal = st.number_input("How much income would you like to receive during retirement?", min_value=0.0)
income_type = st.radio("Is that amount monthly or yearly?", ["monthly", "yearly"])

if st.button("Calculate"):
    if current_age >= retirement_age:
        st.error("Retirement age must be greater than current age.")
    elif name.strip() == "":
        st.error("Please enter your name.")
    elif income_goal <= 0:
        st.error("Please enter an income goal greater than zero.")
    else:
        monthly_investment, required_investment, years_to_grow = calculate_monthly_investment(
            current_age, retirement_age, income_goal, income_type
        )

        st.success(f"Hi {name}, to retire at age {retirement_age}, you need to invest ${monthly_investment:,.0f} per month.")
        st.info(f"This means you will need to have invested a total of ${required_investment:,.0f} in {years_to_grow} years.")
        
        st.warning("Disclaimer: This calculator uses a 4% safe withdrawal rule and assumes a 7% annual return on investment, compounded monthly.")