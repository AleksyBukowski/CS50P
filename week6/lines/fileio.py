names = ["A", "B", "C", "D"]

with open("fileio.txt", "w") as file:
    for name in names:
        file.write(f"{name}\n")



with open("fileio.txt") as file:
    for line in file:
        print("Name: ", line.rstrip())
