

def safe_divide(numerator, denominator):
    import sys
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        sys.stdout.write("Error: Cannot divide by zero.")
    except ValueError:
        sys.stdout.write("Error: Please enter numeric values only.")
    else:
        sys.stdout.write(f"The result of the division is {result:.1f}")
