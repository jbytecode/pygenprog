from gp import *

if __name__ == "__main__":
    varlist = {"x1": 1, "x2": 1}
    constantpool = list(range(1))

    def f (code):
        result1 = postfixeval(code, FunctionListAll, {"x1": 0, "x2": 0})[0]
        result2 = postfixeval(code, FunctionListAll, {"x1": 0, "x2": 1})[0]
        result3 = postfixeval(code, FunctionListAll, {"x1": 1, "x2": 0})[0]
        result4 = postfixeval(code, FunctionListAll, {"x1": 1, "x2": 1})[0]
        total =  abs(result1 - 0) + abs(result2 - 1) + abs(result3 - 1) + abs(result4 - 0)
        return -total   

    gp = GP(f, FunctionListAll ,varlist,constantpool, popsize = 20,  deep = 5, maxdeep=10)
    gp.createRandomPopulation()
    for i in range(100):
        gp.iterate()

    gp.calculateFitness()
    best = gp.getBest()
    print(str(best.code))
    print(best.eval())