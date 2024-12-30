from PIL import Image, ImageOps
from sys import argv, exit

def main():
    argv_len = len(argv)
    allowed_extensions = (".jpg", ".jpeg", ".png")
    if argv_len < 3:
        exit("Too few command-line arguments")
    elif argv_len > 3:
        exit("Too many command-line arguments")
    elif not (argv[1].endswith(allowed_extensions) and argv[2].endswith(allowed_extensions)):
        exit("Files must be PNG, JPG or JPEG")
    elif argv[1][-4:] != argv[2][-4:]:
        exit("Output file must be of the same type as the input file")

    add_cs50_shirt(argv[1], argv[2])


def add_cs50_shirt(src, out):
    with Image.open("shirt.png") as shirt, Image.open(src) as f:
        width, height = shirt.size

        f = ImageOps.fit(f, (width, height))
        f.paste(shirt, mask=shirt)
        f.save(out)

if __name__ == "__main__":
    main()
