# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

people = int(input("Enter number of people: "))
bill = float(input("Enter amount of bill: "))
tip = int(input("Enter tip percentage (0-100): "))

people = float(people)
tip = float(tip)
total_per_person = "{:.2f}".format((bill / people) + (bill / people / 100 * tip))

print("Calculated bill including tip per person: $" + str(total_per_person))
