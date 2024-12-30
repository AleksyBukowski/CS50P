while True:
    try:
        f = input("Fraction: ")
        x, y = f.split("/")
        x = int(x)
        y = int(y)
        e = round(x*100/y)
    except ValueError:
        print("Denominator and numerator must be ints")
    except NameError:
        print("Must provide a valid fraction")
    except ZeroDivisionError:
        print("Can't divide by zero")
    else:
        if e <= 100:
            if 1 < e < 99:
                print(f"{e}%")
            elif e <= 1:
                print("E")
            elif e >= 99:
                print("F")
            break
        else:
            print("Fraction must be less than 1")



