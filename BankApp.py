#Banking application code

customerNames = ['Clint Eastwood', 'James Bond', 'Miyamoto Musashi', 'Hiko seijuro', 'Pai Mei']
customerPins = ['1234', '5678', '9101', '1121', '3141']
customerBalances = [60000000, 7000000, 30000, 20000, 99999]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

# Visual aid for customer
while True:
    print("_____________________________________")
    print("       ----Soloman's Bank----        ")
    print("+++++++++++++++++++++++++++++++++++++")
    print("||| 1. Open an account            |||")
    print("||| 2. Withdrawal                 |||")
    print("||| 3. Deposit                    |||")
    print("||| 4. Check Balances             |||")
    print("||| 5. Exit                       |||")
    print("+++++++++++++++++++++++++++++++++++++")
#User's choice number selection
    choiceNumber = input("Please make a number selection from the table above : ")
    if choiceNumber == "1":
        print("Choice 1: 'Open an account'")
        #how many users of an account
        NOC = eval(input("Please enter the number of account owners (max 2 per account) : "))

        i = i + NOC
        #Restriction of 2 users per account
        if i > 2:
            print("\n")
            print("The maximum number of customers per account is 2")
            i = i - NOC
        else:
            #loop depending on number of customers
            while counter_1 <= i:
                #customer info taken and added to the list
                name = input("Please input your full name : ")
                customerNames.append(name)
                pin = str(input("Please input a security pin number : "))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("Please state your initial deposit : "))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("Pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(customerBalances[counter_2], end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour name has been added")
                print("Your pin has been added")
                print("Your balance has been added")
                print("----Your new account has been created----")
                print(customerNames)
                print("========================================")
                #End of function user message
        mainMenu = input("To exit or continue using this service press enter")
    elif choiceNumber == "2":
        j = 0
        print("Choice 2: Withdrawal")
        #Loop to control access to account
        while j < 1:
            k = -1
            name = input("Please input your full name : ")
            pin = input("Please input your security pin number : ")

            while k < len(customerNames) - 1:
                k = k + 1
                #matching of name and pin
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        #show balance from list
                        print("Current Balance is:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        #asks user for withdrawal amount
                        withdrawal = eval(input("Please enter the amount you would like to Withdraw : "))
                        #
                        if withdrawal > balance:
                            #if withdrawal amount greater than account balance.

                            print ("You cannot withdraw more than the balance of your account : ")

                        else:
                            #withdrawal subtraction
                            balance = balance - withdrawal
                            #update account info and display
                            print("\n")
                            print("----Withdrawal Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            #statement if name and pin don't match
            if j < 1:

                print("Your pin is incorrect\n")
                break
            #End of function user message
        mainMenu = input("To exit or continue using this service press enter ...")
    elif choiceNumber == "3":
        print("Choice 3: Deposit")
        n = 0

        while n < 1:
            k = -1
            name = input("Please input your full name : ")
            pin = input("Please input your security pin number : ")

            while k < len(customerNames) - 1:
                k = k + 1
                #matching of name and pin
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        #show balance then updated balance
                        print("Current Balance is: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        #Take deposit amount
                        deposition = eval(input("Enter the amount you want to deposit : "))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("----Deposit successful!----")
                        print("New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your pin is incorrect\n")
                break
            #End of function user message
        mainMenu = input("To exit or continue using this service press enter ...")
    elif choiceNumber == "4":
        print("Choice 4 : Check Balances")
        k = 0
        print("Customers balances listed below : ")
        print("\n")
        #Show all customer balances
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
            #End of function user message
        mainMenu = input("To exit or continue using this service press enter ...")
    elif choiceNumber == "5":
        #Exit app messages
        print("Choice 5: Exit")
        print("Thank you for using Soloman's bank")
        break
    else:
        #Explain correct input in case of mistake
        print("Please select a number 1-5 that corresponds to your choice of function")
        print("Please Try again")
        #End of function user message
        mainMenu = input("To exit or continue using this service press enter ...")
