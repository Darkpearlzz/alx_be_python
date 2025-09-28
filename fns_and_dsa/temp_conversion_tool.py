FAHRENHEIT_TO_CELSIUS = (lambda f: (f - 32) * 5/9)
CELSIUS_TO_FAHRENHEIT = (lambda c: (c * 9/5) + 32)

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS(fahrenheit)

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT(celsius)

temp = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if unit == 'C':
    converted = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {converted:.14f}°F")

elif unit == 'F':
    converted = convert_to_celsius(temp)
    print(f"{temp}°F is {converted:.14f}°C")

else:
    print("Invalid temperature. Please enter a numeric value.")