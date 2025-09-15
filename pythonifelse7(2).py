print("hello ansd welcome to the unit converter!")
# Ta in ett värde från användare 
value_str = input("inter value to conver")
try:
    value = float (value_str)
except ValueError:
    print("Invalid value , please enter a number")
    exit()

# Fråga vilken typ av konvertering som ska göras 
choice = input("choose what to convert (P = price, S= Speed)")
if choice == "P":
    # omvandla pris rabbat 10 kr och sedan + 20 procent moms
    result = max(value-10 , 0) * 1.20
    print(f"The final price of {value:.2f} after 10kr discount and 20% tax is {result:.2f}kr")

elif choice == "S":
    result  = value * 0.62137
    print(f"{value:.2f} km/h is equivalent to {result:.2f} mph")
else: 
    print("invalid converter, please enter P or S")
    exit()