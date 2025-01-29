class customer():
    def __init__(self,name,age,contactno):
        self.name = name
        self.age = age
        self.contactno = contactno
        
    
    def show_cus_details(self):
        print("")
        print("Your Details....!")
        print(" ")
        print(f"Name -{self.name}")
        print(f"Age - {self.age}")
        print(f"contactno - {self.contactno}")



class bank(customer):
    def __init__(self, name, age, contactno):
        super().__init__(name, age, contactno)
        self.balance = 0

    def check_balance(self):
        print(f"Your current balance is {self.balance}")
    
    def deposit_balance(self,amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Credited amount is {self.amount} and your total balance{self.balance}")

    def withdraw_balance(self,amount):
        self.amount = amount
        if self.amount < self.balance:
            print("Low balance in your Account")
        else:
            self.balance -= self.amount
            print(f"Debited {self.amount} from your Account Your bank balance is {self.balance}")
            

            
c1 = bank("shakeel",23,432432432432)

c1.show_cus_details()
c1.withdraw_balance(230)









            

            
    
