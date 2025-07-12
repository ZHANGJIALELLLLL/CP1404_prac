CURRENT_YEAR = 2023

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self,  other):
        return self.year < other.year

    def get_age(self):
        """Get guitar's age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine whether it is more than 50 years."""
        return self.get_age() >= 50