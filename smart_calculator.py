import math

last_result = None  # Store the last result

while True:
    print("\nSimple Calculator")
    print("Type 'exit' to quit. Type 'ANS' to reuse the last answer.")

    first_input = input("Enter the first number: ")
    if first_input.lower() == "exit":
        print("Goodbye!")
        break

    # Use ANS if typed
    if first_input.upper() == "ANS":
        if last_result is not None:
            first = last_result
        else:
            print("No previous answer available.")
            continue
    else:
        try:
            first = float(first_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

    operation = input("Choose an operation (+, -, *, /, %, //, **, sqrt): ")
    if operation.lower() == "exit":
        print("Goodbye!")
        break

    if operation != "sqrt":
        second_input = input("Enter the second number: ")
        if second_input.lower() == "exit":
            print("Goodbye!")
            break

        if second_input.upper() == "ANS":
            if last_result is not None:
                second = last_result
            else:
                print("No previous answer available.")
                continue
        else:
            try:
                second = float(second_input)
            except ValueError:
                print("Please enter a valid number.")
                continue

    # Perform operations
    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        result = first / second if second != 0 else "Error: You can't divide by zero!"
    elif operation == "**":
        result = first ** second
    elif operation == "%":
        result = first % second
    elif operation == "//":
        result = first // second
    elif operation == "sqrt":
        result = math.sqrt(first)
    else:
        result = "Invalid operation!"

    print("The result is:", result)

    # Save result if it's a number
    if isinstance(result, (int, float)):
        last_result = result
