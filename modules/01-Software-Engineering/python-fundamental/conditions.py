# Simple GPA grade system using conditional statements
# GPA = float(input("Enter your GPA: "))

# if GPA >= 3.5:
#     print("You have an A grade.")
# elif GPA >= 3.0:
#     print("You have a B grade.")
# elif GPA >= 2.0:
#     print("You have a C grade.")
# else:
#     print("You have a D grade or below.")

"""Practice 1"""

print("==== Welcome to the Amba Cinema ====")

print("Please select a movie from the list below: ")
print("1. The Matrix (RP. 10.000)")
print("2. Inceptio (RP. 12.000)")
print("3. Interstellar (RP. 15.000)")

print(" ")

def apply_discount(price):        
    while True:
        age = int(input("Enter your age:"))
        if age < 17:
            price = price * 0.8  # Apply a 20% discount for under 17
            print(f"You are eligible for a 20% discount. Your ticket price is now: RP. {price}")
            break
        elif age < 20:
            price = price * 0.9 # Apply a 10% discount for ages 17-19
            print(f"You are eligible for a 10% discount. Your ticket price is now: RP. {price}")
            break
        else:
            print(f"Your ticket price is: RP. {price}")
            break
            
while True:
    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        price = 10000
        print("You have selected 'The Matrix'. Enjoy the movie!")
        apply_discount(price)
        break
    elif choice == 2:
        price = 12000
        print("You have selected 'Inception'. Enjoy the movie!")
        apply_discount(price)
        break
    elif choice == 3:
        price = 15000
        print("You have selected 'Interstellar'. Enjoy the movie!")
        apply_discount(price)
        break
    else:
        print("Invalid choice. Please select a valid movie.")
 
        
    # 