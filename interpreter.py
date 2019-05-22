import math

class Symbol:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def __str__(self):
        return str(self.symbol)

    def __repr__(self):
        return "SYM(" + str(self.symbol) + ")"

    

class Environment:
    def __init__(self):
        self.variablepool = {}

    def getVariable(self, varname):
        return self.variablepool[varname]

    def setVariable(self, varname, value):
        self.variablepool[varname] = value


class Expression:
    def __init__(self, args):
        self.args = args

    def eval(self, envir):
        pass

    def getArgs(self) -> list:
        return self.args

    @staticmethod
    def getParametersCount():
        pass

    def toPostFix(self) -> list:
        pass


class NumericExpression(Expression):
    def __init__(self, args):
        Expression.__init__(self, args)

    def eval(self, envir):
        return self.args[0]
    
    @staticmethod
    def getParametersCount():
        return 1

    def __str__(self):
        return str(self.args[0])

    def toPostFix(self):
        return ([self.args[0]])

class IdentifierExpression(Expression):
    def __init__(self, args):
        Expression.__init__(self, args)

    def eval(self, envir: Environment):
        return envir.variablepool[self.args[0]]

    @staticmethod
    def getParametersCount():
        return 1

    def __str__(self):
        return str(self.args[0])

    def toPostFix(self):
        return ([self.args[0]])


class PlusExpression(Expression):
    def __init__(self, args):
        Expression.__init__(self, args)

    def eval(self, envir):
        return self.args[0].eval(envir) + self.args[1].eval(envir)

    @staticmethod
    def getParametersCount():
        return 2

    def __str__(self):
        return ("(" + str(self.args[0]) + " + " + str(self.args[1]) + ")")

    def toPostFix(self):
        result = []
        result.extend(self.args[0].toPostFix())
        result.extend(self.args[1].toPostFix())
        result.extend([Symbol("+")])
        return(result)
    
        

class MinusExpression(Expression):
    def __init__(self, args):
        Expression.__init__(self, args)

    def eval(self, envir):
        return self.args[0].eval(envir) - self.args[1].eval(envir)

    @staticmethod
    def getParametersCount():
        return 2

    def __str__(self):
        return ("(" + str(self.args[0]) + " - " + str(self.args[1]) + ")")

    def toPostFix(self):
        return self.args[0].toPostFix().extend(
            [
            self.args[1].toPostFix(),
            Symbol("-")
            ]
        )

class ProductExpression(Expression):
    def __init__(self, args):
        Expression.__init__(self, args)

    def eval(self, envir):
        return self.args[0].eval(envir) * self.args[1].eval(envir)

    @staticmethod
    def getParametersCount():
        return 2

    def __str__(self):
        return ("(" + str(self.args[0]) + " * " + str(self.args[1]) + ")")

    def toPostFix(self):
        return self.args[0].toPostFix().extend(
            [
            self.args[1].toPostFix(),
            Symbol("*")
            ]
        )


class DivideExpression(Expression):
    def __init__(self, args):
        Expression.__init__(self, args)

    def eval(self, envir):
        return self.args[0].eval(envir) / self.args[1].eval(envir)

    @staticmethod
    def getParametersCount():
        return 2

    def __str__(self):
        return ("(" + str(self.args[0]) + " / " + str(self.args[1]) + ")")

    def toPostFix(self):
        return self.args[0].toPostFix().extend(
            [
            self.args[1].toPostFix(),
            Symbol("/")
            ]
        )

class AbsExpression(Expression):

    def __init__(self, args):
        Expression.__init__(self, args)
    
    def eval(self, envir):
        return abs(self.args[0].eval(envir))

    @staticmethod
    def getParametersCount():
        return 1
    
    def __str__(self):
        return "|" + str(self.args[0]) + "|";

    def toPostFix(self):
        return self.args[0].toPostFix().extend(
            [
            Symbol("abs")
            ]
        )

class LogarithmExpression(Expression):
    
    def __init__(self, args):
        return Expression.__init__(self, args)

    def eval(self, envir):
        return math.log2(self.args[0].eval(envir))
    
    @staticmethod
    def getParametersCount():
        return 1

    def __str__(self):
        return "log(" + str(self.args[0]) + ")"

    def toPostFix(self):
        return self.args[0].toPostFix().extend(
            [
            Symbol("log")
            ]
        )