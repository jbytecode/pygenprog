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

    @staticmethod
    def getParametersCount():
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

