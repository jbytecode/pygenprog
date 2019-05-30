from gp import *

if __name__ == "__main__":
    varlist = {"x1": 1, "x2": 1}
    constantpool = [i  for i in range(1,3)]
    myfunclist = FunctionListCompact

    def f (code):
        x1 = [1,2,3,4,5]
        x2 = [6,5,4,5,4]
        y = []
        #y =  [22, 21, 20, 25, 24]
        for i in range(len(x1)):
            y.append(5 + 4 * x1[i] + 3*x2[i])
        
        total = 0.0
        for i in range(len(x1)):
            resulti = postfixeval(code, myfunclist, {"x1": x1[i], "x2": x2[i]})[0]
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