class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 0
        self.TranferCash = False

    def register(self, name , password):
        cash = self.cash
        conditions = True

        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
            conditions = False

        if conditions == True:
            print("Account created successfully")
            self.client_details_list = [name , password , cash]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")


    def login(self, name , password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(password) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[2])
                self.name = name

            else:
                print("Wrong details")

    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(self.cash)))

            print("Amount Deposited Successfully")

        else:
            print("Please enter a valid amount")

    def subtract_cash(self, withdrawal):
        if withdrawal > 0 and withdrawal < self.cash:
            self.cash -= withdrawal
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")


            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(self.cash)))

            print("Amount Withdrawn Successfully")

        else:
            print("Please enter a valid amount")


    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(password)))
            print("new Password set up successfully")



if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcome to Quantum Financial Bank")
    print("1.Login")
    print("2.Creata a new Account")
    user = int(input("Please choose from one of the listed options: "))

    if user == 1:
        print("Logging in")
        name = input("Enter Name: ")
        password = input("Enter password: ")
        Bank_object.login(name, password)
        while True:
            if Bank_object.loggedin:
                print("1.Deposit")
                print("2.Withdrawal")
                print("3.Check Balance")
                print("4.Change Password")
                print("5.Logout")
                login_user = int(input())
                if login_user == 1:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)
                    print("\n1.back to main menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 2:
                    print("Balance =",Bank_object.cash)
                    withdrawal = int(input("Enter amount: "))
                    Bank_object.subtract_cash(withdrawal)
                    print("\n1.back to main menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break


                elif login_user == 3:
                    print("Balance =",Bank_object.cash)
                    print("\n1.back to main menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break



                elif login_user == 4:
                    print("1.Password change")
                    new_passwrod = input("Enter new Password: ")
                    Bank_object.password_change(new_passwrod)
                    print("\n1.back to main menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break


                elif login_user == 5:
                    break




    if user == 2:
        print("Creating A New Account")
        name = input("Enter Name: ")
        password = input("Enter Password: ")
        Bank_object.register(name, password)