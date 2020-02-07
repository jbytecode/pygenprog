import random

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
        return {
            "type": "BinaryOperator",
            "op": self.opname,
            "result": self.resultRegister,
            "operand1": self.operand1,
            "operand2": self.operand2
        }

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
        return {
            "type": "UnaryOperator",
            "op": self.opname,
            "result": self.resultRegister,
            "operand": self.operand
        }

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



variablePool = {
    "r[0]": 1,
    "r[1]": 1
}

b1 = Plus()
b1.generateRandomCode(variablePool, [1,2,3])
b2 = Minus()
b2.generateRandomCode(variablePool, [1,2,3])

print([str(b1), str(b2)])

b1.eval(variablePool)
b2.eval(variablePool)

print(variablePool)
