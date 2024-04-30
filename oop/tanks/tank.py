class Tank:
    def __init__(
        self,
        current_tank_position_x: int = 5,
        current_tank_position_y: int = 5,
        current_direction: str = "↑",
    ):
        self.current_position_x = current_tank_position_x
        self.current_position_y = current_tank_position_y
        self.current_direction = current_direction
        self.shots = {"↑": 0, "→": 0, "←": 0, "↓": 0}

    def move_north(self):  # down
        if self.current_direction != "↓":
            self.current_direction = "↓"
        elif self.current_direction == "↓":
            self.current_position_y += 1

    def move_south(self):  # up
        if self.current_direction != "↑":
            self.current_direction = "↑"
        elif self.current_direction == "↑":
            self.current_position_y -= 1

    def move_east(self):  # right
        if self.current_direction != "→":
            self.current_direction = "→"
        elif self.current_direction == "→":
            self.current_position_x += 1

    def move_west(self):  # left
        if self.current_direction != "←":
            self.current_direction = "←"
        elif self.current_direction == "←":
            self.current_position_x -= 1

    def fire(self):
        self.shots[self.current_direction] += 1

    def get_fire_stats(self):
        return self.shots
