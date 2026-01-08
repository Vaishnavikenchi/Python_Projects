import datetime


name = "User"
balance = 20000
correct_pin = 9824
attempts = 3
daily_limit = 10000
withdrawn_today = 0
transactions = []


while attempts > 0:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("\nLogin Successful ")
        break
    else:
        attempts -= 1
        print("Invalid PIN . Attempts left:", attempts)

if attempts == 0:
    print("Card Blocked!")
    exit()


print(f"\nWelcome {name} to SmartVault ATM ")

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Mini Statement")
    print("5. Change PIN")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f" Current Balance: ₹{balance}")

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited ₹{amount}")
            print(" Deposit Successful")
        else:
            print("Invalid Amount")

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        if withdrawn_today + amount > daily_limit:
            print(" Daily withdrawal limit exceeded")
        elif amount <= balance:
            balance -= amount
            withdrawn_today += amount
            transactions.append(f"Withdrawn ₹{amount}")
            print(" Please collect your cash")
        else:
            print(" Insufficient Balance")

    elif choice == 4:
        print("\n Mini Statement")
        if not transactions:
            print("No transactions yet")
        else:
            for t in transactions[-5:]:
                print("-", t)

    elif choice == 5:
        old_pin = int(input("Enter old PIN: "))
        if old_pin == correct_pin:
            new_pin = int(input("Enter new PIN: "))
            correct_pin = new_pin
            print(" PIN changed successfully")
        else:
            print(" Incorrect old PIN")

    elif choice == 6:
        print("\nThank you for using SmartVault ATM ")
        print("Date:", datetime.datetime.now())
        break

    else:
        print(" Invalid Choice")
