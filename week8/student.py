class Student:
    def __init__(self, name, house="unknown"):
        self.name = name.capitalize()
        self.house = house.title()


    def __str__(self):
        if self.house not in ("unknown", ""):
            return f"{self.name} from {self.house}"
        return self.name

    # def __str__(self):
    #     return f"A student called {self.name}"


    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)



if __name__ == "__main__":
    main()
