balance = 3000

def buy_things(item, price):
    global balance
    print(f"Priveous balance {balance}")
    balance = balance - price
    print(f"After buying balance {item}",{balance})

buy_things("shoe", 1800)
print(balance)