 # Programmer: KC 
# Helped By: 

# Function for bank that deposits, withdraws, and reports the net result
transaction = int(input("How many transactions are there? "))
deep_amount = 0
with_amount = 0
for x in range(transaction):
    trans_type = str(input(f"Is transaction {x + 1} a deposit or withdrawal? [D/W] "))
    while trans_type != 'D' and trans_type != 'W':
        print("Invalid choice! Try again.")
        trans_type = str(input(f"Is transaction {x + 1} a deposit or withdrawal? [D/W] "))
    if trans_type == "D":
        deposit = float(input("How much is being deposited? "))
        deep_amount += deposit
    if trans_type == "W":
        withdraw = float(input("How much is being withdrawn? "))
        with_amount += withdraw
print("")
print(f"Deposits: ${deep_amount:,.2f}")
print(f"Withdrawals: ${with_amount:,.2f}")
print(f"Net Change: ${deep_amount - with_amount:,.2f}")
        
        
    

