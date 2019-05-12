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


    def generateRandomExpressionDeep(self, deep: int) -> Expression:
        cls = random.choice(self.classlist)
        if deep == 0:
            obj = self.generateRandomTerminalExpression()
            return obj
        elif deep == 1:
            cls = random.choice(self.classlist)
            left = self.generateRandomTerminalExpression()
            right = self.generateRandomTerminalExpression()
            obj = cls([left, right])
            return obj
        else:
            cls = random.choice(self.classlist)
            left = self.generateRandomExpressionDeep(deep - 1)
            right = self.generateRandomExpressionDeep(deep - 1)
            obj = cls([left, right])
            return obj


gp = GP()
env = Environment()
env.setVariable("x", 10)
env.setVariable("y", 2)

gp.addClass(PlusExpression)
# gp.addClass(MinusExpression)
# gp.addClass(ProductExpression)
# gp.addClass(DivideExpression)
# gp.addClass(AbsExpression)
# gp.addClass(LogarithmExpression)

gp.addIdentifierExpression(IdentifierExpression(["x"]))
gp.addIdentifierExpression(IdentifierExpression(["y"]))

gp.addConstant(1)
gp.addConstant(2)
gp.addConstant(3)
gp.addConstant(4)


expr = gp.generateRandomExpressionDeep(4)
print(expr)
try:
    print(expr.eval(env))
except Exception as ex:
    print("Error: " + ex.__str__())