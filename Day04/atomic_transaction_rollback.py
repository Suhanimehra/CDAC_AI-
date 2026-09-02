from copy import deepcopy

class AccountNotFoundError(Exception):
    pass

class OverdraftError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass


def process_transaction_batch(accounts, batch_list, log_path):

    copy_account=deepcopy(accounts)

    try: 
        for transaction in batch_list:

            acc=transaction["acc"]
            transaction_type=transaction["type"]
            amount=transaction["amt"]


            if acc not in accounts:
                raise AccountNotFoundError(f"Account '{acc}' not found.")
            
            if transaction_type not in ("deposit" , "withdraw"):
                raise InvalidTransactionError(f"Invalid transaction type '{transaction_type}'.")

            if amount <= 0: 
                raise InvalidTransactionError("Transaction amount must be positive.")

            if transaction_type=="withdraw":
                if accounts[acc]<amount:
                    raise OverdraftError( f"Insufficient funds. Account {acc} " f"has balance {accounts[acc]}, requested {amount}.")
            
            if transaction_type == "deposit":
                accounts[acc]+=amount
            elif transaction_type == "withdraw":
                accounts[acc]-=amount

                
    except Exception as e:
        accounts.clear()
        accounts.update(copy_account)    

        with open(log_path, "a") as file:
            file.write(
                f"[ROLLBACK] Batch aborted: "
                f"{type(e).__name__} - {e}\n"
            )

        # Send the original error back
        raise

    # Everything succeeded
    with open(log_path, "a") as file:
        file.write(
            f"[SUCCESS] Batch completed. "
            f"{len(batch_list)} transaction(s) processed.\n"
        )

    return accounts 
