import math

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")

selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

if selection.lower() == "investment".lower() :
    deposit = int(input("Please enter the amount of money you will be depositing: "))
    interest_rate_investment = float(input("Please enter your interest rate: ")) / 100
    time = int(input("Please enter the number of years you plan on investing: "))
    interest = input("Please enter whether you would like 'simple' or 'compound' interest: ")
    if interest.lower() == "simple".lower():
        total_amount = deposit *(1 + interest_rate_investment * time)
        print("Your total investment will be £ " + str(total_amount) + ".")

    elif interest.lower() == "compound".lower():
        total_amount = deposit * math.pow((1 + interest_rate_investment),time)
        print("Your total investment will be £ " + str(total_amount) + ".")

elif selection.lower() == "bond" :
    house_value = int(input("Please enter the current value of your house in pounds: "))
    interest_rate_bond = (float(input("Please enter your interest rate: ")) / 100) / 12
    months = int(input("Please enter the number of months you plan to take to repay the bond: "))

    repayment = (interest_rate_bond * house_value)/(1 - (1 + interest_rate_bond)**(-months))
    round_repayment = round(repayment,2)
    print("You will repay £" + str(round_repayment) + " each month.")

else:
    print("You have submitted an incorrect response.")