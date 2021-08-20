TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

grossincome = float(input("enter the gross income:"))
numDependents = int(input("Enter the number of dependents: "))

taxableIncome = grossincome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

print("The income tax is $" + str(round(incomeTax,2)))