# Programmer: KC 
# Helped By: 

# Function for bank that deposits, withdraws, and report the net result
transaction = int(input("How many transactions are there? "))
deep_amount = 0
with_amount = 0
for x in range(transaction):
    print("Is transaction", x + 1, "a deposit or withdrawal? {D?W} ")
    trans_type = str(input())
    while trans_type != 'D' and trans_type != 'W':
        print("Is transaction ", x + 1, "a deposit or withdrawal? {D/W}")
        trans_type = str(input()) 
    if trans_type == "D":
        deposit = float(input("How much is being deposited? "))
        deep_amount += deposit
    if trans_type == "W":
        withdraw = float(input("How much is being withdrawn? "))
        with_amount += withdraw
print("")
print(f"Deposits: ${deep_amount:.2f}")
print(f"Withdraws: ${with_amount:,.2f}")
print(f"Net Change: ${deep_amount - with_amount:.2f}")
        
        
    

