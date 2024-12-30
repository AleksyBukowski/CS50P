import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    p = r'((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])'

    if re.fullmatch(p, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
