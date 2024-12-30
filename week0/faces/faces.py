def main():
    s = input("Your message: ")
    print(convert(s))


def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s




main()
