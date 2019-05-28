import unittest
from interpreter import *

class TestExpressions(unittest.TestCase):

    def test_postfix_expression(self):
        funclist = [
            PlusFunction("+", 2),
            MinusFunction("-", 2)
        ]
        identifiers = {"x": 3, "y": 10}
        result = postfixeval([2,2, "+", "y", "-"], funclist, identifiers)
        self.assertEqual(result[0], 6)



if __name__ == '__main__':
    unittest.main()