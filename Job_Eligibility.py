age = int(input("Enter your age:"))
degree =input("Enter you have a degree or not:")

if age >= 18 and degree == "yes": 
    print("Eligible for job.")

    exp = int(input("Enter year of experience:"))
    certification = input("Have certification or not:")

    if exp >= 10 or certification == "yes":
        print("Eligible for Senior Role.")
    elif exp >= 5 or certification == "no":
        print ("Eligible for Junior Role.")
    else:
        print("Eligible as Fresher.")
else:
   print("Not Eligible for Job.")
