# beräkna medelvärdet på tre tal
value1 = float(input("write the value1"))
value2 = float(input("writew the value2"))
value3 = float(input("write the value3"))

# räkna ut medelvärdet
mean = (value1 + value2 + value3) / 3
# skriv ut talet med 2 decimaler 
print(f"medelvärdet är: {mean:.2f}")

#hitta minsta och strösta talet
lowest= min(value1,value2,value3)
highest= max(value1,value2,value3)
print (f"lägsta talet är: {lowest}")
print (f"högsta talet är: {highest}")

#kolla om medelvärdet ligger mellan dem eller är lika med en av de 
if lowest < mean < highest:
    print ("medelvärdet ligger mellan det lägsta och det högsta talet")
elif mean == lowest or mean == highest: 
    print("medelvärdet är lika med ett avtalen")

