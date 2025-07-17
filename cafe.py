menu={
    'Ice tea':190,
    'Vanila Latte':250,
    'Americano':300,
    'Bubble tea':150,
    'coldrink':120,
}

print("Welcome to our cafe!")
print(" Ice tea: 190\nvanila Latte: 250\nAmericano: 300\nBubble tea: 150\n coldrink: 120 ")

order_total = 0
# 190 + 250 = 440 

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Your item {item_1} is not available , please check and give anyother order mam") 

another_item = input("Do you want something else sir ? (Yes/No):")

if another_item == "Yes":
    item_2 = input("Enter the second item =")
    
    if item_2 in menu: 
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Your item {item_2} is not available, please check and give another order mam")

print(f"Your total amount to pay is ₹{order_total}")
print("Thank you mam,\nNext time come to our cafe.")

    


      
     