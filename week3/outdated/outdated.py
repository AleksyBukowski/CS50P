def main():
    print(get_date())


def get_date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date = input("Date: ")
        try:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
        except ValueError:
            try:
                m, d, y = date.split(" ")
                d = int(d[:-1])
                y = int(y)
                m = months.index(m.title()) + 1
            except ValueError:
                pass
            else:
                if m <= 12 and d <= 31:
                    return f"{y}-{m:02}-{d:02}"
        else:
            if m <= 12 and d <= 31:
                return f"{y}-{m:02}-{d:02}"

main()
