import unittest
from hangman import Bank, Player, Processes
import utils


class TestHangmanGame(unittest.TestCase):

    def setUp(self) -> None:
        self.word_bank = Bank()
        self.player1 = Player()
        self.game = Processes()

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

    @unittest.skipIf(utils.request_to_api().status_code == 200, 'test_pic_word => connection OK')
    def test_pic_word(self):
        """if can't connect to api server"""
        print('pick word')
        self.word_bank.pick_topic()
        self.assertIn(self.word_bank.pick_word(),
                      [f'Word is {len(item)} letters long.\n{["_" for word in item]}'
                      for item in Bank.colours + Bank.animals]
                      )


if __name__ == "__main__":
    unittest.main()
