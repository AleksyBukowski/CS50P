from string import ascii_uppercase

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    n = "0123456789"
    nums = ""
    for c in s:
        if c not in ascii_uppercase and c not in n:
            return False
        elif c in n:
            nums += c

    if nums != "" and ((s[:len(s)-len(nums)] != s.replace(nums, "")) or nums[0] == "0"):
        return False


    first2 = True if s[0] in ascii_uppercase and s[1] in ascii_uppercase else False

    if not first2:
        return False

    return True



main()
