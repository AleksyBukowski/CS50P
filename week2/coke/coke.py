remaining = 50

while remaining > 0:
    print(f"Amount Due: {str(remaining)}")
    inserted = int(input("Insert coin: "))
    if inserted in (50, 25, 10, 5, 1):
        remaining -= inserted

print(f"Change Owed: {str(abs(remaining))}")
