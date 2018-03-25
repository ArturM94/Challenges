meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())

tip = meal_cost * tip_percent / 100
tax = meal_cost * tax_percent / 100
total_cost = meal_cost + tip + tax
round_total_cost = round(total_cost, 0)
int_total_cost = int(round_total_cost)

# With % operator
print('The total meal cost is %s dollars.' % int_total_cost)
# With f-strings
print(f'The total meal cost is {int_total_cost} dollars.')
