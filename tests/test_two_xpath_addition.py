import unittest

from xpath_string.two_xpath_addition import TwoXpathAddition

param_list_add_two_xpath_without_contains = [
    ('//span', '//div', '//span//div'),
    ('//div|//svg', '//span', '//div//span|//svg//span'),
    ('//div', '//span|//svg', '//div//span|//div//svg')
]


class TestTwoXpathAddition(unittest.TestCase):

    def test_add_two_xpath_without_contains(self):
        for xpath_1, xpath_2, result in param_list_add_two_xpath_without_contains:
            with self.subTest():
                assert TwoXpathAddition(xpath_1, xpath_2).add_two_xpath_together() == result, \
                    'Addition of {} and {} is "{}" different than expected "{}"'.format(
                        xpath_1, xpath_2, TwoXpathAddition(xpath_1, xpath_2).add_two_xpath_together(), result)
