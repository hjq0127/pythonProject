"""CP1404/CP5632 Practical -  Guitars."""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.cost = cost
        self.name = name
        self.year = year

    def __str__(self):
        return f"name={self.name}, cost={self.cost}, year={self.year}"

    def get_age(self):
        return 2020 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    print(f"My guitar: {name}, first made in {year}")
