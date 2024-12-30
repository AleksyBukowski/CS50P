from PIL import Image, ImageFilter
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

    find_edges(argv[1], argv[2])


def find_edges(input, output):
    with Image.open(input) as f:
        f = f.filter(ImageFilter.FIND_EDGES)
        f.save(output)


if __name__ == "__main__":
    main()
