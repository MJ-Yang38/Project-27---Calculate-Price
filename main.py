
available_parts={
"1": "computer",
"2": "monitor",
"3": "keyboard",
"4": "mouse",
"5": "hdmi cable",
"6": "dvd drive"
}
price_quantity={
    
    "computer": {"price": 500, "quantity" : 10},
    "monitor": {"price": 200, "quantity" : 8},
    "keyboard": {"price": 500, "quantity" : 5},
    "mouse": {"price": 10, "quantity" : 0},
    "hdmi cable": {"price": 20, "quantity" : 7},
    "dvd drive": {"price": 50, "quantity" : 5}
}

total_price=0



user_select=None
while user_select!="0":
  if user_select in available_parts:
    sel_item=available_parts[user_select]
    if price_quantity[sel_item]["quantity"]!=0:
      print(f"Adding {sel_item}")
      total_price+=price_quantity[sel_item]["price"]
      price_quantity[sel_item]["quantity"]-=1
        
    else:
      print(f"{sel_item} is out of stock")
  else:
    print("Please add options from the list")
    for key,value in available_parts.items():
      print(f"{key}: {value}")
    print("0: to finish")
  user_select=input("> ")#start user input part
print(f"Total price is: {total_price}")
