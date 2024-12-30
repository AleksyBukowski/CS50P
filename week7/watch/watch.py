import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if found := re.search(r'src="(http|https)://(www\.)?youtube\.com/embed/(\w+)"', s):
        return f"https://youtu.be/{found.group(3)}"
    else:
        return None


if __name__ == "__main__":
    main()
