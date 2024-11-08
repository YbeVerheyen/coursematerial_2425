# write your code here
def tip_calculator():
    price = input("Enter total price: ")
    tip = input("Enter tip percentage (default=20): ")
    if tip =='':
        tip = 20
    price = int(price)
    tip = int(tip)
    totaal = int(price + price * tip/100)
    print(f"You have to pay {totaal}")