import random


def main():
    level = get_level()
    score = 0
    excercises = 0
    while excercises < 10:
        a = generate_integer(level)
        b = generate_integer(level)
        ans = a + b
        u = -1
        count = 0
        while u != ans:
            count += 1
            print(f"{a} + {b} = ", end="")
            try:
                u = int(input())
            except ValueError:
                pass
            if u != ans:
                print("EEE")
            if count == 3:
                print(f"{a} + {b} = {ans}")
                break
        if u == ans:
            score += 1
        excercises += 1

    print(f"Score: {score}")


def get_level():
    lvl = -1
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in (1, 2, 3):
                return lvl
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level in (2, 3):
        return random.randint(10**(level-1), (10**level)-1)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
