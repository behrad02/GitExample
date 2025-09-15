#fråga efter filmens åldergräns
age_limit = int(input("What is the movie's age rating?"))
#fråga efter personens ålder
age = int(input("how old are you?"))
if age >= 15: 
    print("Welcome, hope you enjoy the movie!")
else: 
    adult = input("Do you have an adult with you?")
    if adult == "yes":
        print("Welcome, hope you enjoy the movie!")
    else: 
        print("Sorry, you are too young to watch the movie!")

