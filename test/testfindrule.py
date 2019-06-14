import unittest 
from gp import *
from interpreter import *

class TestFindRule(unittest.TestCase):

    funclist = [LessThanFunction("<", 4), BiggerThanFunction(">", 4)]
    constantlist = []
    varlist = {"x1": 0, "x2": 0}

    def fitness (self, code):
        # The rule is
        # if x1 > x2 then return x1
        # else if x2 > x1 then return x2
        x1 = [1, 4, 5, 8]
        x2 = [2, 3, 6, 7]
        y =  [2, 4, 6, 8]
        total = 0.0
        for i in range(len(x1)):
            resulti = postfixeval(
                code, self.funclist, {"x1": x1[i], "x2": x2[i]})[0]
            total = total + math.pow(y[i] - resulti, 2.0)
        return -total

    def testFindRule(self):
        gp = GP(self.fitness, self.funclist, self.varlist, 
            self.constantlist, popsize = 100, deep = 1, maxdeep = 1)
        gp.createRandomPopulation()
        gp.iterateN(100)
        gp.sortPopulation()
        self.assertTrue(gp.chromosomes[0].code in
        [
            ['x1', 'x2', 'x1', 'x2', '>'],
            ['x2', 'x1', 'x2', 'x1', '>'],
            ['x2', 'x1', 'x1', 'x2', '<'],
            ['x1', 'x2', 'x2', 'x1', '<']
        ])