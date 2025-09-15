print("calculator | + - * / | type 'exit' to quit")
while True: 
    op = input ("operation ( + - * / or exit)").strip()
    if op == "exit": 
        break
    if op not in ["+", "-", "*", "/"]:
        print("Invalid operation!")
        continue

    
    try: 
        a = float(input("Write the first number").strip())
        b = float(input("Write the second number").strip())

        if op == "+":
           result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/": 
            if b == 0: 
                print (" Division by zero not allowed!")
                continue
            result = a / b
       
        print(f"result: {result:.2f}")
       
    except ValueError: 
        print ("Please enter a numbers only.")

