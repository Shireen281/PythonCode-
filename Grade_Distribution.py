total = 0
highest = 0
lowest = 100


for i in range (1,6):
        marks = int(input(f"Enter your {i} subject marks:"))
        total  = total + marks 

        if marks > highest:
            highest = marks 

        if marks < lowest :

print(f"The total marks of the studenet is :{total}")

average = total / 5
print(f"The average marks of the student is:{average}")

print(f"The highest marks of the student is:{highest}")
print(f"The lowest marks of the student is:{lowest}")
    
if average >= 90:
       print("A+ grade")

elif average >= 75:
        print("A grade")

elif average >= 60:
        print("B grade")

elif average >= 45:
        print("C grade")

elif average >= 33:
        print("D grade")

else:
    print("Fail") 

