class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.player_choices = []

    def check_winner(self):
        if all(item in self.player_choices for item in [1, 2, 3]):
            return f'{self.name} Winner'
        elif all(item in self.player_choices for item in [4, 5, 6]):
            return f'{self.name} Winner'
        elif all(item in self.player_choices for item in [7, 8, 9]):
            return f'{self.name} Winner'
        elif all(item in self.player_choices for item in [1, 4, 7]):
            return f'{self.name} Winner'
        elif all(item in self.player_choices for item in [2, 5, 8]):
            return f'{self.name} Winner'
        elif all(item in self.player_choices for item in [3, 6, 9]):
            return f'{self.name} Winner'
        elif all(item in self.player_choices for item in [1, 5, 9]):
            return f'{self.name} Winner'
        elif all(item in self.player_choices for item in [3, 5, 7]):
            return f'{self.name} Winner'