class Jar:
    def __init__(self, capacity=12):
        if type(capacity) == str or capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        if n > self.capacity - self.size:
            raise ValueError("Invalid deposit ammount")
        self._size += n


    def withdraw(self, n):
        if n > self.size or n < 0:
            raise ValueError("Invalid withdraw ammount")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size


def main():

    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(3)
    print(jar)


if __name__ == "__main__":
    main()
