# Initialize variables
debt = 10000  # The total debt
payments = []  # List to store payment amounts

# Start input loop
while True:
    payment_order = input("Enter your paid part (if there are no more, enter 0 or 'none'): ")

    # Exit logic
    if payment_order == "0" or payment_order.lower() == "none":
        print("Exiting input loop.")
        break

    # Input validation and processing
    try:
        payment_order = float(payment_order)  # Convert input to a number
        if payment_order > 0:  # Only positive payments are valid
            payments.append(payment_order)  # Store the payment
            print(f"Payment recorded: {payment_order}")
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Print all recorded payments
print("\nPayments recorded:")
for recorded_payment in payments:
    print(recorded_payment)

# Remaining debt calculation (optional step for later)
remaining_debt = debt - sum(payments)
print(f"\nRemaining debt: {remaining_debt}")
