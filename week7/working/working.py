import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.match(r'((?:\d|1[0-2])(?::[0-5][0-9])?) (AM|PM) to ((?:\d|1[0-2])(?::[0-5][0-9])?) (AM|PM)', s):
        o = f""
        for i in range(1, len(matches.groups()), 2):
            time = matches.group(i)
            ampm = matches.group(i+1)

            if ":" in time:
                hrs, mins = map(int, time.split(":"))
            else:
                hrs = int(time)
                mins = 0

            if ampm == "PM" and hrs != 12:
                hrs = hrs+12
            elif ampm == "AM" and hrs == 12:
                hrs = 0

            o += f"{hrs:02}:{mins:02}"

            if i == 1:
                o += f" to "

        return o
    else:
        raise ValueError("Incorrect time format")


if __name__ == "__main__":
    main()
