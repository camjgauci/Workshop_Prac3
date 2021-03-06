def cels_fahr():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))

def fahr_cels():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9.0
    print("Result: {:.2f} C".format(celsius))

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        cels_fahr()
    elif choice == "F":
        fahr_cels()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")


