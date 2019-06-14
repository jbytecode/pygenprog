import unittest
from interpreter import *
from gp import *
import random


class TestGp (unittest.TestCase):

    varlist = {"x1": 1, "x2": 1}
    constantlist = [0, 1]
    funclist = [LessThanFunction("<", 4), EqualsFunction("=", 4), BiggerThanFunction(">", 4)]

    def xorfitness(self, code):
        x1 = [1, 0, 1, 0]
        x2 = [0, 0, 1, 1]
        y = [1, 0, 0, 1]
        total = 0.0
        for i in range(len(x1)):
            resulti = postfixeval(
                code, self.funclist, {"x1": x1[i], "x2": x2[i]})[0]
            total = total + math.pow(y[i] - resulti, 2.0)
        return -total

    def testXor(self):
        random.seed(1610)
        gp = GP(self.xorfitness, self.funclist, self.varlist, self.constantlist,
                popsize=50, deep=3, maxdeep=3)
        gp.createRandomPopulation()
        gp.iterateN(100)
        gp.sortPopulation()
        self.assertEqual(0.0, gp.chromosomes[0].fitness)
