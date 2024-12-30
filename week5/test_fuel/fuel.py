def main():
    f = input("Fraction: ")
    c = convert(f)
    print(gauge(c))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        e = round(x*100/y)
    except ValueError:
        raise ValueError("Denominator and numerator must be ints")
    except NameError:
        raise NameError("Must provide a valid fraction")
    except ZeroDivisionError:
        raise ZeroDivisionError("Can't divide by zero")
    else:
        if 0 <= e <= 100:
            return e
        else:
            raise ValueError("Fraction must be less than or equal to 1 and bigger than or equal to 0")



def gauge(percentage):
        if 1 < percentage < 99:
            return f"{percentage}%"
        elif percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"


if __name__ == "__main__":
    main()








