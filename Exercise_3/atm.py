cust_dict = {}

class Customer:
    """
    A customer object is used to track each of the bank's customers. Each customer
    has a unique, six character identifier.

    """

    def __init__(self, name, cust_id, street, city, state, zip, pin):
        # Create a new customer object. Save all of the information provided.
        self.name = name  # Customer's name, e.g. John A. Doe
        self.cust_id = cust_id  # A unique 6 digit value, e.g. 123456
        self.street = street  # Street address where statements are mailed
        self.city = city
        self.state = state  # Two character state, e.g. NY and NJ
        self.zip = zip  # 5 digit postal zip code
        self.pin = pin  # 4 character pin number for authentication
        self.accts = {}
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
        if acct_type == "savings":
            acct_id = f"{self.cust_id}{self.num_s_accts}0"  # Build account id.
            self.num_s_accts += 1  # Increment savings account counter
        else:  # Checking account
            acct_id = f"{self.cust_id}{self.num_c_accts}9"  # Build account id.
            self.num_c_accts += 1  # Increment checking accounts counter
        # print(self.cust_id, acct_id, acct_type)
        new_acct = Account(self.cust_id, acct_id, acct_type)  # Create new account object
        self.accts[acct_id] = new_acct  # Save new account id and object
        new_acct.deposit(amount)  # Make an initial deposit


    def print_cust(self):
        print('Name: ' + self.name)
        print('Customer number: ' + self.cust_id)
        #  for current_cust in self.accts:

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
        self.acct_id = acct_id
        self.cust_id = cust_id
        self.acct_type = acct_type
        self.balance = 0.0
        return

    def withdraw(self, transaction_amt):
        if self.balance < transaction_amt:  # Sufficient funds?
            print(f'Insufficient funds. Current balance is ${self.balance:.2f}.')
        else:
            self.balance -= transaction_amt  # Decrement balance by withdrawal amount
            print(f"Amount of withdrawal is ${transaction_amt:.2f}")
            print(f"New balance is: ${self.balance:.2f}")

    def deposit(self,transaction_amt):
        self.balance += transaction_amt  # Increment balance by amount of deposit

    def get_balance(self):
        print("The current balance in your account is: $" + f"{self.balance:.2f}")

def load_db():

    """
    The purpose of this function is to load the internal data structures with a small amount of
    test data.  Initial contents of data structures displayed to facilitate
    testing.
    :return:
    """
    new_cust = Customer('Susan Lynch', '123456', '100 E. 21st St.', 'New York', 'NY', 10010, '1555')
    cust_dict["123456"] = new_cust  # Save customer id and customer object
    new_cust.open_acct("savings", 500.00)
    new_cust.open_acct("checking", 1000.00)
    print("123456 savings 12345600 pin= 1555")
    print("123456 checking 12345609")

    new_cust = Customer('Karen Widing', '567899', '65 Prospect St.', 'New Paltz', 'NY', '12561', '9999')
    cust_dict["567899"] = new_cust  # Save customer id and customer object
    new_cust.open_acct("checking", 750.00)
    print("567899 checking 56789909 pin=9999")

def main():
    load_db()  # Load test data
    while True:
        inp_cust = input("\nPlease enter your bank customer number: ")
        if inp_cust in cust_dict:  # Valid customer id?
            inp_pin = input("Please enter your customer pin: ")
            if cust_dict[inp_cust].validate(inp_pin):  # Valid pin?
                acct = input("Please enter your account number: ")  # Pin valid. Get account number.
                if acct in cust_dict[inp_cust].accts:  # Valid account number for customer?
                    # So far so good. Get transaction type.
                    trans = input("Enter transaction type (d, w or b): ")
                    if trans == 'd':  # Customer is making a deposit
                        d_amt = float(input('Please enter the amount of your deposit: '))
                        cust_dict[inp_cust].accts[acct].deposit(d_amt)  # Make a deposit
                    elif trans == 'b':  # Customer wants the current balance
                        cust_dict[inp_cust].accts[acct].get_balance()  # Get the current balance
                    elif trans == 'w':  # Make a withdrawal
                        w_amt = float(input('Please enter withdrawal amount: '))
                        cust_dict[inp_cust].accts[acct].withdraw(w_amt)
                    else:  # Invalid transaction type. This is likely a typo.
                        print('Invalid transaction type entered. Enter d, w or b.')
                else:
                    print("The account number entered is invalid. Try again or see teller")
            else:
                print('Incorrect pin. Try again.')

        else:
            print('Invalid customer number. Try again.')

if __name__ == "__main__":
    # execute only if run as a script
    main()