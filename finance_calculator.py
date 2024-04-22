import math
# Finance calculator program to caculates monthly repayment 
# for bonds and Amount earned as interest after specified years for simple and copound interests.
print("\n \t\t Finance calculators \n")
print("\n investment - to calculate the amount of interest you'll earn on your investment \n")
print("\n bond - to calculate the amount you need pay on you home loan \n")
# prompts user to select 'investment' or 'bonds' 
selected_calculation = input("\n Enter either 'investment' or 'bond' from the menu above to proceed: ")
#case sensitive check for the entered string 
selected_calculation = selected_calculation.casefold()
# prompts user to enter details which are used to calculate and print the repayment value for bond 
if(selected_calculation == "bond" ):
    house_present_value = int(input("\n Enter present value of the house: "))
    loan_interest_rate = float(input("\n Enter the interest rate: "))
    loan_interest_rate = (loan_interest_rate/ 100)/12
    number_of_months_to_repay = int(input("\n Enter the number of months to repay: "))
    repayment_amount = ((loan_interest_rate * house_present_value)/(1 - ( 1+ loan_interest_rate) ** (- number_of_months_to_repay)))
    print("\n Amount you need to repay every month is £", round(repayment_amount, 2))  
# prompts user to enter details which are used to calculate and 
# print maturity amount after specified number of years
elif (selected_calculation == "investment" ):
    deposit_amount = int(input("\n Enter the deposit amount: "))
    deposit_interest_rate = float(input("\n Enter interest rate as digit without % symbol: "))
    deposit_int_rate = deposit_interest_rate / 100
    number_of_years_investing = int(input("\n Enter the number of years you are planning to deposit: "))
    interest= input("\n Enter if you want 'simple' or 'compound interest': ")   
#case sensitive check for the entered string    
    interest = interest.casefold()
# calculates and prints maturity amount based on simple interest    
    if interest == "simple":
        amount = (deposit_amount * (1 + (deposit_int_rate * number_of_years_investing)))
        print(f"\n The appropriate amount you will get after {number_of_years_investing} at {deposit_interest_rate} % interest rate is £{round(amount,2)}\n ")
# calculates and prints maturity amount based on compound interest 
    elif interest == "compound":
        amount = (deposit_amount * (math.pow(1 + deposit_int_rate, number_of_years_investing)))
        print(f"\n The appropriate amount you will get after {number_of_years_investing} year(s) at {deposit_interest_rate} % interest rate is £{round(amount,2)}\n ")   
# prints wrong input if anything other than simple or compound is entered
    else:
        print("\n wrong input")
# prints wrong input if anything other than investment or bond is entered
else:
    print("\n Wrong input ")