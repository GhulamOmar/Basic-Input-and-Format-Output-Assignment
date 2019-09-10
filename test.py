"""
Program: test.py
Author: Ghulam Omar
Last date modified: 09/10/19
This tests the program for average_score.py.
"""


import unittest
from format_output import average_scores


class MyTestCase(unittest.TestCase):  # test class
    def test_average(self):  # Function definition.
        scores = 3
        self.assertEquals(average_scores.average(85, 95, 90, scores), 90)


if __name__ == '__main__':
    unittest.main()  # call the function.
