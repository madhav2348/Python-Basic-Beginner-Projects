def is_leap(year):
    if year % 4 ==0:
        if year % 100 ==0:
            if year % 400 ==0:

                print("Leap YEar!")
            else:
                print("NOT LEAP YEAR")
        else:
            print("Leap Year")
    else:
        print("Not leap year")

is_leap("enter the year")