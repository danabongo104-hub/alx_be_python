# This program calculates monthly savings and projects them over a year with compound interest.
# Varibales for initial savings, monthly contribution, and interest rate.

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

# calculate monthly savings.
monthly_savings = monthly_income - monthly_expenses

# calculate projected savings over a year with compound interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the result
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")

