
import datetime
cust_dict = {}  # Customer dictionary.  Key is the six digit customer key. Value is the corresponding customer object.

class Customer:
    """
    A customer object is used to track each of the bank's customers. Each customer
    has a unique, six digit identifier. Construct the customer object.

    """

    def __init__(self, name, cust_id, street, city, state, zipcode, pin):
        # Create a new customer object. Save all of the information provided.
        self.name = name  # Customer's name, e.g. John A. Doe
        self.cust_id = cust_id  # A unique 6 digit value, e.g. 123456
        self.street = street  # Street address where statements are mailed
        self.city = city
        self.state = state  # Two character state, e.g. NY and NJ
        self.zipcode = zipcode  # 5 digit postal zip code
        self.pin = pin  # 4 character pin number for authentication
        self.accts = {}  # Dictionary where key is account number and value is account object
        self.num_s_accts = 0  # Number of savings accounts. Used to build acct id.
        self.num_c_accts = 0  # Number of checking accounts. Used to build acct id.


    def open_acct(self, acct_type, amount):
        """
        Open a new account of the specified type. Supported types are checking and savings.
        Deposit the specified amount in the new account.

        :param acct_type:
        :param amount:
        :return:
        """
        if acct_type == "Savings":
            #  Account ids are 8 digits. First 6 are the customer id. Last digit, 0=savings, 9=checking
            acct_id = f"{self.cust_id}{self.num_s_accts}0"  # Build account id.
            self.num_s_accts += 1  # Increment savings account counter
        else:  # Checking account
            acct_id = f"{self.cust_id}{self.num_c_accts}9"  # Build account id.
            self.num_c_accts += 1  # Increment checking accounts counter
        # print(self.cust_id, acct_id, acct_type)
        new_acct = Account(self.cust_id, acct_id, acct_type)  # Create new account object
        self.accts[acct_id] = new_acct  # Save new account id and account object
        new_acct.deposit(amount)  # Make an initial deposit


    def print_cust(self):
        """
        Print a statement containing a description of the customer, e.g. name,
        a list of the customer's accounts and recent account activity.

        :return:
        """
        print('\nName: ' + self.name)
        print('Customer number: ' + self.cust_id)
        print("Address: " + self.street + ", " + self.city + ", " + self.zipcode)
        print("\nAccounts:")

        # Read transaction log. A single log file is used for all customers and accounts.
        with open('transactions.txt', 'r') as trans_hist:
            history = trans_hist.readlines()  # history is a list with one entry for each logged transaction.

        for key, value in self.accts.items():  # accts is a list of the all account objects for one customer
            print(f"\nAccount: {key} Type: {value.acct_type} Balance: ${value.balance:.2f}")

            #  Split each log entry into the component parts. Parts are account id, customer id, timestamp,
            #  transaction type, transaction amount and balance after processing the transaction.
            t_lst=[]
            for trans in history:
                temp_lst = trans.rstrip().split('\t')  # Log entry is a tab delimited. Split entry into parts.
                if temp_lst[0] == key:  # Compare the account id in the log entry with the current account id.
                    t_lst.append(temp_lst)
            t_lst.reverse()  # Log entries should be sorted from newest to oldest.

            #  Print out log entries for the current account. Most recent entry prints first.
            for details in t_lst:
                print(f'\t\t{details[2]}\t{details[3]:10}\t{details[4]:>10}\t{details[5]:>10}')


    def validate(self, inp_pin):
        """
        Compare the pin number entered by the customer at the ATM to the stored value.
        :param inp_pin:
        :return:
        """
        if self.pin == inp_pin:
            return True  # Successful verification
        else:
            return False  # Unsuccessful verification


class Account:

    def __init__(self, acct_id, cust_id, acct_type):

        """
        An account object is used to track each account at the bank.
        :param acct_id:
        :param cust_id:
        :param acct_type:
        """
        self.acct_id = acct_id  #  Eight digit account identifier.
        self.cust_id = cust_id  #  Six digit customer identifier.
        self.acct_type = acct_type  # Checking or Savings
        self.balance = 0.0  #  Balance in the account
        return

    def withdraw(self, transaction_amt):
        """
        Withdraw the specified amount of money from this account. Issue a message if insufficient funds. Print balance
        after the transaction is processed. Write transaction information to the log file.

        :param transaction_amt:
        :return:
        """
        if self.balance < transaction_amt:  # Sufficient funds?
            print(f'Insufficient funds. Current balance is ${self.balance:.2f}.')
        else:
            self.balance -= transaction_amt  # Decrement balance by withdrawal amount
            print(f"Amount of withdrawal is ${transaction_amt:.2f}")
            print(f"New balance is: ${self.balance:.2f}")
            ttime = datetime.datetime.now().isoformat()[:16]  # Get timestamp w/o seconds or milliseconds
            trans_hist = open('transactions.txt', 'a')  # Open transactions file
            trans_hist.write(f'{self.cust_id}\t{self.acct_id}\t{ttime}\tWithdrawal\t{transaction_amt:.2f}\t{self.balance:.2f}\n')
            trans_hist.close()   # Close the transactions file

    def deposit(self,transaction_amt):
        """
        Deposit the specified amount of money in this account.
        :param transaction_amt:
        :return:
        """

        self.balance += transaction_amt  # Increment balance by amount of deposit
        ttime = datetime.datetime.now().isoformat()[:16]  #  Get timestamp w/o seconds or milliseconds
        print(f"Amount of deposit is ${transaction_amt:.2f}")
        print(f"New balance is: ${self.balance:.2f}")
        trans_hist = open('transactions.txt', 'a')  # Open transactions file
        trans_hist.write(f'{self.cust_id}\t{self.acct_id}\t{ttime}\tDeposit\t{transaction_amt:.2f}\t{self.balance:.2f}\n')
        trans_hist.close()   # Close the transactions file
        
    def get_balance(self):
        """
        Print the amount of money in the current account.

        :return:
        """
        print(f'The current balance in your account is: ${self.balance:.2f}')

def load_db():

    """
    The purpose of this function is to load the internal data structures with a small amount of
    test data.  Initial contents of data structures displayed to facilitate
    testing.
    :return:
    """
    new_cust = Customer('Susan Lynch', '123456', '100 E. 21st St.', 'New York', 'NY', '10010', '1555')
    cust_dict["123456"] = new_cust  # Save customer id and customer object
    new_cust.open_acct("Savings", 500.00)
    new_cust.open_acct("Checking", 1000.00)

    new_cust = Customer('Karen Widing', '567899', '65 Prospect St.', 'New Paltz', 'NY', '12561', '9999')
    cust_dict["567899"] = new_cust  # Save customer id and customer object
    new_cust.open_acct("Checking", 750.00)
    new_cust.open_acct("Savings", 750.00)

def main():
   

    load_db()  # Load test data
    while True:
        #
        #  Get customer number and pin. Validate both.
        #
        inp_cust = input("\nPlease enter your bank customer number or x: ")
        if inp_cust == 'x':
            exit()
        if not inp_cust in cust_dict:
            print('Invalid customer number. Try again.')
            continue
        inp_pin = input("Please enter your customer pin or x: ")
        if inp_pin == 'x':
            exit()
        if not cust_dict[inp_cust].validate(inp_pin):  # Valid pin?
            print('Invalid pin. Please try again.')
            continue
        #
        #  Customer id and pin validated. Get transaction type.
        #
        while True:
            print('Deposit(d), withdrawal(w), transfer(t), balance(b), statement(s) or exit(x)?')
            trans = input("Enter transaction type (d, w, t, b, s or x): ")
            if trans in ['d', 'w', 't', 'b', 's', 'x']:
                break
            print('Invalid transaction type entered.')
        if trans == 'x':
            exit()
        elif trans == 's':
            cust_dict[inp_cust].print_cust()
        else:
            while True:
                acct = input("Please enter your account number or x: ")  # Pin valid. Get account number.
                if acct == 'x':
                    exit()
                if acct in cust_dict[inp_cust].accts:  # Valid account number for customer?
                    break
                print("Invalid account number specified")
            #
            #  Begin processing the requested transaction type.
            #
            if trans == 'd':  # Customer is making a deposit
                d_amt = float(input('Please enter the amount of your deposit: '))
                cust_dict[inp_cust].accts[acct].deposit(d_amt)  # Make a deposit

            elif trans == 'b':  # Customer wants the current balance
                cust_dict[inp_cust].accts[acct].get_balance()  # Get the current balance

            elif trans == 'w':  # Make a withdrawal
                w_amt = float(input('Please enter withdrawal amount: '))
                cust_dict[inp_cust].accts[acct].withdraw(w_amt)
            else:  # Transfer
                while True:
                    acct2 = input("Please enter the receiving account number or x: ")  # Pin valid. Get account number.
                    if acct2 == 'x':
                        exit()
                    if acct2 in cust_dict[inp_cust].accts:  # Valid account number for customer?
                        break
                t_amt = float(input('Please enter the amount of your transfer: '))
                cust_dict[inp_cust].accts[acct].withdraw(t_amt)
                cust_dict[inp_cust].accts[acct2].deposit(t_amt)  # Deposit in receiving account

if __name__ == "__main__":

    main()