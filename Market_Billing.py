
Total_bill = 0
member = input("Are you a member (yes/no):").strip().lower()

for i in range (1,6):
    prize = float(input(f"Enter {i} product prize: "))
    quantity = int(input("Enter the Quantity of Product: "))

    if prize > 0 and quantity > 0:
        item_prize = prize * quantity
        Total_bill = Total_bill + item_prize

        print(f"The item prize is: {item_prize}") 

    else:
        print("Invalid prize or quantity.")

if Total_bill >= 10000:
    discount = Total_bill * 0.15
    print("\nYou have 15% discount")

elif Total_bill >= 5000:
    discount = Total_bill * 0.1
    print("\nYou have 10% discount")

elif Total_bill >= 2000:
    discount = Total_bill * 0.05
    print("\nYou have 5% discount")

else:
    print("\nNo discount")

final_bill = Total_bill - discount

if final_bill >= 5000:

    if member == "yes":
        delivery_charge = 0
        print("You have a free delivery.")

    else:
        delivery_charge = 100
        print("Delivery charge is Rs 100")

else:
    delivery_charge = 100
    print("Delivery charge is Rs 100")

Final_amount = final_bill + delivery_charge

print("\n----BILL SUMMARY----")

print(f"Original bill is {Total_bill}")
print(f"Discount is:{discount}")
print(f"Delivery charge is:{delivery_charge}")
print (f"You have to pay the {Final_amount}")


    

