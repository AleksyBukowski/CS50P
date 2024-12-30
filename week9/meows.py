import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")

parser.add_argument("-n", help="Number of times to meow", default="1", type=int)
parser.add_argument("-o", help="Number of o's in a meow", default="1", type=int)
args = parser.parse_args()


for _ in range(args.n):
    print("Me" + "o"*args.o + "w")
