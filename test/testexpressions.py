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

    def test_postfix_plus_str(self):
        code = [2, "x", "+"]
        funclist = [PlusFunction("+", 2)]
        result = postfix2infix(code, funclist, {"x": "x"})
        self.assertEqual(result[0], "(x + 2)")

    def test_postfix_minus_str(self):
        code = [2, "x", "-"]
        funclist = [MinusFunction("-", 2)]
        result = postfix2infix(code, funclist, {"x": "x"})
        self.assertEqual(result[0], "(x - 2)")

    def test_postfix_product_str(self):
        code = [2, "x", "*"]
        funclist = [ProductFunction("*", 2)]
        result = postfix2infix(code, funclist, {"x": "x"})
        self.assertEqual(result[0], "(x * 2)")


    def test_postfix_divide_str(self):
        code = [2, "x", "/"]
        funclist = [DivideFunction("/", 2)]
        result = postfix2infix(code, funclist, {"x": "x"})
        self.assertEqual(result[0], "(x / 2)")


    def test_postfix_power_str(self):
        code = [2, "x", "^"]
        funclist = [PowerFunction("^", 2)]
        result = postfix2infix(code, funclist, {"x": "x"})
        self.assertEqual(result[0], "(x ^ 2)")


    def test_postfix_log_str(self):
        code = ["x", "Log"]
        funclist = [LogFunction("Log", 1)]
        result = postfix2infix(code, funclist, {"x": "x"})
        self.assertEqual(result[0], "Log(x)")

    def test_postfix_log2_str(self):
        code = [math.exp(1), "Log"]
        funclist = [LogFunction("Log", 1)]
        result = postfix2infix(code, funclist, {"x": "x"})
        self.assertEqual(result[0], 1.0)


if __name__ == '__main__':
    unittest.main()