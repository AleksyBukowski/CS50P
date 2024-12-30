def main():
    g = input("Greeting: ")
    print(greeting_check(g))



def greeting_check(g):
    g = g.strip().lower()
    if g[:5] == "hello":
        return "$0"
    elif g[0] == "h":
        return "$20"
    else:
        return "$100"

main()
