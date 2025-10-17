account_balance = 10000
withdrawal = 6000

if withdrawal <= account_balance:
    account_balance -= withdrawal
    print (f"Withdrawal successful. New balance: ${account_balance}")
else:
    print ("Insufficient funds!")