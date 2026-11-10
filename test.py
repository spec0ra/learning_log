item = "               Energy Drink                 "

price = 5

quantity = 3

border = '='


print(border*20)

total = price*quantity

print(f"Order: {quantity} * {item} | Total: ${total}")

print(f"Next week total: ${(price+2)*quantity}")

print(len(item))

just_test = item.upper()

print (just_test)

print(item.lower())

print(item.replace('Energy', 'Redbull'))

print(item.strip())





splits = item.split()

print(splits)

joined_try = ' '.join(splits)
print(joined_try)

joined_try2 = ''.join(splits)

print(joined_try2)

