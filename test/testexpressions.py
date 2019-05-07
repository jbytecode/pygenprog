import unittest
from gp.interpreter import *

class TestExpressions(unittest.TestCase):

    def test_plus_expression(self):
        envir = Environment()
        pe = PlusExpression(
            [
                NumericExpression([100]),
                NumericExpression([960])
            ]
        )
        result = pe.eval(envir)
        self.assertEqual(1060, result)


    def test_minus_expression(self):
        envir = Environment()
        pe = MinusExpression(
            [
                NumericExpression([100]),
                NumericExpression([960])
            ]
        )
        result = pe.eval(envir)
        self.assertEqual(-860, result)


    def test_product_expression(self):
        envir = Environment()
        pe = ProductExpression(
            [
                NumericExpression([100]),
                NumericExpression([960])
            ]
        )
        result = pe.eval(envir)
        self.assertEqual(96000, result)


    def test_divide_expression(self):
        envir = Environment()
        pe = DivideExpression(
            [
                NumericExpression([1000]),
                NumericExpression([100])
            ]
        )
        result = pe.eval(envir)
        self.assertEqual(10, result)



if __name__ == '__main__':
    unittest.main()