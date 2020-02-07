import random
import math
from typing import Dict


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
        lenReg = len(registerList)
        lenCons = len(constantList)
        self.resultRegister = registerList[random.randint(0, lenReg - 1)]
        if(random.random() < 0.5):
            self.operand1 = registerList[random.randint(0, lenReg - 1)]
        else:
            self.operand1 = constantList[random.randint(0, lenCons - 1)]
        if(random.random() < 0.5):
            self.operand2 = registerList[random.randint(0, lenReg - 1)]
        else:
            self.operand2 = constantList[random.randint(0, lenCons - 1)]


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
        if (val2 == 0.0):
            localVariablePool[self.resultRegister] = float("Inf")
        else:
            localVariablePool[self.resultRegister] = val1 / val2


class Pow(BinaryOperator):
    def __init__(self):
        super().__init__("^")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        try:
            result = math.pow(val1, val2)
        except OverflowError:
            result = float("inf")
        except ValueError:
            result = float("inf")
        localVariablePool[self.resultRegister] = result

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
        try:
            result = math.exp(val)
        except OverflowError:
            result = float("inf")
        localVariablePool[self.resultRegister] = result


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
        self.verbose = True
        self.detectUnaryAndBinaryTypes()

    def isBinary(self, clazz):
        return BinaryOperator in clazz.mro()

    def isUnary(self, clazz):
        return UnaryOperator in clazz.mro()

    def detectUnaryAndBinaryTypes(self):
        self.TypeNamesUnary = list(filter(self.isUnary, self.TypeNames))
        self.TypeNamesBinary = list(filter(self.isBinary, self.TypeNames))

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

    def getBestCostWithProgram(self):
        mincost = self.costs[0]
        bestprogram = self.population[0]
        for i in range(1, self.popSize):
            if self.costs[i] < mincost:
                mincost = self.costs[i]
                bestprogram = self.population[i]
        return tuple((mincost, bestprogram))

    def tournament(self):
        index1 = random.randint(0, self.popSize - 1)
        index2 = index1
        while index1 == index2:
            index2 = random.randint(0, self.popSize - 1)
        if self.costs[index1] < self.costs[index2]:
            return index1
        else:
            return index2

    def twoPointChrossOver(self, program1, program2):
        if len(program1) < 2 or len(program2) < 2:
            return tuple((program1, program2))
        cutpoints_for1 = random.sample(range(0, len(program1)), 2)
        cutpoints_for2 = random.sample(range(0, len(program2)), 2)
        child1 = []
        child2 = []
        for i in range(0, cutpoints_for1[0]):
            child1.append(program1[i])
        for i in range(cutpoints_for2[0], cutpoints_for2[1]):
            child1.append(program2[i])
        for i in range(0, cutpoints_for1[1]):
            child1.append(program1[i])

        for j in range(0, cutpoints_for2[0]):
            child2.append(program2[j])
        for j in range(cutpoints_for1[0], cutpoints_for1[1]):
            child2.append(program1[j])
        for j in range(0, cutpoints_for2[1]):
            child2.append(program2[j])
        return tuple((child1, child2))

    def pickRandomUnaryOperator(self):
        self.TypeNames.filt

    def mutateBinaryOperator(self, programsegment):
        return programsegment

    def mutateUnaryOperator(self, programsegment):
        return programsegment


    def mutate(self, program):
        length = len(program)
        luckypartindex = random.randint(0, length - 1)
        luckypart = program[luckypartindex]
        newluckypart = luckypart
        if isinstance(luckypart, BinaryOperator):
            newluckypart = self.mutateBinaryOperator(luckypart)
        elif isinstance(luckypart, UnaryOperator):
            newluckypart = self.mutateUnaryOperator(luckypart)
        else:
            raise Exception(str(luckypart) + " is neither unary nor a binary operator")
        program[luckypartindex] = newluckypart
        return program

    def iterate(self):
        newpop = []
        self.calculateCosts()
        bestcost, bestprogram = self.getBestCostWithProgram()
        if(self.verbose): print(f"*** Last best cost: {bestcost}")
        newpop.append(bestprogram)
        while len(newpop) < self.popSize:
            bestParentIndex1 = self.tournament()
            bestParentIndex2 = self.tournament()
            parent1 = self.population[bestParentIndex1]
            parent2 = self.population[bestParentIndex2]
            offspring1, offspring2 = self.twoPointChrossOver(parent1, parent2)
            offspring1 = self.mutate(offspring1)
            offspring2 = self.mutate(offspring2)
            if len(newpop) < self.popSize:
                newpop.append(offspring1)
            else:
                break
            if len(newpop) < self.popSize:
                newpop.append(offspring2)
            else:
                break
        self.population = newpop

    def getResult(self):
        self.calculateCosts()
        bestcost, bestprogram = self.getBestCostWithProgram()
        resultdict = tuple((
            bestcost,
            str(bestprogram)
        )
        )
        return resultdict


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
variablePool: Dict[str, int] = {
    "r[0]": 1,
    "r[1]": 1,
    "r[2]": 1
}

constantPool = [
    1.0, 2.0, 3.0
]


def fitness(program):
    varPool = variablePool.copy()
    for line in program:
        line.eval(varPool)
    r0 = varPool["r[0]"]
    r1 = varPool["r[1]"]
    result = math.fabs(r0 - 17) + math.fabs(r1 - 23)
    return result


lp = LinearGP(100, 20, fitness, TypeNames, variablePool, constantPool)
lp.calculateCosts()
print(lp.costs)
for i in range(10):
    lp.iterate()
#print(lp.getResult())
