class Student:
    def __init__(self, name, home):
        if not name:
            raise ValueError('missing name')

        self.name = name
        self.home = home

    def __str__(self):
        return f"{self.name} form {self.home}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "s"
            case "Otter":
                return "O"
            case _:
                return 'default case'

    @property
    def home(self):
        return self._home

    @home.setter
    def home(self, home):
        if home not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid home")
        self._home = home

def main():
    student = get_student()
    print(f"{student.name} from {student.home}")

def get_student():
    name = input("Name: ")
    home = input("home: ")
    return Student(name, home)

if __name__ == "__main__":
    main()
