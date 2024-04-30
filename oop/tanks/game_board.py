from random import randint
from tank import Tank


class Board(Tank):
    def __init__(self, board_width: int = 10, board_height: int = 10):
        super().__init__()
        self.tank = Tank()
        self.board_width = board_width
        self.board_height = board_height
        self.points = 200
        self.hits = 0
        self.top_guns = []
        self.target_x = None
        self.target_y = None
        self.generate_target()

    def generate_target(self):
        self.target_x = randint(0, self.board_width - 1)
        self.target_y = randint(0, self.board_height - 1)

    def get_visual_board(self):
        for y in range(self.board_height):
            for x in range(self.board_width):
                if (
                    x == self.tank.current_position_x
                    and y == self.tank.current_position_y
                ):
                    if self.tank.current_direction == "↑":
                        print("↑", end="")
                    elif self.tank.current_direction == "→":
                        print("→", end="")
                    elif self.tank.current_direction == "↓":
                        print("↓", end="")
                    elif self.tank.current_direction == "←":
                        print("←", end="")
                elif x == self.target_x and y == self.target_y:
                    print("X", end="")
                else:
                    print("_", end="")
            print()

    def make_tank_move_on_board(self):
        self.generate_target()  # kad taikiniai ant lentos atsirastu
        while True:
            user_input_direction = (
                input(
                    """
                Where do you want to go?
                (right, left, up, down, fire, top or exit)
                """
                )
                .strip()
                .lower()
            )
            print(self.tank.shots)
            print("User input:", user_input_direction)

            if user_input_direction == "fire":
                self.tank.fire()
                print(
                    f"Tank's current position: x={self.tank.current_position_x} and y={self.tank.current_position_y}"
                )

                if (
                    (
                        self.tank.current_direction == "↑"
                        and self.tank.current_position_y > self.target_y
                    )
                    or (
                        self.tank.current_direction == "↓"
                        and self.tank.current_position_y < self.target_y
                    )
                    or (
                        self.tank.current_direction == "→"
                        and self.tank.current_position_x < self.target_x
                    )
                    or (
                        self.tank.current_direction == "←"
                        and self.tank.current_position_x > self.target_x
                    )
                ):
                    print("I'm Death - Straight up")
                    self.hits += 1
                    self.points += 50
                    self.generate_target()
                else:
                    print("Did You Miss Me?")
                    self.points -= 10

            elif user_input_direction == "down":
                self.tank.move_north()
                self.points -= 10
                print(
                    f"Tank's current position: x={self.tank.current_position_x} and y={self.tank.current_position_y}"
                )

            elif user_input_direction == "up":
                self.tank.move_south()
                self.points -= 10
                print(
                    f"Tank's current position: x={self.tank.current_position_x} and y={self.tank.current_position_y}"
                )

            elif user_input_direction == "right":
                self.tank.move_east()
                self.points -= 10
                print(
                    f"Tank's current position: x={self.tank.current_position_x} and y={self.tank.current_position_y}"
                )

            elif user_input_direction == "left":
                self.tank.move_west()
                self.points -= 10
                print(
                    f"Tank's current position: x={self.tank.current_position_x} and y={self.tank.current_position_y}"
                )

            elif user_input_direction == "exit":
                print("Don't leave me...")
                break
            elif user_input_direction == "top":
                self.show_top_scores()
            else:
                print("Wrong command")

            if (
                self.points <= 0
                or self.tank.current_position_x >= self.board_width
                or self.tank.current_position_x < 0
                or self.tank.current_position_y >= self.board_height
                or self.tank.current_position_y < 0
            ):
                print("It's over lady's and gentlemen! It's over!")
                self.save_score()
                break

            self.get_visual_board()
            print(f"Earned points total: {self.points}")
            print(f"Shots fired: {self.tank.shots} Hits: {self.hits}")

    def save_score(self):
        name = input("Enter your name: ")
        self.top_guns.append((name, self.hits))

    def show_top_scores(self):
        print("Top Guns:")
        sorted_scores = sorted(self.top_guns, key=lambda x: x[1], reverse=True)
        for player, (name, score) in enumerate(sorted_scores[:5], start=1):
            print(f"{player}. {name}: {score}")


# if __name__ == "__init__":
game_board = Board()
game_board.get_visual_board()
game_board.make_tank_move_on_board()
