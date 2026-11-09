age = int(input("Enter your age:"))
ID_CARD =input("Enter whether you have ID_CARD:")

if age >= 18 and ID_CARD == "yes":
   print("eligible to vote & allowed to vote.")
elif age >= 18 and ID_CARD == "no":
    print("eligible to vote but not allowed to vote.")
elif age >= 60 and ID_CARD == "yes":
   print("Senior citizen and allowed to vote")
else:
    print("Not allowed to vote He/She is Minor")