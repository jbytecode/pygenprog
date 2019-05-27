
import math

class GpFunction:
    name = "no name"
    numparams = 0
    def __init__(self, name: str, numparams: int):
        self.name = name;
        self.numparams = numparams
    def eval(self, params: list):
        pass

class PlusFunction (GpFunction):
    def eval(self, params: list):
        param1 = params.pop()
        param2 = params.pop()
        params.append(param1 + param2)

class MinusFunction (GpFunction):
    def eval(self, params: list):
        param1 = params.pop()
        param2 = params.pop()
        params.append(param1 - param2)

class ProductFunction (GpFunction):
    def eval(self, params: list):
        param1 = params.pop()
        param2 = params.pop()
        params.append(param1 * param2)

class DivideFunction (GpFunction):
    def eval(self, params: list):
        param1 = params.pop()
        param2 = params.pop()
        try:
            result = param1 / param2
        except:
            result = float("-inf")
        params.append(result)

class PowerFunction (GpFunction):
    def eval(self, params: list):
        param1 = params.pop()
        param2 = params.pop()
        params.append(math.pow(param1, param2))


class LogFunction (GpFunction):
    def eval(self, params: list):
        param = params.pop()
        try:
            result = math.log(param)
        except:
            result = float("-inf")
        params.append(result)

    
def findFunction(funcname: str, gpFunctionList: [GpFunction]):
    for gpfunc in gpFunctionList:
        if gpfunc.name == funcname:
            return gpfunc
    return None

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



if __name__ == "__main__":
    funclist = [
        PlusFunction("+", 2),
        MinusFunction("-", 2)
    ]
    identifiers = {"x": 3, "y": 10}
    print(postfixeval([2,2, "+", "y", "-"], funclist, identifiers))

