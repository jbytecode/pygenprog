from interpreter import *
import random

class GP:
    def __init__(self):
        self.population = []
        self.classlist = []
        self.constantlist = []
        self.identifierList = []

    def addClass(self, clazz):
        self.classlist.append(clazz)

    def getClassList(self):
        return self.classlist

    def addConstant(self, constant: float):
        self.constantlist.append(constant)

    def getConstantList(self):
        return self.constantlist

    def addIdentifierExpression(self, identifierExpression: IdentifierExpression):
        self.identifierList.append(identifierExpression)

    def getIdentifierList(self):
        return self.identifierList

    def generateRandomTerminalExpression(self) -> Expression:
        cls = random.choice(self.classlist)
        paramcount = cls.getParametersCount()
        params = []
        for i in range(1, paramcount + 1):
            if random.uniform(0, 1) < 0.5:
                current_const = random.choice(self.constantlist)
                params.append(NumericExpression([current_const]))
            else:
                current_identifier = random.choice(self.identifierList)
                params.append(current_identifier)
        return cls(params)

   



gp = GP()
env = Environment()

gp.addClass(PlusExpression)
gp.addClass(MinusExpression)
gp.addClass(ProductExpression)
gp.addClass(DivideExpression)

gp.addIdentifierExpression(IdentifierExpression(["x"]))

gp.addConstant(1)
gp.addConstant(2)
gp.addConstant(3)

expr = gp.generateRandomTerminalExpression()
print(expr)
env.setVariable("x", 10)
print(expr.eval(env))