from gp import *

if __name__ == "__main__":
    varlist = {"x1": 1, "x2": 1}
    constantpool = [i for i in range(1, 5)]
    myfunclist = [
        PlusFunction("+", 2),
        MinusFunction("-", 2),
        ProductFunction("*", 2),
        DivideFunction("/", 2),
        AbsFunction("Abs", 1)
    ]

    def f(code):
        x1 = [1, 0, 1, 0]
        x2 = [0, 0, 1, 1]
        y = [1, 0, 0, 1]

        total = 0.0
        for i in range(len(x1)):
            resulti = postfixeval(
                code, myfunclist, {"x1": x1[i], "x2": x2[i]})[0]
            total = total + math.pow(y[i] - resulti, 2.0)
        return -total

    gp = GP(f, myfunclist, varlist, constantpool,
            popsize=100,  deep=3, maxdeep=3)
    gp.createRandomPopulation()

    gp.interactive()
