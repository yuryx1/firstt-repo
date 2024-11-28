
for i in range(5):

    year = int(input("enter a year: "))

    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        if year % 100 == 0 and year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is a not a leap year")


