n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
op = input("Choose the operation (+, -, *, /):")

match op:
    case "+":
        r = n1 + n2
        print(f"The result is {r}.")
    case "-":
        r = n1 - n2
        print(f"The result is {r}.")
    case "*":
        r = n1 * n2
        print(f"The result is {r}.")
    case "/":
        if n2 == 0:
            print("Cannot divide by zero.")
        else:
            r = n1 / n2
            print(f"The result is {r}.")
