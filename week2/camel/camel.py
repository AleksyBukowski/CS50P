var = input("camelCase: ")

snake = ""
for letter in var:
    if letter == letter.upper():
        snake += "_"
        snake += letter.lower()
    else:
        snake += letter

print(snake)
