print("Hello and welcome to the unit converter!")
# Ta in ett värde från användare
value_str = input ("inter value to convert")
try: 
    value = float(value_str)
except ValueError:
    print ("invalid value, please enter a number")
    exit()
result = max ( value - 50 , 0) * 1.09
print (f"the final price of {value: .2f} after 50kr discount and 9% discount is {result:.2f}kr")
exit()
