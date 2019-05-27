from interpreter import GpFunction
from interpreter import findFunction, postfixeval
from interpreter import PlusFunction, MinusFunction, LogFunction, ProductFunction, DivideFunction
from interpreter import PowerFunction
import random
import math

class Chromosome:
    code = []
    functionlist = [] 
    constantpool = []
    deep = 0
    fitness = float("-inf")

    def __init__(self, functionlist: list, constantpool: list, deep: int):
        self.functionlist = functionlist
        self.deep = deep
        self.constantpool = constantpool
        self.code = []
        for i in range(deep):
            gpfunc = random.choice(functionlist)
            numparams = gpfunc.numparams
            if i == 0:
                k = numparams
            else:
                k = numparams - 1
            cons = random.choices(constantpool, k = k)
            self.code.extend(cons)
            self.code.append(gpfunc.name)

    def __str__(self):
        return(str(self.code))

        
class GP:
    popsize = 100
    fitness = None
    funclist = None
    varlist = None
    constantpool = None
    chromosomes = None
    deep = 3

    def __init__(self, fitness, funclist, varlist, constantpool, popsize = 100, deep = 3):
        self.popsize = popsize
        self.fitness = fitness
        self.varlist = varlist
        self.constantpool = constantpool
        self.chromosomes = []
        self.funclist = funclist
        self.deep = deep
        
    
    def createRandomPopulation(self):
        self.chromosomes = []
        for i in range(self.popsize):
            ch = Chromosome(self.funclist, self.constantpool, self.deep)
            self.chromosomes.append(ch)
        
        
    
    def crossover(self, code1: list, code2: list):
        operator_indices1 = []
        operator_indices2 = []
        newch1 = []
        newch2 = []
        for i in range(len(code1)):
            func = findFunction(code1[i], self.funclist)
            if func != None: 
                operator_indices1.append(i)
        for i in range(len(code2)):
            func = findFunction(code2[i], self.funclist)
            if func != None: 
                operator_indices2.append(i)
        op1_ind = random.choice(operator_indices1)
        op2_ind = random.choice(operator_indices2)
        for i in range(op1_ind + 1):
            newch1.append(code1[i])
        for i in range(op2_ind + 1, len(code2)):
            newch1.append(code2[i])
        for i in range(op2_ind + 1):
            newch2.append(code2[i])
        for i in range(op1_ind + 1, len(code1)):
            newch2.append(code1[i])
        return [newch1, newch2]

    def mutate(self, code: list):
        offspring = code.copy()
        random_index = random.choice(range(len(offspring)))
        element = offspring[random_index]
        t = type(element).__name__
        if(t == "int" or t == "float"):
            luckynum = random.choice(constantpool)
            offspring[random_index] = luckynum
        else:
            gpfunc = findFunction(element, funclist)
            if gpfunc != None:
                luckyfun = random.choice(funclist)
                offspring[random_index] = luckyfun.name
            else:
                luckyvar = random.choice(varlist)
                offspring[random_index] = luckyvar
        return offspring

    def __str__(self):
        return(str(self.chromosomes))

    def iterate(self):
        for i in range(len(self.chromosomes)):
            f = self.fitness(self.chromosomes[i].code)
            self.chromosomes[i].fitness = f
        temppop = []
        for i in range(int(len(self.chromosomes) / 2)):    
            indices1 = random.choice(range(len(self.chromosomes)))
            indices2 = random.choice(range(len(self.chromosomes)))
            if(self.chromosomes[indices1].fitness > self.chromosomes[indices2].fitness):
                parent1 = self.chromosomes[indices1]
            else:
                parent1 = self.chromosomes[indices2]
            indices1 = random.choice(range(len(self.chromosomes)))
            indices2 = random.choice(range(len(self.chromosomes)))
            if(self.chromosomes[indices1].fitness > self.chromosomes[indices2].fitness):
                parent2 = self.chromosomes[indices1]
            else:
                parent2 = self.chromosomes[indices2]
            offsprings = self.crossover(parent1.code, parent2.code)
            offsprings[0] = self.mutate(offsprings[0])
            offsprings[1] = self.mutate(offsprings[0])
            ch1 = Chromosome(self.funclist,self.constantpool,self.deep)
            ch2 = Chromosome(self.funclist,self.constantpool,self.deep)
            ch1.code = offsprings[0]
            ch2.code = offsprings[1]
            temppop.append(ch1)
            temppop.append(ch2)    
        self.chromosomes = temppop

    def getBest(self):
        for element in self.chromosomes:
            element.fitness = self.fitness(element.code)

        bestf = float("-inf")
        bestc = None
        for element in self.chromosomes:
            if(element.fitness > bestf):
                bestf = element.fitness
                bestc = element
        return bestc

if __name__ == "__main__":
    funclist = [
        PlusFunction("+", 2),
        MinusFunction("-", 2),
        ProductFunction("*", 2)
    ]
    varlist = {"x": 10, "y": 100}
    constantpool = [1,2,3,4,5,6,7,8,9,10]

    def abs (x):
        if x < 0:
            return (-x)
        else:
            return x

    def f (ch):
        result = postfixeval(ch, funclist, varlist)[0]
        return -abs(result - 75)   

    gp = GP(f, funclist,varlist,constantpool, popsize = 100,  deep = 3)
    gp.createRandomPopulation()
    for i in range(100):
        gp.iterate()

    best = gp.getBest().code
    print(str(best))
    print(postfixeval(best, funclist, varlist))