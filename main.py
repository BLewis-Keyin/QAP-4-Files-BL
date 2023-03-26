# Program for creating insurance policies for customers
# Completed 3/21/2023
# Made by Brandon Lewis

# import libraries for use in the program
from datetime import date, timedelta
import time

today = date.today()
payment_day = today.replace(day=1) + timedelta(days=32)
payment_day = payment_day.replace(day=1)


# define constants from OSICDef.dat
f = open('OSICDef.dat', 'r')
POLICY_NUM = int(f.readline().strip())
BASE_PREMIUM = float(f.readline().strip())
RATE_DISCOUNT = float(f.readline().strip())
COST_LIB = float(f.readline().strip())
COST_GLASS = float(f.readline().strip())
COST_LOANER = float(f.readline().strip())
RATE_HST = float(f.readline().strip())
PROCESS_FEE = float(f.readline().strip())
f.close()


# define province list
provlist = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

# start of the program loop
while True:
    # user inputs for policy information
    print("Please input customer policy information below\n")

    # prompt the user for customer first name
    while True:
        c_first_name = input("Customer First Name:                        ").title()
        if len(c_first_name) == 0:
            print("ERROR: Nothing was entered, please try again.")
        elif c_first_name.replace("-", "").replace("'", "").isalpha() is False:
            print("ERROR: Name does not contain only letters")
        else:
            break

    # prompt the user for customer last name
    while True:
        c_last_name = input("Customer Last Name:                         ").title()
        if len(c_last_name) == 0:
            print("ERROR: Nothing was entered, please try again.")
        elif c_last_name.replace("-", "").replace("'", "").isalpha() is False:
            print("ERROR: Name does not contain only letters")
        else:
            break

    # prompt the user for customer address
    while True:
        c_address = input("Customer Address:                           ").title()
        if len(c_address) == 0:
            print("ERROR: Nothing was entered, please try again.")
        else:
            break

    # prompt the user for customer city
    while True:
        c_city = input("Customer City:                              ").title()
        if len(c_city) == 0:
            print("ERROR: Nothing was entered, please try again.")
        else:
            break

    # prompt the user for customer province
    while True:
        c_province = input("Enter customer province (XX):               ").upper()
        if len(c_province) > 2:
            print("ERROR: Province length exceeds maximum amount (2 characters)")
        elif len(c_province) == 0:
            print("ERROR: Nothing was entered")
        elif c_province not in provlist:
            print("ERROR: Invalid province")
        else:
            break

    # prompt the user for customer postal code
    while True:
        postcode = input("Enter customer postal code (X9X9X9):        ").upper().replace("-", "").replace(" ", "")
        if len(postcode) > 6:
            print("ERROR: Postal code length exceeds maximum amount (6 characters)")
        elif len(postcode) == 0:
            print("ERROR: Nothing was entered")
        elif postcode[0:5:2].isalpha() is False or postcode[1:6:2].isdigit() is False:
            print("ERROR: Invalid postal code format (X9X9X9)")
        else:
            break

    # prompt the user for customer phone number
    while True:
        c_phone_number = input("Enter customer phone number (10 digits):    ").replace("-", "").replace(" ", "").replace(
            "(", "").replace(")", "")
        if len(c_phone_number) != 10:
            print("ERROR: Phone number was not entered in a 10 digit format")
        elif c_phone_number.isdigit() is False:
            print("ERROR: Phone number does not contain only numbers")
        else:
            break

    # prompt the user for the numbers of cars being insured
    while True:
        try:
            num_car_ins = int(input("Number of cars insured:                     "))
            break
        except ValueError:
            print("ERROR: Invalid input, please try again.")

    # prompt the user for extra liability option
    while True:
        op_ex_liability = input("Optional Extra liability (Y/N):             ").upper()
        if not op_ex_liability == "Y" and not op_ex_liability == "N":
            print("ERROR: Invalid input, please use 'Y' or 'N'")
        else:
            break

    # prompt the user for glass coverage option
    while True:
        op_glass = input("Optional Glass Coverage (Y/N):              ").upper()
        if not op_glass == "Y" and not op_glass == "N":
            print("ERROR: Invalid input, please use 'Y' or 'N'")
        else:
            break

    # prompt the user for loaner car option
    while True:
        op_loaner = input("Optional Loaner Car (Y/N):                  ").upper()
        if not op_loaner == "Y" and not op_loaner == "N":
            print("ERROR: Invalid input, please use 'Y' or 'N'")
        else:
            break

    # prompt the user for customer payment type preference
    while True:
        pay_type = input("Full or monthly payment (F/M):              ").upper()
        if not pay_type == "F" and not pay_type == "M":
            print("ERROR: Invalid input, please use 'F' or 'M'")
        else:
            break

    # Calculations

    premium = BASE_PREMIUM
    if num_car_ins > 1:
        premium += (num_car_ins - 1) * (BASE_PREMIUM - (BASE_PREMIUM * RATE_DISCOUNT))
    extra_costs = 0
    if op_ex_liability == "Y":
        extra_costs += COST_LIB * num_car_ins
    if op_glass == "Y":
        extra_costs += COST_GLASS * num_car_ins
    if op_loaner == "Y":
        extra_costs += COST_LOANER * num_car_ins
    total_premium = premium + extra_costs
    hst = total_premium * RATE_HST
    total_cost = total_premium + hst
    monthly_payment = (total_cost + PROCESS_FEE) / 8

    # Printing and formatting of the inputs and calculations
    print()
    print(f" {'ONE STOP INSURANCE COMPANY':^42s}")
    print(f" {'Customer Insurance Policy Receipt':^42s}")
    print(f" ----------------------------------------- ")
    print(f" Name: {f'{c_first_name} {c_last_name}':<24s}")
    print(f" Phone: {c_phone_number}")
    print(f"   {c_address} ")
    print(f"   {c_city}, {c_province} ")
    print(f"   {postcode} ")
    print()
    print(f" Policy Number: {POLICY_NUM}")
    print(f" Vehicle amount: {num_car_ins}     Issued: {today} ")
    print(f"                               ---------- ")
    print(f" Premium Amount:               {f'${premium:>,.2f}':>10s} ")
    print(f" Extra Cost Amount:            {f'${extra_costs:>,.2f}':>10s} ")
    print(f" Total Premium:                {f'${total_premium:>,.2f}':>10s} ")
    print(f"                               ---------- ")
    print(f" HST:                          {f'${hst:>,.2f}':>10s}")
    print(f" Total Claim :                 {f'${total_cost:>,.2f}':>10s}")
    if pay_type == "M":
        print()
        print(f" Monthly Payment:              {f'${monthly_payment:>,.2f}':>10s}")
    print()

    # writes the policy information to Policies.dat
    with open('Policies.dat', 'a') as a:
        a.write(f"{str(POLICY_NUM)}, {today}, {c_first_name}, {c_last_name}, {c_address}, {c_city}, {c_province}, {postcode}, {c_phone_number}, {num_car_ins}, {op_ex_liability}, {op_glass}, {op_loaner}, {pay_type}, {total_premium}\n ")
        POLICY_NUM = POLICY_NUM + 1
        print("Saving policy information...")
        time.sleep(2)
        print("Policy information successfully saved.\n")
        time.sleep(1)

    # program end option, writes all constants back to OSICDef.dat if END is used
    program_end = input("Press any key to enter a new policy or type END to exit... :  ").upper()
    if program_end == "END":
        f = open('OSICDef.dat', 'w')
        f.write(f'{POLICY_NUM}\n')
        f.write(f'{BASE_PREMIUM}\n')
        f.write(f'{RATE_DISCOUNT}\n')
        f.write(f'{COST_LIB}\n')
        f.write(f'{COST_GLASS}\n')
        f.write(f'{COST_LOANER}\n')
        f.write(f'{RATE_HST}\n')
        f.write(f'{PROCESS_FEE}\n')
        f.close()

        exit()

