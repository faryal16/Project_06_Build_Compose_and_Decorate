# 4. Class Variables and Class Methods Assignment:
# Create a class Bank with a class variable bank_name.
# Add a class method change_bank_name(cls, name) that allows changing the bank name.
# Show that it affects all instances.


def run():
    class Bank:
        bank_name = "🏦 Default Bank"
        
        def __init__(self, account_holder):
            self.account_holder = account_holder

        @classmethod
        def change_bank_name(cls, name):
            cls.bank_name = f"🏦 {name}"

        def display(self):
            print(f"👤 Account Holder: {self.account_holder} | Bank: {self.bank_name}")

    # Create bank users
    user1 = Bank("Faryal")
    user2 = Bank("Junaid")

    # Display initial bank info
    print("\n--- Initial Bank Info ---\n")
    user1.display()
    user2.display()

    # Change bank name
    print("\n🔁 Changing bank name to Pakistan National Bank...\n")
    Bank.change_bank_name("Pakistan National Bank")
    user1.display()
    user2.display()

    # Change bank name again
    print("\n🔁 Changing bank name to Meezan Bank...\n")
    Bank.change_bank_name("Meezan Bank")
    user1.display()
    user2.display()

# call the main function
if __name__ == "__main__":
    run() 