AUDIT_TRANSACTION_COUNT = 0


def create_bank_account(owner_name, initial_balance):
    balance = float(initial_balance)
    history = [f"Account created with {balance}"]

    def deposit(amount):
        nonlocal balance, history
        global AUDIT_TRANSACTION_COUNT

        balance += amount
        history.append(f"deposit {amount}")
        AUDIT_TRANSACTION_COUNT += 1

    def withdraw(amount):
        nonlocal balance, history
        global AUDIT_TRANSACTION_COUNT

        if balance >= amount:
            balance -= amount
            history.append(f"withdraw {amount}")
            AUDIT_TRANSACTION_COUNT += 1
        else:
            raise ValueError("Insufficient balance")

    def get_statement():
        return (owner_name, balance, history.copy())

    return {
        "deposit": deposit,
        "withdraw": withdraw,
        "statement": get_statement
    }




print(AUDIT_TRANSACTION_COUNT)  # 0

acc = create_bank_account("Arham", 1000.0)

acc["deposit"](200.0)

acc["withdraw"](150.0)

try:
    acc["withdraw"](2000.0)
except ValueError as e:
    print(e)  

owner, bal, txn_history = acc["statement"]()

print(owner)
print(bal)
print(txn_history)

print(AUDIT_TRANSACTION_COUNT)
