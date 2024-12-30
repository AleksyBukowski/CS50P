tweet = input("Input: ")

output = ""
for letter in tweet:
    if not letter.upper() in ("A", "E", "I", "O", "U"):
        output += letter

print(output)
