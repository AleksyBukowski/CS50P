def main():
    tweet = input("Input: ")
    print(f"Output: {shorten(tweet)}")

def shorten(word):
    output = ""
    for letter in word:
        if not letter.upper() in ("A", "E", "I", "O", "U"):
            output += letter

    return output


if __name__ == "__main__":
    main()



