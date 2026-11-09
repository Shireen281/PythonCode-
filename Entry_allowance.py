admin = input("Enter are you a admin:") 
password = input("Tell the password:")

if admin == "yes":
    print("Entry permission.")

    if password == "123":
      print("Entry Allowed")

    else:
       print("Entry not allowed")
       
else:
    print("Not allowed to entry permission")
