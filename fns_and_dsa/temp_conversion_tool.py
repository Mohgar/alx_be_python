FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    return fahrenheit


temperature = int(input("Enter the temperature to convert: "))
F_or_C_question = input("Is this temperature in Celsius or Fahrenheit? (C/F) ").lower()


if F_or_C_question == 'f':
    celsius_temp = convert_to_celsius(temperature)
    print(f"{temperature} °F is {celsius_temp} °C")
elif F_or_C_question == 'c':
    fahrenheit_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature} °C is {fahrenheit_temp} °F")
else:
    print("Invalid temperature. Please enter a numeric value.")



