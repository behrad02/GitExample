# Användaren ska skriva ett tal och kommer veta om det är negativt eller positivt tal
user_input = input("Enter a number: ")

try:
    value = float(user_input)

if value > 0:
    print("Number is positive")
elif value == 0: 
    print("Number is zero")
else:
    print("Number is negative")
except ValueError:
print (" You must enter a number!")
    print (" You must enter a number!")