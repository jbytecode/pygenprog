import random
import math

class Operator:
    def eval(self):
        pass

    def EvalSingleArgument(self, argument, localVariablePool):
        tt = type(argument).__name__
        if tt == 'float' or tt == 'int':
            return argument
        else:
            return localVariablePool[argument]

class BinaryOperator(Operator):
    """
    General class for Binary Operations, eval should be implemented by user
    r[i] = r[j] OP r[h],
    r[i] = r[j] OP Constant,
    r[i] = Constant OP r[h],
    r[i] = Constant OP Constant,
    type operations are handled
    """
    def __init__(self, opname):
        self.opname = opname
        self.resultRegister = None
        self.operand1 = None
        self.operand2 = None

    def generateRandomCode(self, registerDict, constantList):
        registerList = list(registerDict)
        allOperandList = registerList + constantList
        lenReg = len(registerList)
        lenAll = len(allOperandList)
        self.resultRegister = registerList[random.randint(0, lenReg - 1)]
        self.operand1 = allOperandList[random.randint(0, lenAll - 1)]
        self.operand2 = allOperandList[random.randint(0, lenAll -1)]

    def __repr__(self):
        return str({
            "type": "BinaryOperator",
            "op": self.opname,
            "result": self.resultRegister,
            "operand1": self.operand1,
            "operand2": self.operand2
        })

    def __str__(self):
        return str(self.__repr__())


class UnaryOperator(Operator):
    """
        General class for Unary Operations or single argument functions eval should be implemented by user
        r[i] = OP(r[j]),
        r[i] = OP(Constant)
        type operations are handled
        """
    def __init__(self, opname):
        self.opname = opname
        self.resultRegister = None
        self.operand = None

    def generateRandomCode(self, registerDict, constantList):
        registerList = list(registerDict)
        allOperandList = registerList + constantList
        lenReg = len(registerList)
        lenAll = len(allOperandList)
        self.resultRegister = registerList[random.randint(0, lenReg - 1)]
        self.operand = allOperandList[random.randint(0, lenAll - 1)]

    def __repr__(self):
        return str({
            "type": "UnaryOperator",
            "op": self.opname,
            "result": self.resultRegister,
            "operand": self.operand
        })

    def __str__(self):
        return str(self.__repr__())



class Plus(BinaryOperator):
    def __init__(self):
        super().__init__("+")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        localVariablePool[self.resultRegister] = val1 + val2

class Minus(BinaryOperator):
    def __init__(self):
        super().__init__("-")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        localVariablePool[self.resultRegister] = val1 - val2

class Product(BinaryOperator):
    def __init__(self):
        super().__init__("*")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        localVariablePool[self.resultRegister] = val1 * val2


class Divide(BinaryOperator):
    def __init__(self):
        super().__init__("/")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        if(val2 == 0.0):
            localVariablePool[self.resultRegister] = float("Inf")
        else:
            localVariablePool[self.resultRegister] = val1 / val2

class Pow(BinaryOperator):
    def __init__(self):
        super().__init__("^")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        localVariablePool[self.resultRegister] = math.pow(val1, val2)


class Negate(UnaryOperator):
    def __init__(self):
        super().__init__("(-)")

    def eval(self, localVariablePool):
        val = self.EvalSingleArgument(self.operand, localVariablePool)
        localVariablePool[self.resultRegister] = -val


class Exp(UnaryOperator):
    def __init__(self):
        super().__init__("Exp")

    def eval(self, localVariablePool):
        val = self.EvalSingleArgument(self.operand, localVariablePool)
        localVariablePool[self.resultRegister] = math.exp(val)


class Log(UnaryOperator):
    def __init__(self):
        super().__init__("Log")

    def eval(self, localVariablePool):
        val = self.EvalSingleArgument(self.operand, localVariablePool)
        if val <= 0:
            localVariablePool[self.resultRegister] = float("Inf")
        else:
            localVariablePool[self.resultRegister] = math.log(val)


def runProgram(codeList, variablePoolDict):
    for line in codeList:
        line.eval(variablePoolDict)


class LinearGP:
    def __init__(self, popSize, initialLineCount, costFunction, TypeNames, variablePool, constantPool):
        self.TypeNames = TypeNames
        self.variablePool = variablePool
        self.constantPool = constantPool
        self.popSize = popSize
        self.costFunction = costFunction
        self.initialLineCount = initialLineCount
        self.population = []
        self.costs = [None] * popSize
        self.createRandomPopulation()


    def createRandomPopulation(self):
        self.population = []
        for i in range(self.popSize):
            program = self.generateProgram(
                self.TypeNames,
                self.variablePool,
                self.constantPool
            )
            self.population.append(program)

    def generateProgram(self, typePoolList, variablePoolDict, constantPoolList):
        program = []
        for index in range(self.initialLineCount):
            opIndex = random.randint(0, len(typePoolList) - 1)
            optype = typePoolList[opIndex]
            opObject = optype()
            opObject.generateRandomCode(variablePoolDict, constantPoolList)
            program.append(opObject)
        return program

    def calculateCosts(self):
        for i in range(self.popSize):
            self.costs[i] = self.costFunction(self.population[i])

    def tournament(self):
        index1 = random.randint(0, self.popSize - 1)
        index2 = index1
        while index1 != index2:
            index2 = random.randint(0, self.popSize - 1)
        if(self.costs[index1] < self.costs[index2]):
            return index1
        else:
            return index2

    def iterate(self):
        newpop = []
        self.calculateCosts()
        while len(newpop) <= self.popSize:
            bestParentIndex1 = self.tournament()
            bestParentIndex2 = self.tournament()
            newpop.append(self.population[bestParentIndex1])
            newpop.append(self.population[bestParentIndex2])
        self.population = newpop

TypeNames = [
    Plus,
    Minus,
    Product,
    Divide,
    Negate,
    Exp,
    Pow,
    Log
]



### End of library ###
variablePool = {
    "r[0]": 1,
    "r[1]": 1,
    "r[2]": 1
}
constantPool = [
    1, 2, 3
]

def fitness (program):
    varPool = variablePool.copy()
    for line in program:
        line.eval(varPool)
    r0 = varPool["r[0]"]
    r1 = varPool["r[1]"]
    result = math.fabs(r0 - 17)
    return result

lp = LinearGP(10 ,5, fitness, TypeNames, variablePool, constantPool)
lp.calculateCosts()
print(lp.costs)
lp.iterate()
lp.calculateCosts()
print(lp.costs)