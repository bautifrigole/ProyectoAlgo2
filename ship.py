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

    def update_position(self, actual_day, initial_day):
        if self.direction == "E" or self.direction == "NE" or self.direction == "SE":
            self.actual_position[0] += actual_day - initial_day

        if self.direction == "W" or self.direction == "NW" or self.direction == "SW":
            self.actual_position[0] -= actual_day - initial_day

        if self.direction == "N" or self.direction == "NW" or self.direction == "NE":
            self.actual_position[1] += actual_day - initial_day

        if self.direction == "S" or self.direction == "SW" or self.direction == "SE":
            self.actual_position[1] -= actual_day - initial_day


def are_equal_ships(ship1, ship2):
    return ship1.name == ship2.name and ship1.initial_position == ship2.initial_position \
           and ship1.actual_position == ship2.actual_position and ship1.direction == ship2.direction
