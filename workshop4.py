class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
        
    def change_name(self, name):
        self.name = name
        
    def change_pin(self, pin):
        self.pin = pin
        
    def change_password(self, password):
        self.password = password
        

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    
    def show_balance(self):
        print(self.name, "has an acct bal of:", self.balance, "\n")
        
    def withdraw(self):
        amount = float(input("Enter Withdraw Amount: "))
        self.balance -= amount
    
    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        self.balance += amount
        
    def transfer_money(self, otherUser):
        pin = input("Enter PIN of transfering User: ")
        if self.pin == pin:
            amount = eval(input("Enter Transfer Amount: "))
            otherUser.balance = otherUser.balance + amount
            self.balance = self.balance - amount
            print("Succesful transfer, thank you for banking with us!\n")
            return True
        else:
            print("Inavalid PIN, Transaction canceled.\n")
            return False
            
    def request_money(self, otherUser):
        pin = input("Enter PIN of transfering user: ")
        if otherUser.pin == pin:
            passWord = input("Enter other user Password: ")
        else: 
            print("Inavalid PIN, Transaction canceled.\n")
            return False
        if self.password == passWord:
            amount = eval(input("Enter Transfer Amount: "))
            otherUser.balance = otherUser.balance - amount
            self.balance = self.balance + amount
            print("Success. Thank you for banking with us!\n")
            return True
        else: 
            print("Inavalid Password, Transaction canceled.")
            return False
    
        
        
""" Driver Code: Task 1 
Bob = User("Bob", "1234", "GreatPassword")
print(Bob.name)
print(Bob.pin)
print(Bob.password)
"""
""" Driver Code: Task 2 
Bob = User("Bob", "1234", "GreatPassword")
print(Bob.name)
print(Bob.pin)
print(Bob.password)
Bob.change_name("Bobby")
Bob.change_pin("8181")
Bob.change_password("NewPass9")
print(Bob.name)
print(Bob.pin)
print(Bob.password)
"""
""" Driver Code: Task 3 
Guy = BankUser("JohnDoe", "0909", "TopSecret")
print(Guy.name)
print(Guy.pin)
print(Guy.password)
print(Guy.balance)
"""
""" Driver Code: Task 4 
JohnDoe = BankUser("JD", "819", "HardGuess")
JohnDoe.show_balance()
JohnDoe.deposit()
JohnDoe.show_balance()
JohnDoe.withdraw()
JohnDoe.show_balance()
"""
""" Driver Code: Task 5 """
JohnDoe = BankUser("JD", "09", "pw1")
JaneDoe = BankUser("Jane", "90", "pw2")
JaneDoe.deposit()
JaneDoe.show_balance()
JohnDoe.show_balance()
JaneDoe.transfer_money(JohnDoe)
JaneDoe.show_balance()
JohnDoe.show_balance()
JaneDoe.request_money(JohnDoe)
JaneDoe.show_balance()
JohnDoe.show_balance()
