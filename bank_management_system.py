import os

def clear_screen():
    os.system("cls")

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class Login_system:
    def __init__(self):
        self.users = []
        self.accounts = {}
        self.loan_enabled = True
        self.total_balance = 1000
        self.total_loan_amount = 0



    def Bank(self):
        self.accounts = {}
        self.total_balance= 0
        self.loan_enabled = True
        self.total_loan_amount = 0
    def Available_Balance(self, account_number):
        
        print("\t\t\tAvailable Balance : ",self.accounts[account_number]['balance'])
    def Bank_Balance(self):
        clear_screen()
        print("\n\t\t\t_______________________Bank Management System_______________________")
        print("\t\t\t\t_______________________Admin_______________________")
        print("\t\t\t\t_______________________Bank Balance_______________________\n")
        print(f'\t\t\tTotal Bank Balance --> {self.total_balance}')
    def Deposit_amount(self, account_number, amount):
        
        if amount > 0:
            self.accounts[account_number]['balance'] += amount
            self.total_balance += amount
            self.accounts[account_number]['transaction_history'].append(f'Deposit--> +{amount}')
            print("\n\t\t\t\t\t-------Deposit successful..!-------" )
        else:
            print("\n\t\t\t\t\t-------Deposit amount must be greater than 0-------")
    
    def Withdrawal_amount(self,account_number, amount):
        
        if amount > 0:
            if amount <= self.accounts[account_number]['balance']:
                self.accounts[account_number]['balance'] -= amount
                self.accounts[account_number]['transaction_history'].append(f'Withdrwal--> -{amount}')
                print("\n\t\t\t\t\t-------Withdrawal successful..!-------")
            else:
                print(f'\t\t\tYou don\'t have {amount} this mouch money in your account..!')
    
    def Transfer_Amount(self,account_number, recive_account_number, amount):
        
        if account_number in self.accounts and recive_account_number in self.accounts:
            sender_balance = self.accounts[account_number]['balance']
            if sender_balance >= amount:
                self.accounts[account_number]['balance'] -= amount
                self.accounts[recive_account_number]['balance'] +=amount

                self.accounts[account_number]['transaction_history'].append(f'Transaction To Account {recive_account_number}: -{amount} ')
                self.accounts[recive_account_number]['transaction_history'].append(f'Transaction From Account {account_number}: -{amount} ')
                print(amount,"\n\t\t\t\t\t-------Taka Transaction Successful..!-------")
            else:
                print(f'\t\t\tYou don\'t have {amount} this mouch money ih your account..!')
        else:
            print(f'\n\t\t\t\t\t-------The Account Holder Not Available-------')
    def Transaction_History(self, account_number):        
        if account_number in self.accounts:
            transaction_history = self.accounts[account_number]['transaction_history']
            print(f'\t\t\tTransaction History {account_number}')
            for transaction in transaction_history:
                print(transaction)
    def Take_lone(self,account_number):
        
        if account_number in self.accounts:
            if self.loan_enabled == True:
                account = self.accounts[account_number]
                loan_limit = account['balance']*2
                if loan_limit > account['loan_limit']:
                    account['loan_limit'] = loan_limit
                    account['loan_amount'] += loan_limit
                    self.total_loan_amount += loan_limit
                    account['transaction_history'].append(f'Loan: +{loan_limit}')
                    print(f'\t\t\t{loan_limit} taka loan successful')
                else:
                    print("\n\t\t\t\t\t-------Lone Limit Reached.-------")
            print(f'\t\t\tLoan feature is currently disabled by the admin')
        else:
            print("\n\t\t\t\t\t-------Account Holder Not Available.-------")
    def Total_loan_amount(self):
        
        print(f'\t\t\tTotal Loan amout {self.total_loan_amount}')
    def Create_account(self, email, password, is_admin=False):
        user = User(email, password)
        self.users.append((user, is_admin))
        account_number = len(self.users)
        self.accounts[account_number] = {
            'name': email,
            'balance': 0,
            'loan_amount': 0,
            'loan_limit': 0,
            'transaction_history': []
        }
        print("\n\t\t\t\t-------Account Created Successfully! ACC_NM->",account_number,"-------")
        return account_number


    def Login(self, email, password):

        for index, (user, is_admin) in enumerate(self.users):
            if user.email == email and user.password == password:
                if is_admin:
                    clear_screen()
                    print("\n\t\t\t_______________________Bank Management System_______________________\n")
                    print("\t\t\t\t_______________________Admin_______________________\n")
                    print("\t\t\t1--> Available Balance.")
                    print("\t\t\t2--> Total Loan Amount.")
                    print("\t\t\t3--> Off The Loan Feature.")
                    opt = int(input("\t\t\tWaiting for your option: "))
                    if opt == 1:
                        clear_screen()
                        print("\n\t\t\t_______________________Bank Management System_______________________")
                        print("\t\t\t\t_______________________Admin_______________________")
                        print("\t\t\t\t_______________________Bank Balance_______________________\n")
                        self.Bank_Balance()
                    elif opt == 2:
                        clear_screen()
                        print("\n\t\t\t_______________________Bank Management System_______________________")
                        print("\t\t\t\t_______________________Admin_______________________")
                        print("\t\t\t\t_______________________Loan_______________________\n")
                        self.Total_loan_amount()
                    elif opt == 3:
                        clear_screen()
                        print("\n\t\t\t_______________________Bank Management System_______________________")
                        print("\t\t\t\t_______________________Admin_______________________")
                        print("\t\t\t\t_______________________Loan Feature_______________________\n")
                        OFF_ON = input("\t\t\t-----Do you want to turn [F/N] : ")
                        if OFF_ON.lower() == 'f':
                            self.loan_enabled = False
                        elif OFF_ON.lower() == 'n':
                            self.loan_enabled = True
                    else:
                        print("\n\t\t\t\t\t-------Invalid option!-------")
                else:
                    account_number = index + 1 
                    clear_screen()
                    print("\n\t\t\t_______________________Bank Management System_______________________")
                    print("\t\t\t\t_______________________User_______________________\n")
                    print("\t\t\t1--> Available Balance.")
                    print("\t\t\t2--> Deposit Amount.")
                    print("\t\t\t3--> Withdrawal Amount.")
                    print("\t\t\t4--> Transfer Amount.")
                    print("\t\t\t5--> Check Transaction History.")
                    print("\t\t\t6--> Take a Loan.")
                    opt = int(input("\t\t\tWaiting for your option: "))
                    if opt == 1:
                        clear_screen()
                        print("\n\t\t\t_______________________Bank Management System_______________________")
                        print("\t\t\t\t_______________________User_______________________")
                        print("\t\t\t\t_______________________Balance_______________________\n")
                        self.Available_Balance(account_number) 
                    elif opt == 2:
                        clear_screen()
                        print("\n\t\t\t_______________________Bank Management System_______________________")
                        print("\t\t\t\t_______________________User_______________________")
                        print("\t\t\t\t_______________________Deposit_______________________\n")
                        amount = float(input("\t\t\tEnter the Deposit Amount: "))
                        self.Deposit_amount(account_number, amount)    
                    elif opt == 3:
                        clear_screen()
                        print("\n\t\t\t_______________________Bank Management System_______________________")
                        print("\t\t\t\t_______________________User_______________________")
                        print("\t\t\t\t_______________________Withdrawal_______________________\n")
                        amount = float(input("\t\t\tEnter the Withdrawal Amount: "))
                        self.Withdrawal_amount(account_number, amount)
                    elif opt == 4:
                        clear_screen()
                        print("\n\t\t\t_______________________Bank Management System_______________________")
                        print("\t\t\t\t_______________________User_______________________")
                        print("\t\t\t\t_______________________Transfer_______________________\n")
                        recive_account_number = int(input("\t\t\tEneter The Account number: "))
                        amount = int(input("\t\t\tEnter The Amount: "))
                        self.Transfer_Amount(account_number,recive_account_number,amount)
                    elif opt == 5:
                        clear_screen()
                        print("\n\t\t\t_______________________Bank Management System_______________________")
                        print("\t\t\t\t_______________________User_______________________")
                        print("\t\t\t\t_______________________History_______________________\n")
                        self.Transaction_History(account_number)
                    elif opt == 6:
                        clear_screen()
                        print("\n\t\t\t_______________________Bank Management System_______________________")
                        print("\t\t\t\t_______________________User_______________________")
                        print("\t\t\t\t_______________________Loan_______________________\n")
                        self.Take_lone(account_number)
                    else:
                        print("\n\t\t\t\t\t-------Invalid option!-------")
                return
        print("\n\t\t\t\t\t-------Invalid email/password!-------")


login_system = Login_system()

while True:
    clear_screen()
    print("\n\t\t\t_______________________Bank Management System_______________________\n")
    print("\t\t\t1--> Sign In.")
    print("\t\t\t2--> Sign Up.\n")
    opt = int(input("\t\t\tWaiting for your option: "))

    if opt == 1:
        clear_screen()
        print("\n\t\t\t_______________________Bank Management System_______________________")
        print("\t\t\t\t_______________________Sing In_______________________\n")
        email = input("\n\n\t\t\tEnter Your Email: ")
        password = input("\t\t\tEnter Your Password: ")
        login_system.Login(email, password)

    elif opt == 2:
        clear_screen()
        print("\n\t\t\t_______________________Bank Management System_______________________")
        print("\t\t\t\t_______________________SiNg Up_______________________\n")
        email = input("\t\t\tEnter New Email: ")
        password = input("\t\t\tEnter Your Password: ")
        user_type = int(input("\t\t\t\t1--> for admin\n\t\t\t\t2--> for normal user\n\t\t\t\tWaiting for your option: "))

        if user_type == 1:
            login_system.Create_account(email, password, is_admin=True)

        elif user_type == 2:
            login_system.Create_account(email, password, is_admin=False)

        else:
            print("\n\t\t\t\t\t-------Invalid user type!-------")

    again = input("\n\t\t\t\t-------Do you want to exit? [Y/N]: ")

    if again.lower() == 'y':
        break
