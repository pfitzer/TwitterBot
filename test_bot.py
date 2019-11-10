import unittest
from bots.favretweet import FavRetweetListener
from unittest.mock import MagicMock
import tweepy


class TwitterBotTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.api = tweepy.API()

    def test_on_status(self):
        bot = FavRetweetListener(self.api)
        bot.on_status()


if __name__ == '__main__':
    unittest.main()


