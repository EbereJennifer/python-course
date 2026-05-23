class Kunde:
    def __init__(self, nummer, name, email):
        self.nummer = nummer
        self.name = name
        self.email = email
    def __str__(self):
        return f'Kunde {self.nummer} \n {self.name} \n {self.email}'


def main():
    kunde = Kunde(54646, "Dennis Oduo", "denni@gmail.com")
    print(kunde)


if __name__ == "__main__":
        main()
