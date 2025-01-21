

def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError or ValueError:
        print("division by zero not allowed")