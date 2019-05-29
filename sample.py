from gp import *

if __name__ == "__main__":
    varlist = {"x": 1}
    constantpool = [i  for i in range(1,11)]
    myfunclist = FunctionListCompact

    def f (code):
        x = [1,2,3,4,5]
        y = [(2 * element  + 3) for element in x]
        total = 0.0
        for i in range(len(x)):
            resulti = postfixeval(code, myfunclist, {"x": x[i]})[0]
            total = total + math.pow(y[i] - resulti, 2.0)
        return -total


    gp = GP(f, myfunclist ,varlist,constantpool, popsize = 100,  deep = 20, maxdeep = 20)
    gp.createRandomPopulation()
    for i in range(1):
        gp.iterate()

    gp.interactive()

    #gp.calculateFitness()
    #best = gp.getBest()
    #print(str(best.code))
    #print(postfix2infix(best.code, myfunclist, {"x": "x"}))
    #print(best.eval())