numbers = [10,45,34,45,87,24,9,89,66,81]

total = sum(numbers)
print("The total of the num is:",total)


average = total / len(numbers)
print("The average of the num is:",average)


for num in numbers:
    if num > average:
        print(num, f"is greater than {average}")
    elif num < average:
        print(num, f"is less than {average}")
    else:
        print(num, f"is equal to {average}")


        

        
        


