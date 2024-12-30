import sys, csv, tabulate


def main():
    argv_len = len(sys.argv)
    if argv_len < 2:
        sys.exit("Too few command-line arguments")
    elif argv_len > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")


    show_cool_table(sys.argv[1])


def show_cool_table(f):
    try:
        with open(f) as file:
            reader = list(csv.DictReader(file))
            table_values = []

            for line in reader:
                table_values.append(line.values())

            print(tabulate.tabulate(table_values, list(reader[0].keys()), tablefmt="grid"))
            return


    except FileNotFoundError:
        sys.exit("File does not exist")









if __name__ == "__main__":
    main()
