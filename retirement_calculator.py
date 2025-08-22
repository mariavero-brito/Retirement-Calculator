def main():

    name = input("What is your name?")

    while True:
        try:
            current_age = int(input("What is your current age?"))

            if 14<current_age<99:
                break 
            else:
                print("Invalid age. Age must be between 14 and 99.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            retirement_age = int(input("What age do you want to retire?"))

            if 18<retirement_age<99 and retirement_age>current_age:
                break 
            else:
                print("Invalid retirement age. Age must be between 18 and 99, and greater than your current age.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            raw_income_goal = input("How much income would you like to receive during your retirement?")
            
            cleaned_income_goal = raw_income_goal.replace(",", "").replace("$", "")
            income_goal = float(cleaned_income_goal)

            if income_goal <= 0:
                    print("Please enter a number bigger than zero.")
            if income_goal > 0:
                    break
        except ValueError:
            print("Please enter a valid number.")

    income_type = input("Is that amount monthly or yearly? (monthly/yearly)").lower()
    if income_type == "monthly":
        annual_income = income_goal * 12
    else:
        annual_income = income_goal

    required_investment = annual_income / 0.04

    years_to_grow = int(retirement_age - current_age)

    n = years_to_grow * 12 #number of yrs until retirement multiplied by 12 for months in a yr
    r = 0.07 / 12 #calculating monthly return
    monthly_investment = required_investment / (((1 + r)**n - 1) / r) #formula to find monthly contribution

    print(f"-----Retirement Summary-----")
    print(f"{name}, you are {current_age} years old")
    print(f"Your monthly investment required is: ${monthly_investment:,.0f}")
    print(f"To retire by {retirement_age} years old")
    print(f"This mean you will need to have invested a total of ${required_investment:,.0f} in {years_to_grow} years")
    
if __name__ == "__main__":
    while True:
        main()
        repeat = input("Would you like to calculate again? (yes/no)").lower()
        if repeat != "yes":
            print("Thanks for using the Retirement Calculator")
            break
 


        