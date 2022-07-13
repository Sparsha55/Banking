
class User():
    def __init__(self, name, age , gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details:")
        print("name", self.name)
        print("age", self.age)
        print("gender", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super(). __init__(name, age, gender)
        self.balance= 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Your main balance is: ", self.balance)

    def withdrawl(self, amount):
        self.amount = amount

        if self.amount>self.balance:

             print("Insufficient fund, remaining balance is: ", self.balance)
        else:
             self.balance = self.balance - self.amount
             print("Successfully deposited. New balance is: ", self.balance)

    def view_balance(self):
        self.show_details()
        print("You have: ", self.balance)


D1 = Bank("Sparsha Pandey", 22, "Male")
D1.deposit(10000)
D1.withdrawl(500)
#D1.show_details()
D1.view_balance()




