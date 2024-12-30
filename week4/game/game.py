import random

lvl = None

while True:
    try:
        if not lvl or lvl < 1:
            lvl = int(input("Level: "))
            r = random.randint(1, lvl)
        i = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if i < 1:
            pass
        elif i < r:
            print("Too small!")
        elif i > r:
            print("Too large!")
        else:
            print("Just right!")
            break
