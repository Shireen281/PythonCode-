total_bill = 0   
Highest_price = 0

for i in range(1,6):
    price = float(input("enter your product price:"))
    total_bill = price + total_bill 

    if price >= 3000:
        print("Expensive Item")
    if price > Highest_price:
        Highest_price = price

    print(f"The Highest price is {Highest_price}")
    print(f"The total bill is:{total_bill}")

if total_bill >=10000:
    print("You have 20% discount")
    discount = 0.2

elif total_bill >= 5000:
    print("You have 10% discount")
    discount = 0.1

elif total_bill >=2000:
    print("You have 5% discount")

else:
    print("No Discount")

    discount_amount = total_bill * discount
    print(f"Your discount amount is: {discount_amount}")

    final_bill = total_bill - discount_amount
    print(f"You have to pay:{final_bill}")
 