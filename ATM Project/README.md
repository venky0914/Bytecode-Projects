
# 🏦 Secure Banking ATM Console Application

## 📌 Project Overview
**Secure Banking ATM Console Application** is a console-based Python project that simulates the core functionality of a real bank ATM. The application is designed to be straightforward, exam-ready, and implemented using only `while` loops to practice control flow logic.

## 🎯 Project Objective
Create a fully functional ATM menu system that behaves like a real ATM using only `while` loops. The application should provide clear prompts and messages for the user and handle invalid operations gracefully.

## ✨Features
- 🔐 PIN verification (default correct PIN: `2004`)
- ❌Maximum **3 wrong attempts** → account/card gets blocked
- 📋Main menu after successful PIN entry:
  - Check Balance
  - Withdraw Money (must be multiples of 100; check for sufficient balance)
  - Deposit Money
  - Change PIN
  - Exit
- All operations keep running until user chooses **Exit**
- Proper user messages for every action and validation

## 🛠️ Tech Stack
- Python 3.x (no external libraries required)

## 📥  Installation
1. Clone the repository:
```bash
git clone https://https://github.com/venky0914/Bytecode-Projects
cd <ATM  project>
```

## 🔁 Typical flow:
1. Enter PIN. If correct, you are taken to the main menu.
2. Choose actions from the menu (check balance, withdraw, deposit, change PIN).
3. Withdrawals must be in multiples of 100 and the system checks for sufficient balance.
4. Deposit increases the balance.
5. The program loops until you select **Exit**.

## Example Behaviour
- After 3 invalid PIN attempts, the account should be blocked and the program should exit (or return to a blocked state).
- Withdraw should reject amounts that are not multiples of 100 or exceed the current balance.
- Change PIN should ask for the current PIN, then the new PIN (with confirmation if implemented).

## 📁 Project Structure (suggested)
```
.
├── atm_console.py      # Main Python program
├── README.md
└── assets/
    └── screenshot.png  # Example screenshot (see below)
```

## 📸 Screenshot:
<img width="1216" height="537" alt="Screenshot 2025-11-24 222622" src="https://github.com/user-attachments/assets/48107a90-9044-44b4-9608-e36ca241179e" />


<img width="1212" height="397" alt="Screenshot 2025-11-24 222649" src="https://github.com/user-attachments/assets/0a8335c0-79b0-4f6b-8fa8-196ecea51bdf" />





## How to Test
- Test PIN validation by entering correct and incorrect PINs.
- Test withdrawal logic with:
  - multiples of 100 (allowed)
  - non-multiples (rejected)
  - amounts greater than balance (rejected)
- Test deposit by adding funds and verifying balance update.
- Test PIN change flow and confirm old PIN no longer works.


## 👨‍💻 Author
Bommideni Venkateshwar

---
*Generated from the project requirements screenshot.*
