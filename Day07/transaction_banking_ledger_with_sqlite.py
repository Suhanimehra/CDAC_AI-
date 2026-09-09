import sqlite3
from datetime import datetime


class TransactionError(Exception):
    pass


class BankingLedger:

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

        
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_id TEXT PRIMARY KEY,
                holder_name TEXT,
                balance REAL
            )
        """)

        
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS audit_log (
                tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_acc TEXT,
                to_acc TEXT,
                amount REAL,
                timestamp TEXT
            )
        """)

        self.conn.commit()

    def create_account(
        self,
        account_id,
        holder_name,
        initial_deposit
    ):
        if initial_deposit < 0:
            raise ValueError(
                "Initial deposit cannot be negative"
            )

        self.conn.execute(
            """
            INSERT INTO accounts
            (account_id, holder_name, balance)
            VALUES (?, ?, ?)
            """,
            (
                account_id,
                holder_name,
                initial_deposit
            )
        )

        self.conn.commit()

    def transfer_funds(
        self,
        from_acc,
        to_acc,
        amount
    ):
        try:

            
            if amount <= 0:
                raise TransactionError(
                    "Transfer amount must be greater than zero"
                )

            
            cursor = self.conn.execute(
                """
                SELECT balance
                FROM accounts
                WHERE account_id = ?
                """,
                (from_acc,)
            )

            from_row = cursor.fetchone()

            if from_row is None:
                raise TransactionError(
                    f"Account {from_acc} does not exist"
                )

            
            cursor = self.conn.execute(
                """
                SELECT balance
                FROM accounts
                WHERE account_id = ?
                """,
                (to_acc,)
            )

            to_row = cursor.fetchone()

            if to_row is None:
                raise TransactionError(
                    f"Account {to_acc} does not exist"
                )

            
            from_balance = from_row[0]

            if from_balance < amount:
                raise TransactionError(
                    f"Insufficient funds in account {from_acc}"
                )

            
            self.conn.execute(
                """
                UPDATE accounts
                SET balance = balance - ?
                WHERE account_id = ?
                """,
                (amount, from_acc)
            )

            
            self.conn.execute(
                """
                UPDATE accounts
                SET balance = balance + ?
                WHERE account_id = ?
                """,
                (amount, to_acc)
            )

            
            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            self.conn.execute(
                """
                INSERT INTO audit_log
                (from_acc, to_acc, amount, timestamp)
                VALUES (?, ?, ?, ?)
                """,
                (
                    from_acc,
                    to_acc,
                    amount,
                    timestamp
                )
            )

            
            self.conn.commit()

        except TransactionError:

            self.conn.rollback()
            raise

        except Exception as e:
            
            self.conn.rollback()

            raise TransactionError(
                f"Transaction failed: {e}"
            )

    def get_balance(self, account_id):

        cursor = self.conn.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_id = ?
            """,
            (account_id,)
        )

        row = cursor.fetchone()

        if row is None:
            raise ValueError(
                f"Account {account_id} does not exist"
            )

        return row[0]

    def close(self):
        self.conn.close()



if __name__ == "__main__":

    bank = BankingLedger("bank.db")

    
    bank.create_account(
        "ACC101",
        "Arham",
        5000.0
    )

    bank.create_account(
        "ACC102",
        "Lisa",
        2000.0
    )

    
    bank.transfer_funds(
        "ACC101",
        "ACC102",
        1500.0
    )

    print(
        "ACC101:",
        bank.get_balance("ACC101")
    )

    print(
        "ACC102:",
        bank.get_balance("ACC102")
    )

    
    try:
        bank.transfer_funds(
            "ACC101",
            "ACC102",
            10000.0
        )

    except TransactionError as e:
        print(e)

    print(
        "ACC101:",
        bank.get_balance("ACC101")
    )

    print(
        "ACC102:",
        bank.get_balance("ACC102")
    )

    bank.close()