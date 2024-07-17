def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        print(" it is not allowed to divide by zero")
    except ValueError:
        print("Non-numeric Input")
    else:
        print(f" Result: {result}")
