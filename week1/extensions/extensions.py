def main():
    f = input("File name: ")
    print(check_mime(f))


def check_mime(f):
    f = f.lower().strip()
    s = ""
    for i in range(len(f)-1, -1, -1):
        if f[i] == ".":
            s = f[i+1:]
            break

    match s:
        case "jpg" | "jpeg" | "gif" | "png":
            p = "image"
            s = "jpeg" if s == "jpg" else s
        case "txt":
            p = "text"
            s = "plain"
        case _:
            p = "application"
            s = s if s in ("zip", "pdf") else "octet-stream"

    return f"{p}/{s}"


main()
