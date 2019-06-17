from gp import *

if __name__ == "__main__":
    varlist = {"x": None}
    constantpool = [i for i in range(1, 5)]
    myfunclist = [
        PlusFunction("+", 2),
        MinusFunction("-", 2),
        ProductFunction("*", 2),
        DivideFunction("/", 2),
        AbsFunction("Abs", 1),
        ExpFunction("Exp", 1)
    ]

    x = []
    y = []
    count = 0
    x1 = -5
    deltax1 = 0.1
    while (count < 100):
        x.append(x1)
        y.append(1.0 / (1.0 + math.exp(-x1)))
        x1 = x1 + deltax1
        count = count + 1

    def f(code):
        total = 0.0
        for i in range(len(x)):
            resulti = postfixeval(
                code, myfunclist, {"x": x[i]})[0]
            total = total + (y[i] - resulti) * (y[i] - resulti)
        return -total

    gp = GP(f, myfunclist, varlist, constantpool,
            popsize=100, deep=3, maxdeep=3)
    gp.addMustInclude("x")
    gp.addMustInclude("Exp")
    gp.setIsShortestBest(False)
    gp.createRandomPopulation()

    gp.interactive()
