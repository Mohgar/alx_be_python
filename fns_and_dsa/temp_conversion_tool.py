FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
temperature = int(input("Enter the temperature to convert: "))
F_or_C_question = input("Is this temperature in Celsius or Fahrenheit? (C/F) ").lower()
if F_or_C_question == 'f':
    convert_to_celsius(temperature)
    print(f"{temperature} °F is {convert_to_celsius(temperature)} °C")
elif F_or_C_question == 'c':
    convert_to_fahrenheit(temperature)
    print(f"{temperature} °C is {convert_to_fahrenheit(temperature)} °F")
else:
    print("Invalid temperature. Please enter a numeric value.")
