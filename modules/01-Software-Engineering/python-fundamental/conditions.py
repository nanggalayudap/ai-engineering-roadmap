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
print("1. The Matrix")
print("2. Inception")
print("3. Interstellar")

print(" ")
while True:
    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        print("You have selected 'The Matrix'. Enjoy the movie!")
        break
    elif choice == 2:
        print("You have selected 'Inception'. Enjoy the movie!")
        break
    elif choice == 3:
        print("You have selected 'Interstellar'. Enjoy the movie!")
        break
    else:
        print("Invalid choice. Please select a valid movie.")
        
    # Adding a conditions for age restriction and ticket price