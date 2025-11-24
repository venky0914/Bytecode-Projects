#!/usr/bin/env python
# coding: utf-8

# In[2]:


pin = "2434"        
balance = 50000     
attempts = 3        

# PIN verification loop
while attempts > 0:
    user_pin = input("Enter your 4-digit PIN: ")

    if user_pin == pin:
        print("WELL COME !")

        while True:
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter your choice: ")

            # 1️ Check Balance
            if choice == "1":
                print(f"Your balance is: ₹{balance}")

            # 2️ Withdraw
            elif choice == "2":
                amount = int(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print(f"Withdrawal successful! New balance: ₹{balance}")

            # 3️ Deposit
            elif choice == "3":
                amount = int(input("Enter deposit amount: "))
                balance += amount
                print(f"Deposit successful! New balance: ₹{balance}")

            # 4️ Change PIN
            elif choice == "4":
                new_pin = input("Enter new 4-digit PIN: ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN changed successfully!")
                else:
                    print("PIN must be exactly 4 digits!")

            # 5️ Exit
            elif choice == "5":
                print("Thank you!")
                break  # Exit from menu loop

            else:
                print("Invalid choice! Please try again.")

        break  # Exit from the PIN loop after menu exit

    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password! {attempts} attempts left.")
        else:
            print("Your card has been BLOCKED!")
            break


# ###### 

# In[ ]:




