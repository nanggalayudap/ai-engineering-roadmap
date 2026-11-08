"""
  Variable
    
"""
# Strings =========
first_name = "Jhon"
food = "Pizza"
email = "Brofake@email.com"

# print(f"Hello, my name is {first_name}. I love to eat {food}. You can contact me at {email}.")

# Integers ========
age = 23
number_of_siblings = 2

# print(f"Your age is {age} and you have {number_of_siblings} siblings.")

# Floats =========
pi = 3.14
gpa = 4.00
distance = 10.5

# print(f"My GPA is {gpa} and the value of pi is approximately {pi}.")
# print(f"The distance to the nearest star is {distance} light-years.")

# Booleans ========
is_student = True
has_pet = False

# print(f"Is the person a student? {is_student}")
# print(f"Does the person have a pet? {has_pet}")

    # What if we put a condition? Lets see..
# if is_student:
#     print("The person is a student.")
# else:
#     print("The person is not a student")

# Typecasting  =======
name = "Alice"
age = 25
gpa = 3.8
student = True

gpa = int(gpa)  # Convert float to int

# print(type(name)) # Convert string to int
# print(type(age))
# print(type(gpa))
# print(type(student))

# User input ========
input_name = input("Enter your name: ") # Basiccally the type of input is string
input_age = int(input("Enter your age: ")) # Convert the input to an integer
input_gpa = float(input("Enter your GPA: ")) # Convert the input to a float

input_age = int(input_age)  # Convert the input to an integer
input_gpa = input_gpa + 1

# print(f"your name is {input_name}, you are {input_age} years old, and your GPA is {input_gpa}.")

    # practices
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width

# print(f"The area of the rectangle is: {area}")


item = input("What kind of item do you want to buy? ")
price = float(input(f"What is the price of the {item}? "))
quantity = int(input(f"How many {item}s do you want to buy? "))

car_price = 32000.00

total = price * quantity
print(f"The total cost for {quantity} {item}/s is: ${total}")
print(f"The car price is: ${round(car_price, 4)}")

"""
"""
    