#Project 1 --> Income Tax Calculator
#Request --> The customer requests a program that computes a person’s income tax.

gross_income = float(input("Enter the gross income: "))
num_dependent = int(input("Enter the number of dependents: "))

#The income tax is 20% of the gross income after $10,000 deduction 
#and an $3,000 deduction for each dependent.
income_tax = (gross_income - 10000 - num_dependent * 3000) * 0.2

print(f'The income tax is ${income_tax}')