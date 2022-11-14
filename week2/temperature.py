"""
CP1404/CP5632 - Practical
Temperature conversions
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
 print(MENU)
 choice = input(">>> ").upper()
 while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit : "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
    print("Thank you.")

def Celsius(celsius):
    return celsius * 9.0 / 5 + 32
def Fahrenheit(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

main()
