print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
num_people = int(input("How many people to split the bill? "))
percentage_tip = int(
    input("What percentage tip would you like to give? 10, 12 or 15? ")
)

total_per_person = (total_bill + total_bill * (percentage_tip / 100)) / num_people

print(f"Each person should pay: ${round(total_per_person, 1)}")
