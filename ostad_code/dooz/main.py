from players import Player
from settings import Settings
from table import Table
from utils import clear

if __name__ == '__main__':
    # register 2 players
    p1 = Player(input('Player1 Enter your name: '), input('your sign: '))
    p2 = Player(input('Player2 Enter your name: '), input('your sign: '))

    # Settings => Round Count !
    setting = Settings()
    game_round = int(input('Enter number of Game round: '))
    setting.round_count = game_round

    # Play Game
    for i in range(1, game_round + 1):
        table = Table()
        table.table()
        p1.player_choices.clear()
        p2.player_choices.clear()
        while True:
            print(f'round {i}')
            p1_input = int(input('Player 1 set your input [1-9]: '))
            p1.player_choices.append(p1_input)
            table.set(p1_input, p1.sign)
            res = p1.check_winner()
            if res:
                print(res)
                break
            table.table()
            p2_input = int(input('Player 2 set your input [1-9]: '))
            p2.player_choices.append(p2_input)
            res = p2.check_winner()
            if res:
                print(res)
                break
            table.set(p2_input, p2.sign)
            table.table()
