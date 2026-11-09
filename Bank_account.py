age = int(input("Enter your age:"))
adhaar = input("Whether you have adhaar(yes/no):")
pan = input ("Whether you have pan(yes/no):")

if age >= 18 and adhaar == "yes":
    print ("You can open a bank account.")

    amount = int(input("Enter initial Deposit account."))

    if pan == "yes" and amount <= 50000:
        print ("Can proceed for KYC.")
        

        if amount >= 100000:
            print("premium account with 7% interest.")
        elif amount >=25000 and amount <= 99999:
            print("Saving account with 5% interest.")
        elif amount >= 5000 and amount <= 24999:
            print("Basic account with 3% interest.")
        else:
            print ("reject the application.")


        print("For Debit Card.")
        if amount >= 25000 and age <= 60:
            print ("Premium debit card.")
        else:
           print("Standard Debit Card.")


    else:
        print("You cannot proceed for KYC.")
    
else:
    print ("Not eligible to open a bank account.")
