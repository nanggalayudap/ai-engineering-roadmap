# Simple GPA grade system using conditional statements
GPA = float(input("Enter your GPA: "))

if GPA >= 3.5:
    print("You have an A grade.")
elif GPA >= 3.0:
    print("You have a B grade.")
elif GPA >= 2.0:
    print("You have a C grade.")
else:
    print("You have a D grade or below.")