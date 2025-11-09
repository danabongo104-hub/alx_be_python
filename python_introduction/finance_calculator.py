# This program calculates monthly savings and projects them over a year with compound interest.
# Varibales for initial savings, monthly contribution, and interest rate.

m_income = int(input("Enter your monthly income: "))
m_expenses = int(input("Enter your monthly expenses: "))

# calculate monthly savings.
m_savings = m_income - m_expenses

# calculate projected savings over a year with compound interest
projected_savings = m_savings * 12 + (m_savings * 12 * 0.05)

# Display the result
print(f"Your monthly savings are ${m_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")

