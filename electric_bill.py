  
    

#a = input('Enter your name')
#b = input('Enter your Age')
#print(a,b)

##num = int(input("enter the number:"))
#square = num*num
#print('square',square)

#a = input("Enter the first number")
#b = input("Enter the second number")
#if a == b:
   # print("both are equal")
#elif a > b :
    #print("first one is Greater.")
#else:
    #print("Second one is Greater.")

#year= int((input("Enter the year")))
#if year % 4 == 0:
   # print("Leap year")
#if year % 100 == 0:
   # print("Not a leap Year")
#f year % 400 == 0:
   # print("Leap year")
#else:
   # print("Not a leap year")

#age = int(input("Enter your Age:"))#
#card = input("Have card:")#

#if age >= 18:#
   # print("Eligible to vote")#
   # if card == "yes":#
        #print("Allow to vote")#

       # if age > 60:#
          #  print("Senior Citizen")#
       # else:
         #   print("Not a Senior Citizen")#
   # else:
     #   print("Not allowed to vote")#
#lse:
   # print("Not Eligible to vote")#

#admin = input("Enter are you a admin:") 
#password = input("Tell the password:")

#if admin == "yes":
    #print("Entry permission.")
   # if password == "123":
   #     print("Entry Allowed")
   # else:
    #    print("Entry not allowed")
#else:
   # print("Not allowed to entry permission")

#age = int(input("Enter your age:"))
#ID_CARD =input("Enter whether you have ID_CARD:")

#if age >= 18 and ID_CARD == "yes":
  #  print("eligible to vote & allowed to vote.")
#elif age >= 18 and ID_CARD == "no":
    #print("eligible to vote but not allowed to vote.")
#elif age >= 60 and ID_CARD == "yes":
  #  print("Senior citizen and allowed to vote")
#else:
   # print("Not allowed to vote He/She is Minor")

#C = int(input("Enter theory marks:"))
#D = int(input("Enter practical marks:"))

#if C >=35 or D >= 35:
  #  print("PASS")
#else:
   # print("FAIL")

#exp = int(input("Enter how much years of experience:"))
#skill = input("Tell your skill such as (JAVA/PYTHON):")

#if exp >= 10 or skill == "PYTHON":
   # print("Selected for interview.")

#else:
   # print("Not selected for interview.") 

#age = int(input("Enter your age:"))
#degree =input("Enter you have a degree or not:")

#if age >= 18 and degree == "yes": 
   # print("Eligible for job.")

    #exp = int(input("Enter year of experience:"))
    #certification = input("Have certification or not:")

    #if exp >= 10 or certification == "yes":
     #   print("Eligible for Senior Role.")
    #elif exp >= 5 or certification == "no":
     #   print ("Eligible for Junior Role.")
    #else:
     #   print("Eligible as Fresher.")
#else:
   # print("Not Eligible for Job.")

#age  = int(input("Enter your age:"))
#adhaar = input("Whether you have adhaar or not(Yes/No):").lower()
#passport = input ("Whether you have passport or not(Yes/No):").lower()
#print(passport)
#print(adhaar)
#if age >= 18 and (adhaar == "yes" or passport == "yes"):
  #  print("You can check In.")

   # room = input("Which kind of room you want(Premium/Standard):")
    #if room == "premium":
     #   print("Premium room alloted.")
   # else:
    #    print("Standard room alloted.")
#else:
#    print("You can't check In.")

#print ("Bank Account Application process.")

#age = int(input("Enter your age:"))
#adhaar = input("Whether you have adhaar(yes/no):")
#pan = input ("Whether you have pan(yes/no):")

#if age >= 18 and adhaar == "yes":
 #   print ("You can open a bank account.")

  #  amount = int(input("Enter initial Deposit account."))

   # if pan == "yes" and amount <= 50000:
    #    print ("Can proceed for KYC.")
        

     #   if amount >= 100000:
      #      print("premium account with 7% interest.")
       # elif amount >=25000 and amount <= 99999:
        #    print("Saving account with 5% interest.")
        #elif amount >= 5000 and amount <= 24999:
         #   print("Basic account with 3% interest.")
        #else:
         #   print ("reject the application.")


        #print("For Debit Card.")
        #if amount >= 25000 and age <= 60:
         #   print ("Premium debit card.")
        #else:
         #   print("Standard Debit Card.")


   # else:
    #    print("You cannot proceed for KYC.")
    
#else:
    #print ("Not eligible to open a bank account.")

#num = int(input("enter the number."))


#for i in range (1,10) :
   # print(i,"square =",(i*i))


#for i in range(1,11):
    
 #   Y=(Y+i)
    #Y = 0
    

#print ("sum of first 10 numbers",Y)


#for i in range (10,0):
 #   print(i)

#t = int(input ("enter a number"))
#y = 0

#for i in range(0,t,5):
   #  y = y+i
#print (y)

#y = 0
#x = 0
#for i in range (0,10,5 ):
 ##  if i % 2 == 0:
   #     y = y+1
    ##   x = x+1  

#print("even numbers are:",y)
#print("odd numbers are:",x)




#for i in range (1,6):
    
   #print("*" * i)




#num = int(input("Enter a number:")) 

#count = 0

#for s in range(1,num+1):

   # if num % s == 0 : 
    #    count = count + 1

#if count == 2:
   # print ("The number is a prime number.")

#else:
   # print("The number is not a prime number")

#for i in range (1,6):
 ##   marks = int(input(f"Enter your {i} subject marks here:"))

   # if marks >= 90:
      #  print("A+ grade")
   # elif marks >= 75:
     #   print("A grade")
  #  elif marks >= 60:
      #  print("B grade")
   # elif marks >= 45:
   #     print("C grade")
    #elif marks >= 33:
     #   print("D grade")
    #else:
     #   print("FAIL")

#word = input("enter the name:")

#rev_name = ""

  #  for i in word:

   #     rev_name =i + rev_name

    #print(f"The reverse of the name is: {rev_name}")

    #if word == rev_name:
     #   print("palindromic word")
    #else:
     #   print("non-palindromic")  

 #   total = 0
   # highest = 0
  #  lowest = 100


   # for i in range (1,6):
    #    marks = int(input(f"Enter your {i} subject marks:"))
#   total  = total + marks 
#
 #       if marks > highest:
  #          highest = marks 
#
 #       if marks < lowest :
  ##
#
 #   print(f"The total marks of the studenet is :{total}")
#
 #   average = total / 5
  #  print(f"The average marks of the student is:{average}")
#
 #   print(f"The highest marks of the student is:{highest}")
  #  print(f"The lowest marks of the student is:{lowest}")
#
 #   if average >= 90:
  #      print("A+ grade")
#
 #   elif average >= 75:
  #      print("A grade")

   # elif average >= 60:
    #    print("B grade")

   # elif average >= 45:
    #    print("C grade")

   # elif average >= 33:
    #    print("D grade")
#
 #   else:
  #      print("Fail") 
#

    ###################################################################

    
  ## total_withdrawl = 0
    #total_deposit = 0
#    success_count = 0
 #   failed_count = 0
#
 #   for i in range (1,6):
 #       amount = float(input("Enter your  amount"))
#
#
 #   if amount > 0 :
  #      success_count = success_count + 1
#
 #       print ("deposited")
#
 #       balance = amount + balance
#
 #       total_deposit = total_deposit + amount 

  #  elif amount <0:
         
    
   #     withdrawl = -amount

    #    if withdrawl <= balance:
 #           success_count = success_count + 1
#
   #         total_withdrawl = total_withdrawl + withdrawl
        #    balance = balance - withdrawl

       #     print("We can do the withdrawal")
               
   #     else:
    #        print("Insufficient transsaction")

   # else:
   #     print("failed transaction") 
    #    failed_count = failed_count + 1
            

  #  print(f"The final balance is:{balance}") 
   # print(f"The total withdrawl is:{total_withdrawl}") 
    ##rint(f"There are {success_count} succesfull transaction")
  #  print(f"There are {failed_count} unsuccessfull transaction")

##########################################################################

 #   total_bill = 0   
  #  Highest_price = 0
#
 #   for i in range(1,6):
  ###    total_bill = price + total_bill 

     ##  if price >= 3000:
       #     print("Expensive Item")
#
 #   print(f"The Highest price is {Highest_price}")
  #  print(f"The total bill is:{total_bill}")
#
 ##      print("You have 20% discount")
   #     discount = 0.2
#
 ##      discount = 0.1
#
 ####
    #else:
     #   print("No discount")

    #d#iscount_amount = total_bill * discount
   # print(f"Your discount amount is: {discount_amount}")

    #final_bill = total_bill - discount_amount
    #print(f"You have to pay:{final_bill}")
        
#######################################################################

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

    
############################################################################






    



    

    

    