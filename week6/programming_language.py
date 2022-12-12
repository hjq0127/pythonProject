"""CP1404/CP5632 Practical - programming_language."""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.typing = typing
        self.name = name
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"name={self.name}, typing={self.typing}, reflection={self.reflection}, " \
               f"year={self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
