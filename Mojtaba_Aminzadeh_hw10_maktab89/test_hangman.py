import unittest
from hangman import Bank, Player, Processes
import utils

RED = "\u001b[31m"
END = "\u001b[37m"


class TestHangmanBank(unittest.TestCase):

    def setUp(self) -> None:
        self.word_bank = Bank()

    def test_pic_topic(self):
        topic_name = Bank.topic_names
        self.assertIn(self.word_bank.pick_topic(), [f'Topic: {name}' for name in topic_name])
        self.assertIsInstance(self.word_bank.pick_topic(), str)

    @unittest.skipIf(not utils.is_connect('8.8.8.8') or
                     utils.request_to_api().status_code != 200,
                     'test_get_word_from_api_ok => connection disable OR response != 200')
    def test_get_word_from_api_ok(self):
        """if network connection OK"""
        self.assertTrue(self.word_bank.get_word())

    @unittest.skipIf(utils.request_to_api().status_code == 200,
                     'test_get_word_from_api_fail => connection to api server <OK:200>')
    def test_get_word_from_api_fail(self):
        """if network connection timeout"""
        self.assertFalse(self.word_bank.get_word())

    @unittest.skipIf(utils.is_connect('8.8.8.8'), 'test_get_word_from_api_request_exception => connection OK')
    def test_get_word_from_api_request_exception(self):
        self.assertFalse(self.word_bank.get_word())

    def test_pic_word(self):
        """if can't connect to api server"""
        self.word_bank.pick_topic()
        self.assertIn(self.word_bank.pick_word(),
                      [f'Word is {len(item)} letters long.\n{["_" for word in item]}'
                      for item in Bank.colours + Bank.animals]
                      )

    def test_check_not_solve_True(self):
        self.word_bank.letters_guessed_counter = 1
        self.word_bank.current_word = 'abc'
        self.word_bank.check_solve()
        self.assertTrue(self.word_bank.not_solved)

    def test_check_not_solve_False(self):
        self.word_bank.letters_guessed_counter = 3
        self.word_bank.current_word = 'abc'
        self.word_bank.check_solve()
        self.assertFalse(self.word_bank.not_solved)


class TestHangmanPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank()
        self.bank.current_word = 'abc'
        self.player1 = Player(self.bank.current_word)

    def test_guess(self):
        print(f'{RED}input single character for test.{END}')
        self.player1.guess()
        self.assertEqual(self.player1.answer, self.player1.answer.lower())

    def test_player_lives_x3(self):
        self.assertEqual(self.player1.lives, 9)


class TestHangmanProcesses(unittest.TestCase):
    def setUp(self) -> None:
        self.processes = Processes()
        self.bank = Bank()
        self.player1 = Player(self.bank.current_word)

    def test_validate_user_input(self):
        self.player1.answer = ''
        self.assertTrue(self.processes.validate_user_input(player=self.player1))

        self.player1.answer = ' '
        self.assertTrue(self.processes.validate_user_input(player=self.player1))

        self.player1.answer = 'ab'
        self.assertTrue(self.processes.validate_user_input(player=self.player1))

        self.player1.answer = '1'
        self.assertTrue(self.processes.validate_user_input(player=self.player1))

        self.player1.answer = 'a1'
        self.assertTrue(self.processes.validate_user_input(player=self.player1))

        self.player1.answer = 'a'
        self.assertFalse(self.processes.validate_user_input(player=self.player1))

        self.player1.answer = 'F'
        self.assertFalse(self.processes.validate_user_input(player=self.player1))

    def test_check_answer_update_lives(self):
        self.bank.letters_already_guessed = ['a', 'b']
        self.player1.answer = 'a'
        result = self.processes.check_answer_update_lives(bank=self.bank, player=self.player1)
        self.assertEqual(result, '\nLetter already guessed.')

        self.bank.current_word = 'blue'
        self.player1.answer = 'x'
        self.player1.lives = 10
        result = self.processes.check_answer_update_lives(bank=self.bank, player=self.player1)
        self.assertEqual(result, '\nNope!\nLives remaining: {}'.format(self.player1.lives))
        self.assertEqual(self.player1.lives, 9)
        self.assertIn(self.player1.answer, self.bank.letters_already_guessed)

        self.bank.current_word = 'red'
        self.player1.answer = 'r'
        self.bank.current_word_display = ['_', '_', '_']
        self.bank.letters_guessed_counter = 0
        self.bank.letters_already_guessed = []
        result = self.processes.check_answer_update_lives(bank=self.bank, player=self.player1)
        self.assertEqual(result, '\nNice!')
        self.assertEqual(self.bank.letters_guessed_counter, 1)
        self.assertEqual(self.bank.letters_already_guessed, ['r'])


if __name__ == "__main__":
    unittest.main()
