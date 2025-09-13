monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = (monthly_income) - (monthly_expenses) 
print(f"Your monthly savings are: ${monthly_savings}")

annual_savings = monthly_savings * 12
annual_interest_rate = 0.05

interest_earned = annual_savings * annual_interest_rate
projected_annual_savings = annual_savings + interest_earned
print(f"Projected savings after one year, including interest, is: ${projected_annual_savings}") # The projected annual savings including interest