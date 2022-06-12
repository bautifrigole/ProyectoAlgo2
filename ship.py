class Ship:
    name = None
    initial_position = tuple
    actual_x = None
    actual_y = None
    direction = None

    def __init__(self, name="", initial_position=tuple, direction=""):
        self.name = name
        self.initial_position = initial_position
        self.actual_x = initial_position[0]
        self.actual_y = initial_position[1]
        self.direction = direction

    def update_position(self, day):
        if self.direction == "E" or self.direction == "NE" or self.direction == "SE":
            self.actual_x += day - 1

        if self.direction == "W" or self.direction == "NW" or self.direction == "SW":
            self.actual_x -= day - 1

        if self.direction == "N" or self.direction == "NW" or self.direction == "NE":
            self.actual_y += day - 1

        if self.direction == "S" or self.direction == "SW" or self.direction == "SE":
            self.actual_y -= day - 1
