age = int(input("Enter Your age:"))
Card = input("Do You Have Card")

if age >= 18:
    print("Eligible to vote")

    if Card == " yes":
        print("Allowed To Vote")

        if age > 60:
            print("Senior citizen")

        else:
            print("Not a Senior Citizen")

    else:
        print("Not Allowed To Vote")

else:
    print("Not Allowed to Vote")
