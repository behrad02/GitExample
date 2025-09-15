# Program att kolla på betyg och skriva ut 

betyg = int(input("skriv in din betyg"))
if betyg < 10: 
    print("du är underkänd")
elif betyg >= 10 and betyg <= 20:
    print("du är godkänd")
else:
    print("ange en värdefull siffra") 