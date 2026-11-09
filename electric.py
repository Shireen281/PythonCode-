Total_collection = 0



for i in range (1,6):
    unit = int(input("Enter the amount of unit you used"))

    if unit <= 100:
        bill = 0
    
    elif unit <=300:
        bill = unit * 5

    elif unit <= 500:
        bill = unit * 7

    else:
        bill = unit * 10

    Total_collection = bill + Total_collection

print(f"THe total collection is:{Total_collection}")

    





