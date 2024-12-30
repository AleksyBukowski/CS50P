from pyfiglet import Figlet, FontNotFound
import sys
import random

figlet = Figlet()

l = len(sys.argv)
if l not in (1, 3):
    sys.exit(f"0 or 2 additional arguments expected, {l} given.")
elif l == 3 and sys.argv[1] not in ("-f", "--font"):
    sys.exit("Wrong font argument")


if l == 3:
    try:
        figlet.setFont(font=sys.argv[2])
    except FontNotFound:
        sys.exit("Font not found")
elif l == 1:
    font_list = figlet.getFonts()
    figlet.setFont(font=random.choice(font_list))

i = input("Input: ")

print(f"Output:\n{figlet.renderText(i)}")
