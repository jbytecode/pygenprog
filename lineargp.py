import random
import math
from typing import Dict


class Operator:
    def eval(self):
        pass

    def prettyPrint(self):
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
        registerListWithY = registerList.copy();
        registerListWithY.append("y")
        lenReg = len(registerList)
        lenRegWithY = len(registerListWithY)
        lenCons = len(constantList)
        self.resultRegister = registerListWithY[random.randint(0, lenRegWithY - 1)]
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

    def prettyPrint(self):
        print(f"{self.resultRegister} = {self.operand1} {self.opname} {self.operand2}")


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

    def prettyPrint(self):
        print(f"{self.resultRegister} = {self.opname} {self.operand}")

class Plus(BinaryOperator):
    def __init__(self):
        super().__init__("+")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        try:
            localVariablePool[self.resultRegister] = val1 + val2
        except:
            localVariablePool[self.resultRegister] = float("inf")

class Minus(BinaryOperator):
    def __init__(self):
        super().__init__("-")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        try:
            localVariablePool[self.resultRegister] = val1 - val2
        except:
            localVariablePool[self.resultRegister] = float("inf")

class Product(BinaryOperator):
    def __init__(self):
        super().__init__("*")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        try:
            localVariablePool[self.resultRegister] = val1 * val2
        except:
            localVariablePool[self.resultRegister] = float("inf")

class Divide(BinaryOperator):
    def __init__(self):
        super().__init__("/")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        try:
            localVariablePool[self.resultRegister] = val1 / val2
        except:
            localVariablePool[self.resultRegister] = float("inf")


class Pow(BinaryOperator):
    def __init__(self):
        super().__init__("^")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        try:
            localVariablePool[self.resultRegister]  = math.pow(val1, val2)
        except:
            localVariablePool[self.resultRegister] = float("inf")

class Less(BinaryOperator):
    def __init__(self):
        super().__init__("<")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        try:
            if val1 < val2:
                localVariablePool[self.resultRegister]  = 1
            else:
                localVariablePool[self.resultRegister]  = 0
        except:
            localVariablePool[self.resultRegister] = float("inf")


class Equals(BinaryOperator):
    def __init__(self):
        super().__init__("<")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        try:
            if val1 == val2:
                localVariablePool[self.resultRegister]  = 1
            else:
                localVariablePool[self.resultRegister]  = 0
        except:
            localVariablePool[self.resultRegister] = float("inf")


class Bigger(BinaryOperator):
    def __init__(self):
        super().__init__("<")

    def eval(self, localVariablePool):
        val1 = self.EvalSingleArgument(self.operand1, localVariablePool)
        val2 = self.EvalSingleArgument(self.operand2, localVariablePool)
        try:
            if val1 > val2:
                localVariablePool[self.resultRegister]  = 1
            else:
                localVariablePool[self.resultRegister]  = 0
        except:
            localVariablePool[self.resultRegister] = float("inf")



class Negate(UnaryOperator):
    def __init__(self):
        super().__init__("(-)")

    def eval(self, localVariablePool):
        val = self.EvalSingleArgument(self.operand, localVariablePool)
        try:
            localVariablePool[self.resultRegister] = -val
        except:
            localVariablePool[self.resultRegister] = float("inf")


class Exp(UnaryOperator):
    def __init__(self):
        super().__init__("Exp")

    def eval(self, localVariablePool):
        val = self.EvalSingleArgument(self.operand, localVariablePool)
        try:
            result = math.exp(val)
        except:
            result = float("inf")
        localVariablePool[self.resultRegister] = result


class Log(UnaryOperator):
    def __init__(self):
        super().__init__("Log")

    def eval(self, localVariablePool):
        val = self.EvalSingleArgument(self.operand, localVariablePool)
        try:
            localVariablePool[self.resultRegister] = math.log(val)
        except:
            localVariablePool[self.resultRegister] = float("Inf")


class Abs(UnaryOperator):
    def __init__(self):
        super().__init__("Abs")

    def eval(self, localVariablePool):
        val = self.EvalSingleArgument(self.operand, localVariablePool)
        try:
            localVariablePool[self.resultRegister] = math.fbas(val)
        except:
            localVariablePool[self.resultRegister] = float("Inf")



class LinearGP:
    def __init__(self, popSize, initialLineCount, maximumLineCount, costFunction, TypeNames, variablePool, constantPool):
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
        self.maxProgramLength = maximumLineCount
        self.bestEverFitness = float("inf")
        self.bestEverProgram = []


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

    def min(self, i1, i2):
        if i1 < i2:
            return i1
        else:
            return i2

    def OnePointCrossOver(self, program1, program2):
        l1 = len(program1)
        l2 = len(program2)
        min = self.min(l1, l2)
        child1 = []
        child2 = []
        cutpoint = random.randint(0, min)
        for i in range(0, cutpoint):
            child1.append(program1[i])
        for i in range(cutpoint, l2):
            child1.append(program2[i])
        cutpoint = random.randint(0, min)
        for i in range(0, cutpoint):
            child2.append(program2[i])
        for i in range(cutpoint, l1):
            child2.append(program1[i])
        return tuple((child1, child2))



    def TwoPointCrossOver(self, program1, program2):
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


    def mutateBinaryOperator(self, programsegment):
        if random.random() < 0.80:
            lenops = len(self.TypeNamesBinary)
            randomop = self.TypeNamesBinary[random.randint(0, lenops - 1)]
            newop = randomop()
            newop.operand1 = programsegment.operand1
            newop.operand2 = programsegment.operand2
            newop.resultRegister = programsegment.resultRegister
            return newop
        else:
            programsegment.generateRandomCode(self.variablePool, self.constantPool)
            return programsegment

    def mutateUnaryOperator(self, programsegment):
        #print(f"Mutating {programsegment} to:")
        lenops = len(self.TypeNamesUnary)
        randomop = self.TypeNamesUnary[random.randint(0, lenops - 1)]
        newop = randomop()
        newop.operand = programsegment.operand
        newop.resultRegister = programsegment.resultRegister
        #print(f"this {newop}")
        return newop


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
        if bestcost < self.bestEverFitness:
            self.bestEverFitness = bestcost
            self.bestEverProgram = bestprogram
            print(f"*** Best ever is now {self.bestEverFitness}")
            self.prettyPrintBest()
        #if(self.verbose): print(f"*** Last best cost: {bestcost}")
        newpop.append(bestprogram)
        if len(self.bestEverProgram) > 0:
            newpop.append(self.bestEverProgram)
        else:
            newpop.append(bestprogram)
        while len(newpop) < self.popSize:
            bestParentIndex1 = self.tournament()
            bestParentIndex2 = self.tournament()
            parent1 = self.population[bestParentIndex1]
            parent2 = self.population[bestParentIndex2]
            if random.random() < 0.80:
                offspring1, offspring2 = self.TwoPointCrossOver(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2
            if(random.random() < 0.05):
                offspring1 = self.mutate(offspring1)
                offspring2 = self.mutate(offspring2)
            if(len(list(offspring1)) > self.maxProgramLength):
                offspring1 = offspring1[0:self.maxProgramLength]
            if(len(list(offspring2)) > self.maxProgramLength):
                offspring2 = offspring2[0:self.maxProgramLength]

            if len(newpop) < self.popSize:
                newpop.append(offspring1)
            else:
                break
            if len(newpop) < self.popSize:
                newpop.append(offspring2)
            else:
                break
        self.population = newpop.copy()


    def getResult(self):
        resultdict = tuple((
            self.bestEverFitness,
            str(self.bestEverProgram)
        )
        )
        return resultdict

    def prettyPrintBest(self):
        for row in self.bestEverProgram:
            row.prettyPrint()
        print(f"with cost {self.bestEverFitness}")

TypeNames = [
    Plus,
    Minus,
    Product,
    Divide,
    Negate,
    Exp,
    Pow,
    Log,
    Abs
]




### End of library ###
independentVariablePool: Dict[str, int] = {
    "x1": None,
    "x2": None
}

constantPool = [i for i in range(5)]


def fitness(program):
    x1 = [1, 2, 3, 4]
    x2 = [6, 7, 8, 9]
    k = 1
    y =  [7 * k, 9 * k, 11 * k, 13 * k]
    l = len(y)
    sumsquares = 0.0
    for i in range(l):
        varPool = {"y": None, "x1": x1[i], "x2": x2[i]}
        for line in program:
            line.eval(varPool)
        r0 = varPool["y"]
        try:
            sumsquares += math.pow(r0 - y[i], 2.0)
        except:
            sumsquares = float("inf")
    result = sumsquares
    return result


lp = LinearGP(100, 50, 500, fitness, TypeNames, independentVariablePool, constantPool)

for i in range(200):
    lp.iterate()

print(lp.prettyPrintBest())