def main():
    print("monthly payement loan calculator \n")


    principal = float(input("enter loan ammount"))
    apr = float(input("enter loan annual rate intrest"))
    year =int(input("enter year"))
    montly_intrest = apr / 1200
    amount_of_month = year * 12
    monthly_payable = principal * montly_intrest /(1 - (1+ montly_intrest)**(-amount_of_month))


    print("monthly payement is  "+ str(monthly_payable))

main()
