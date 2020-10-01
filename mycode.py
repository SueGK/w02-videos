# Initial balance of the bank account
initial_balance = 200

# Bank statement with all transactions for the past 6 months
statement = [[-119.02, -56.54, 1200, -80, -12.99, -550, -167.90, -5.58, -3.54, -9.99],
             [-138.32, -67.12, 1200, -80, -12.99, -268.10, -550, -92.90, -125.65],
             [-101.44, -48.83, -19.99, -92.12, 1200, -80, -67.33, -12.99, -550, -30.33],
             [-91.98, -45.65, -50, -9.99, 1200, -80, -414.22, -12.99, -550, -9.29, -67.12],
             [-159.53, -27.61, -168.45, 1200, -80, -12.99, -76.94, -550, -28.08, -27.89],
             [-141.97, 1200, -87.78, -80, -12.99, -67.92, -188.09, -550, -4.20, -13.68]]

# Your job: pay monthly 0.5% interest to this account.

# Update the account balance each month: OK!
# Calculate interest each month: OK!
# Pay the total interest (6 months) to the account:
# - pay the total (update the balance for the last month)
# - log that transaction into statement for 6th month.

def update_balance(month,start_balance):
    balance = start_balance + sum(month)
    return balance

def caculate_interest(balance, interest_rate):
    interest = 0.01 * balance * interest_rate
    return interest

def update_statement(initial_balance, statement, interest_rate):
    '''
    before For Loop一定要先定义balance, interest的初始值
    '''
    balance = initial_balance
    interest = 0
    for month in statement:
        '''
        balance = update_balance(month,initial_balance)
        错因：initial_balance是固定值200，但是我们是想依次加上每月最终的balance，
        是变动的值
        '''

        balance = update_balance(month, balance)
        interest = interest + caculate_interest(balance, interest_rate) 
    '''
    要log that transation(which is bank interest) into statement for 6th month
    '''
    statement[-1].append(interest)
    balance = balance + interest

    return statement, balance


print(update_statement(initial_balance, statement, 0.5))
