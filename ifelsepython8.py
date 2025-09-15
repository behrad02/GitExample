#beräkna rabbat och moms på tre olika produkter 
price1 = float(input("write the price1"))
price2 = float(input("write the price2"))
price3 = float(input("write the price3"))
sum = (price1 + price2 + price3)
discount_price = max(sum - 30, 0) 
total = discount_price * 1.20
print(f"{total: .2f}")

