def main():
    w = input("What time is it? ")
    o = convert(w)

    if 7 <= o <= 8:
        print("breakfast time")
    elif 12 <= o <= 13:
        print("lunch time")
    elif 18 <= o <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    fract = round(float(minutes) / 60, 2)

    return float(hours) + fract




if __name__ == "__main__":
    main()
