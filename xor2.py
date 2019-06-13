from gp import *

if __name__ == "__main__":
    varlist = {"x1": 1, "x2": 1}
    constantpool = [0, 1]
    myfunclist = [
        EqualsFunction("==", 4),
        NotEqualsFunction("!=", 4)
        ]

    def f (code):
        x1 = [1, 0, 1, 0]
        x2 = [0, 0, 1, 1]
        y  = [1, 0, 0, 1]
        
        total = 0.0
        for i in range(len(x1)):
            resulti = postfixeval(code, myfunclist, {"x1": x1[i], "x2": x2[i]})[0]
            total = total + math.pow(y[i] - resulti, 2.0)
        return -total


    gp = GP(f, myfunclist ,varlist,constantpool, popsize = 100,  deep = 10, maxdeep = 10)
    gp.createRandomPopulation()
    for i in range(1):
        gp.iterate()

    gp.interactive()
    