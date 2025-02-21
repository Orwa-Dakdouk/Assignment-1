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
spendings=savings + rent + electricity
remainder= salary - spendings
print(f"You spent {spendings} $")
print(f"You have {remainder} $ left")
yearlyPayment= 12*(rent + electricity)
print(f"You pay {yearlyPayment} $ yearly for rent and electricity")
print(f"Your salary raised to the power of 2 is {salary**2} $")
answer=input("Do you have any extra amount that you take(yes or no): ")
if answer.lower()=="yes":
    extraAmount=float(input("Enter the extra amount in $: "))
    savings=(salary*(savingsPercentage/100)) + extraAmount
    print(f"Your savings are {savings} $")
    print("Exiting Program...")
else:
    print("Exiting Program...")






