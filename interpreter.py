
import math

# Defines the abstract class for
# all functions used in a genetic 
# programming search
class GpFunction:
    name = "no name"
    numparams = 0
    def __init__(self, name: str, numparams: int):
        self.name = name
        self.numparams = numparams
    # Evaluates the function and returns the result
    def eval(self, params: list):
        pass
    # Returns a human-readable representation of an equation
    # For example, a postfix expression 2 3 + 
    # is evaluated to (2 + 3)
    # Paranthesis are always used because the operator precedence 
    # is satisfied.
    def evalStr(self, params: list):
        pass

# Plus function is a GpFunction
# which takes exactly two arguments
# and returns the sum.
# It is used like
# 2 5 + 
# in postfix notation
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

# Minus function is a GpFunction
# which takes exactly two arguments
# and returns the difference.
# It is used like
# 2 5 - 
# in postfix notation for (5 - 2)
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

# Product function is a GpFunction
# which takes exactly two arguments
# and returns the product.
# It is used like
# 2 5 * 
# in postfix notation for (2 * 5)
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

# Divide function is a GpFunction
# which takes exactly two arguments
# and returns the division.
# It is used like
# 2 5 / 
# in postfix notation for (5 / 2). 
# The result is float.
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

# Power function is a GpFunction
# which takes exactly two arguments
# and returns the power.
# It is used like
# 2 5 ^ 
# in postfix notation for (5 ^ 2)
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

    def evalStr(self, params: list) -> str:
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        if isnum(param1) and isnum(param2):
            try:
                params.append(math.pow(param1, param2))
            except:
                params.append(float("-inf"))
        else:
            params.append("(" + str(param1) + " ^ " + str(param2) + ")")     



# Log function is a GpFunction
# which takes exactly one argument
# and returns the natural logarithm.
# It is used like
# 10 log 
# in postfix notation for ln(10)
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

    def evalStr(self, params: list) -> str:
        if(len(params) < self.numparams):
            return float("-inf")
        param = params.pop()
        if isnum(param):
            try:
                result = math.log(param)
            except:
                result = float("-inf")
            params.append(result)
        else:
            params.append("Log(" + str(param) + ")")


# Sqrt function is a GpFunction
# which takes exactly one argument
# and returns the square root.
# It is used like
# 25 Sqrt 
# in postfix notation for Sqrt(25)
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

    def evalStr(self, params: list) -> str:
        if(len(params) < self.numparams):
            return float("-inf")
        param = params.pop()
        if isnum(param):
            try:
                result = math.log(param)
            except:
                result = float("-inf")
            params.append(result)
        else:
            params.append("Sqrt(" + math.sqrt(param) + ")")


# Abs function is a GpFunction
# which takes exactly one argument
# and returns the absolute value.
# It is used like
# 10 Abs 
# in postfix notation for |10|
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

    def evalStr(self, params: list) -> str:
        if(len(params) < self.numparams):
            return float("-inf")
        param = params.pop()
        if isnum(param):
            try:
                result = abs(param)
            except:
                result = float("-inf")
            params.append(result)
        else:
            params.append("Abs(" + str(param) + ")")



# LessThan function is a GpFunction
# which takes exactly four arguments
# if args1 < args2 then return args3 else return args4
# It is used like
# 1 2 3 4 < 
# in postfix notation for "if 4 < 3 then return 2 else return 1"
class LessThanFunction (GpFunction):
    def eval(self, params: list):
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        param3 = params.pop()
        param4 = params.pop()
        try:
            if(param1 < param2):
                result = param3
            else:
                result = param4
        except:
            result = float("-inf")
        params.append(result)

    def evalStr(self, params: list) -> str:
        if(len(params) < self.numparams):
            return float("-inf")
        param1 = params.pop()
        param2 = params.pop()
        param3 = params.pop()
        param4 = params.pop()
        params.append("(" + str(param1) + " < " + str(param2)  + " ? " + str(param3) + " : " + str(param4) + ")")



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
        float(p1)
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

