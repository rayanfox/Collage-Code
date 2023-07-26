def calculate_payment_schedule(purchase_price):
    down_payment = purchase_price * 0.10
    balance = purchase_price - down_payment
    rate = 0.12
    monthly_payment = (purchase_price - down_payment) * 0.05

    print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
    month = 1
    while balance > 0:
        interest = balance * rate / 12
        principal = monthly_payment - interest
        if balance < monthly_payment:
            monthly_payment = balance
            principal = balance - interest
            balance = 0
        else:
            balance -= principal

        # Explicitly set the balance to 0.00 if it becomes very close to zero
        if abs(balance) < 0.01:
            balance = 0.00

        print(f"{month:3d}    {balance:9.2f}       {interest:10.2f}      {principal:10.2f}     {monthly_payment:7.2f}   {balance:13.2f}")

        month += 1

def main():
    try:
        purchase_price = float(input("Enter the purchase price: "))
        if purchase_price <= 0:
            print("Please enter a valid positive purchase price.")
        else:
            calculate_payment_schedule(purchase_price)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
