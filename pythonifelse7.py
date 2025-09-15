print ("hello and welcome to the unit convert")
# beräkna priset med fast rabbat (10) med ökande moms 20%
price = float(input("write the price"))
discount = max(price-10, 0)
total = discount * 1.20 
print (f"{total:.2f}")

# omvadla hastigheten i km/h til mph 
kmh = float(input("write the speed kmh:"))
mph =  kmh * 0.62137
print (f"{mph: .2f}")

# beräkna priset med 50kr rabbat om köpet är över 500 och med 25% ökande moms. 
price = float(input("write the price"))
if price >= 500:
    discount_price = price-50 
else: 
    discount_price = price 
total = discount_price * 1.25
print (f"{total: .2f}")

