class Ship:
    name = None
    initial_position = []
    actual_position = []
    direction = None

    def __init__(self, name="", initial_position=None, direction=""):
        self.name = name
        self.initial_position = initial_position
        self.actual_position = initial_position
        self.direction = direction

    def update_position(self, day):
        if self.direction == "E" or self.direction == "NE" or self.direction == "SE":
            self.actual_position[0] += day - 1

        if self.direction == "W" or self.direction == "NW" or self.direction == "SW":
            self.actual_position[0] -= day - 1

        if self.direction == "N" or self.direction == "NW" or self.direction == "NE":
            self.actual_position[1] += day - 1

        if self.direction == "S" or self.direction == "SW" or self.direction == "SE":
            self.actual_position[1] -= day - 1
