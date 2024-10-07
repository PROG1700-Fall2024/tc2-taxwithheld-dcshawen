"""
    Author: Dan Shaw w0190983
    Program: Tax Calculator
    Description: Calculates the total amount of tax withheld from an employee
"""

# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

PROV_TAX_RATE = 0.06
FED_TAX_RATE = 0.25
DEPENDENT_TAX_DEDUCTION = 0.02

def main():
    global PROV_TAX_RATE, FED_TAX_RATE, DEPENDENT_TAX_DEDUCTION
    greeting = "| TAX CALCULATOR |"
    print("-" * len(greeting))
    print(greeting)
    print("-" * len(greeting))
    
    # Gets input values from user
    while (employeeSalary := validateFloat(input("\tEnter the employee's weekly salary: "))) == None:
        print("Please enter a valid salary")

    while (dependents := validateInt(input("\tEnter the number of dependents: "))) == None:
        print("You must enter a valid number of dependents")

    provTaxWithheld = calculateValue(employeeSalary, PROV_TAX_RATE)
    fedTaxWithheld = calculateValue(employeeSalary, FED_TAX_RATE)
    dependentDeduction = 0

    if dependents > 0:
        dependentDeduction = employeeSalary * DEPENDENT_TAX_DEDUCTION * dependents

    totalTaxes =  provTaxWithheld + fedTaxWithheld - dependentDeduction
    totalTakehome = employeeSalary - (provTaxWithheld + fedTaxWithheld - dependentDeduction)

    print("""    Provincial Tax Withheld: ${0:.2f}
    Federal Tax Withheld: ${1:.2f}
    Depend Deduction for {2} dependents: ${3:.2f}
    Total Withheld: ${4:.2f}
    Total Take-Home: ${5:.2f}""".format(provTaxWithheld, fedTaxWithheld, dependents, dependentDeduction, totalTaxes, totalTakehome))

# Takes an input value and a modifier and multiplies them together
def calculateValue(inputValue, modifier):
    return inputValue * modifier

# Validates inputQuery as a number. Converts to int and returns converted value.
# Returns None if the user enters a non-number
def validateInt(inputQuery):
    try:
        return int(inputQuery)
    except:
        return None

# Validates whether inputQuery is a valid number by trying to convert to a float
# Returns the converted float if successfull and None if fails
def validateFloat(inputQuery):
    try:
        return float(inputQuery)
    except:
        return None        

if __name__ == "__main__":
    main()