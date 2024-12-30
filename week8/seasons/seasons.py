from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    date_of_birth = input("Date of birth: ")
    minutes = minutes_since(date_of_birth)
    print(f"{p.number_to_words(minutes, andword="").capitalize()} minutes")


def minutes_since(d):
    try:
        current_date = date.today()
        difference = current_date - date.fromisoformat(d)
        return int(difference.total_seconds() / 60)
    except ValueError:
        sys.exit("Invalid date")



if __name__ == "__main__":
    main()
