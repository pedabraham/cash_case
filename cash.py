#get input
change = -1
while change < 0:
    try:
        change = float(input("Change owed: "))
    except:
        pass
#convert to cents
change *= 100

coin_values = [25,10,5,1]

#get number of coins
total_coins = 0
for value in coin_values:
    coins_per_value = change//value
    if coins_per_value:
        total_coins += coins_per_value
        change = change % value
        if change == 0:
            break

print(int(total_coins))
