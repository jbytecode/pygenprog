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

    def generateRandomExpression(self) -> Expression:
        cls = random.choice(self.classlist)
        left = self.generateRandomTerminalExpression()
        right = self.generateRandomTerminalExpression()
        obj = cls([left, right])
        return obj

    def generateRandomExpressionDeep2(self) -> Expression:
        cls = random.choice(self.classlist)
        left = self.generateRandomExpression()
        right = self.generateRandomExpression()
        obj = cls([left, right])
        return obj
    
    def generateRandomExpressionDeep4(self) -> Expression:
        cls = random.choice(self.classlist)
        left = self.generateRandomExpressionDeep2()
        right = self.generateRandomExpressionDeep2()
        obj = cls([left, right])
        return obj

    def generateRandomExpressionDeep8(self) -> Expression:
        cls = random.choice(self.classlist)
        left = self.generateRandomExpressionDeep4()
        right = self.generateRandomExpressionDeep4()
        obj = cls([left, right])
        return obj


gp = GP()
env = Environment()
env.setVariable("x", 10)

gp.addClass(PlusExpression)
gp.addClass(MinusExpression)
gp.addClass(ProductExpression)
gp.addClass(DivideExpression)
gp.addClass(AbsExpression)
gp.addClass(LogarithmExpression)

gp.addIdentifierExpression(IdentifierExpression(["x"]))

gp.addConstant(1)
gp.addConstant(2)
gp.addConstant(3)
gp.addConstant(4)


expr = gp.generateRandomExpressionDeep8()
print(expr)
print(expr.eval(env))