import inflect

p = inflect.engine()

names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        s = p.join(names)
        print(f"Adieu, adieu, to {s}")
        break
