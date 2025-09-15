# Mata in ett tal och avgöra om det är positivt eller negativt, 
# ge en utskrift 

# värdet 0 behandlas separat, dvs vi ger en utskrift om att värdet är 0

number = int(input ( "Mata in ett tal"))

if number > 0: #if vilkor: 
    print("positivt tal")
elif number < 0: 
    print("negativt tal")
else: #else : 
    print("talet är 0")

    print("end")
