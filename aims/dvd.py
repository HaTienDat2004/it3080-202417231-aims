class DigitalVideoDisc:
    def __init__(self, title, category="Unknown", cost=0.0, director="Unknown", length=0):
        self.title = title
        self.category = category
        self.cost = float(cost)
        self.director = director
        self.length = length
