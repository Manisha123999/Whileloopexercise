while True:
    inches = float(input("Enter the length in inches (enter a negative value to quit): "))
    if inches < 0:
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")