year = int(input("Please input a year: "))
if not year % 400 or not year % 4 and year % 100:
    print("This is a leep year.")
else:
    print("This is not a leap year.")