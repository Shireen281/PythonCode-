numbers = [10,45,34,45,87,24,9,89,66,81]
Even = []
Odd = []

for num in numbers:

    if num % 2 == 0:
        Even.append(num)    

    else:
        Odd.append(num)

print("The Even Numbers are:",Even)
print("The Odd Numbers are:",Odd)
        

