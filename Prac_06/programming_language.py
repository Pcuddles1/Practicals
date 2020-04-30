class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=True, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    "Python, Dynamic Typing, Reflection=True, First appeared in 1991"