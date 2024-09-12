import random

class Ludo:
    def __init__(self):
        self.player_pos = 0
        self.computer_pos = 0
        self.finish_line = 100

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, position, dice_roll):
        return min(position + dice_roll, self.finish_line)

    def play_turn(self):
        input("Press Enter to roll the dice...")
        dice_roll = self.roll_dice()
        print(f"You rolled a {dice_roll}")
        self.player_pos = self.move_player(self.player_pos, dice_roll)
        print(f"You are now at position {self.player_pos}")

    def computer_turn(self):
        dice_roll = self.roll_dice()
        self.computer_pos = self.move_player(self.computer_pos, dice_roll)
        print(f"Computer rolled a {dice_roll}")
        print(f"Computer is now at position {self.computer_pos}")

    def check_winner(self):
        if self.player_pos == self.finish_line:
            return "Congratulations! You win!"
        elif self.computer_pos == self.finish_line:
            return "Computer wins! Better luck next time!"
        return None

    def play_game(self):
        print("Welcome to Ludo!")
        while True:
            self.play_turn()
            if self.check_winner():
                print(self.check_winner())
                break

            self.computer_turn()
            if self.check_winner():
                print(self.check_winner())
                break

if __name__ == "__main__":
    game = Ludo()
    game.play_game()
