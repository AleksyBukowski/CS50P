import requests
import sys


l = len(sys.argv)
if l == 1:
    sys.exit("Missing command-line argument")
elif l != 2:
    sys.exit(f"1 additional command-line argument expected, {l-1} given")


try:
    quantity = float(sys.argv[1])
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = request.json()
    price = o["bpi"]["USD"]["rate_float"]
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Error loading bitcoin price")


print(f"${quantity * price:,}")
