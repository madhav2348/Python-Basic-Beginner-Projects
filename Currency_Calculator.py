def main():
    print("US  dollar to pounds \n")

    dollar = eval(input("enter amount"))

    pound = convert_to_pound(dollar)

    print("that is ", pound,"pounds")

convert_to_pound = lambda dollar: dollar * 0.83

main()