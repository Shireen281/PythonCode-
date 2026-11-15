num = int(input("Enter a number:")) 

count = 0

for s in range(1,num+1):

    if num % s == 0 : 
        count = count + 1

if count == 2:
    print ("The number is a prime number.")

else:
    print("The number is not a prime number")
