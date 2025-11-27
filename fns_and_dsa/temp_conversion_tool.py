# Simple program to convert temperature between Celcius and Fahrenheit
# Conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    "Converts Fahrenheit to Celcius"
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius

def convert_to_fahrenheit(celcius):
    "Converts Celcius to Fahrenheit"
    fahrenheit = (celcius *CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

if __name__ == "__main__":
    # User input 
    temp = float(input("Enter the temperature value to convert: "))
    units = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")
    if units.upper() == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    elif units.upper() == 'F':
        converted = convert_to_celcius(temp)
        print(f"{temp}°F is {converted}°C")
    else:
        print("Invalid temperature. Please enter a numeric valu.")