import sys
from csv import DictReader, DictWriter

def main():
    argv_len = len(sys.argv)
    if argv_len < 3:
        sys.exit("Too few command-line arguments")
    elif argv_len > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv" and sys.argv[2][-4:] != ".csv":
        sys.exit("Not a CSV file")

    scourgify(sys.argv[1], sys.argv[2])


def scourgify(from_file, to):
    try:
        with open(from_file) as f:
            reader = DictReader(f)
            newlist = []

            for line in list(reader):
                last, first = line["name"].split(", ")
                newlist.append({"first": first, "last": last, "house": line["house"]})

        with open(to, "w") as f:
            writer = DictWriter(f, fieldnames=list(newlist[0].keys()))
            writer.writeheader()
            for line in newlist:
                writer.writerow(line)


    except FileNotFoundError:
        sys.exit("Could not read file")




if __name__ == "__main__":
    main()
