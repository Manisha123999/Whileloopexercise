while True:
    inches = float(input("Enter a length in inches (or a negative value to end): "))

    if inches < 0:
        print("Program ending. Goodbye!")
        break  # Exit the loop if the input is negative

    centimeters = inches * 2.54

    print(f"{inches} inches is equal to {centimeters:.2f} centimeters")
