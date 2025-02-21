salary=float(input("Please enter your salary for the month in $: "))
month=input("Please enter the name of the month: ")
savingsPercentage=float(input("Please enter the percentage for your savings: "))
rentPercentage=float(input("Please enter the percentage for your rent: "))
electricityPercentage=float(input("Please enter the percentage for your electricity: "))
savings=salary*(savingsPercentage/100)
print(f"Your savings are {savings} $")
rent=salary*(rentPercentage/100)
print(f"Your rent is {rent} $")
electricity=salary*(electricityPercentage/100)
print(f"Your electricity cost {electricity} $")


