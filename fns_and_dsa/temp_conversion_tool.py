def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

try:
    current_temp = float(input("Enter the temperature to convert: "))
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if temp_unit == "C":
        converted = convert_to_fahrenheit(current_temp)
        print(f"{current_temp}°C is {converted:.2f}°F")
    elif temp_unit == "F":
        converted = convert_to_celsius(current_temp)
        print(f"{current_temp}°F is {converted:.2f}°C")
    else:
        print("Invalid temperature unit. Please enter C or F.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
