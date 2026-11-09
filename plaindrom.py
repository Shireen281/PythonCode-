word = input("enter the name:")

rev_name = ""

for i in word:

       rev_name =i + rev_name

print(f"The reverse of the name is: {rev_name}")

if word == rev_name:
        print("palindromic word")
else:
    print("non-palindromic")  