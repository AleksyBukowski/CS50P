import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")

    print(count_lines(sys.argv[1]))




def count_lines(f):
    try:
        lines = 0
        with open(f) as file:
            for line in file:
                l = line.strip()
                if not (l == "" or l[0] == "#"):
                    lines += 1
        return lines
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
