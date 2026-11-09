age  = int(input("Enter your age:"))
adhaar = input("Whether you have adhaar or not(Yes/No):").lower()
passport = input ("Whether you have passport or not(Yes/No):").lower()
print(passport)
print(adhaar)
if age >= 18 and (adhaar == "yes" or passport == "yes"):
    print("You can check In.")

    room = input("Which kind of room you want(Premium/Standard):")
    if room == "premium":
        print("Premium room alloted.")
    else:
        print("Standard room alloted.")
else:
    print("You can't check In.")

print ("Bank Account Application process.")