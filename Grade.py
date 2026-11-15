for i in range (1,6):
    marks = int(input(f"Enter your {i} subject marks here:"))

    if marks >= 90:
        print("A+ grade")
    elif marks >= 75:
        print("A grade")
    elif marks >= 60:
        print("B grade")
    elif marks >= 45:
        print("C grade")
    elif marks >= 33:
        print("D grade")
    else:
        print("FAIL")
