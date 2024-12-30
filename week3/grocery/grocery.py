grocery_list = {}
while True:
    try:
        item = input()
        if item not in grocery_list:
            grocery_list.update({item: 1})
        else:
            grocery_list[item] += 1
    except EOFError:
        print()
        break


for item, quantity in sorted(grocery_list.items()):
    print(f"{quantity} {item.upper()}")
