
import math

class GpFunction:
    name = "no name"
    numparams = 0
    def __init__(self, name: str, numparams: int):
        self.name = name
        self.numparams = numparams
    def eval(self, params: list):
        pass
    def evalStr(self, params: list):
        pass

class PlusFunction (GpFunction):
    def eval(self, params: list):
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        params.append(param1 + param2)
    def evalStr(self, params: list) -> str:
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        if isnum(param1) and isnum(param2):
            params.append(param1 + param2)
        else:
            params.append("(" + str(param1) + " + " + str(param2) + ")")

class MinusFunction (GpFunction):
    def eval(self, params: list):
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        params.append(param1 - param2)
    def evalStr(self, params: list) -> str:
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        if isnum(param1) and isnum(param2):
            params.append(param1 - param2)
        else:
            params.append("(" + str(param1) + " - " + str(param2) + ")")

class ProductFunction (GpFunction):
    def eval(self, params: list):
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        params.append(param1 * param2)
    def evalStr(self, params: list) -> str:
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        if isnum(param1) and isnum(param2):
            params.append(param1 * param2)
        else:
            params.append("(" + str(param1) + " * " + str(param2) + ")")

class DivideFunction (GpFunction):
    def eval(self, params: list):
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        try:
            result = param1 / param2
        except:
            result = float("-inf")
        params.append(result)
    def evalStr(self, params: list) -> str:
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        if isnum(param1) and isnum(param2):
            params.append(param1 / param2)
        else:
            params.append("(" + str(param1) + " / " + str(param2) + ")")

class PowerFunction (GpFunction):
    def eval(self, params: list):
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        if(param1 > 10^5 or param2 > 10^5 or param1 < -10^5 or param2 < -10^5):
            params.append(float("-inf"))
        else:
            try:
                params.append(math.pow(param1, param2))
            except:
                params.append(float("-inf"))
            


class LogFunction (GpFunction):
    def eval(self, params: list):
        if(len(params) < self.numparams):
            return float("-inf")
        param = params.pop()
        try:
            result = math.log(param)
        except:
            result = float("-inf")
        params.append(result)


class SqrtFunction (GpFunction):
    def eval(self, params: list):
        if(len(params) < self.numparams):
            return float("-inf")
        param = params.pop()
        try:
            result = math.sqrt(param)
        except:
            result = float("-inf")
        params.append(result)


class AbsFunction (GpFunction):
    def eval(self, params: list):
        if(len(params) < self.numparams):
            return float("-inf")
        param = params.pop()
        try:
            if param < 0:
                result = -(param)
            else:
                result = param
        except:
            result = float("-inf")
        params.append(result)


def findFunctionCount (code: str, gpFunctionList: list):
    count = 0
    for codeElement in code:
            gpFuncName = findFunction(codeElement, gpFunctionList)
            if gpFuncName != None: 
                count = count + 1
    return count

def findFunction(funcname: str, gpFunctionList: [GpFunction]):
    for gpfunc in gpFunctionList:
        if gpfunc.name == funcname:
            return gpfunc
    return None

def isnum(p1):
    #t = type(p1).__name__
    #return (t == "float " or t == "int")
    try:
        a = float(p1)
    except:
        return False
    return True


def postfixeval (code: list, gpFunctionList: list, identifiers: list):
    stack = []
    for element in code:
        t = type(element).__name__
        if t == "int"  or t == "float":
            stack.append(element)
        elif t == "str":
            GpFunc = findFunction(element, gpFunctionList)
            if GpFunc != None:
                GpFunc.eval(stack)
            else:
                stack.append(identifiers[element])
    return stack

def postfix2infix (code: list, gpFunctionList: list, identifiers: list):
    stack = []
    for element in code:
        t = type(element).__name__
        if t == "int"  or t == "float":
            stack.append(element)
        elif t == "str":
            GpFunc = findFunction(element, gpFunctionList)
            if GpFunc != None:
                GpFunc.evalStr(stack)
            else:
                stack.append(identifiers[element])
    return stack

    
FunctionListCompact = [
    PlusFunction("+", 2),
    MinusFunction("-", 2),
    ProductFunction("*", 2),
    DivideFunction("/", 2)
]

FunctionListAll = [
    PlusFunction("+", 2),
    MinusFunction("-", 2),
    ProductFunction("*", 2),
    DivideFunction("/", 2),
    PowerFunction("^", 2),
    LogFunction("Log", 1),
    SqrtFunction("Sqrt", 1),
    AbsFunction("Abs", 1)
] 


if __name__ == "__main__":
    funclist = [
        PlusFunction("+", 2),
        MinusFunction("-", 2)
    ]
    identifiers = {"x": 3, "y": 10}
    print(postfixeval([2,2, "+", "y", "-"], funclist, identifiers))

