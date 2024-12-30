def main():
    i = input("Input: ")
    print(f"${value(i)}")


def value(greeting):
    g = greeting.strip().lower()
    if g[:5] == "hello":
        return 0
    elif g[0] == "h":
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()


