# Program för att kolla ålder och skriva ut 
ålder = int(input("skriv din ålder"))
if ålder < 13: 
    print("du är barn")
elif ålder >= 13 and ålder <= 19: 
    print("du är tonårig")
else: 
    print("du är vuxen")
    