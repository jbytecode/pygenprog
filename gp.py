from interpreter import *
from interpreter import postfixeval

import copy

import random
import math

class Chromosome:
    code = []
    functionlist = [] 
    constantpool = []
    varlist = []
    paramlist = []
    deep = 0
    fitness = float("-inf")

    def __init__(self, functionlist: list, constantpool: list, varlist: list, deep: int):
        self.functionlist = functionlist
        self.deep = deep
        self.constantpool = constantpool
        self.code = []
        self.paramlist = []
        self.paramlist.extend(constantpool)
        self.paramlist.extend(varlist)
        self.varlist = varlist
        for i in range(deep):
            gpfunc = random.choice(functionlist)
            numparams = gpfunc.numparams
            if i == 0:
                k = numparams
            else:
                k = numparams - 1
            cons = random.choices(self.paramlist, k = k)
            self.code.extend(cons)
            self.code.append(gpfunc.name)

    def __str__(self):
        return(str(self.code))

    def cut(self, maxdeep: int):
        count = findFunctionCount(self.code, self.functionlist)
        if count > maxdeep:
            while True:
                if findFunctionCount(self.code, self.functionlist) <= maxdeep:
                    if findFunction(self.code[len(self.code) - 1], self.functionlist) != None:
                        break
                self.code.pop()
    
    def eval(self):
        result = postfixeval(self.code, self.functionlist, self.varlist)
        return result

    
class GP:
    popsize = 100
    fitness = None
    funclist = None
    varlist = None
    constantpool = None
    chromosomes = None
    deep = 3
    maxdeep = 5

    def __init__(self, fitness, funclist, varlist, constantpool, popsize = 100, deep = 3, maxdeep = 5):
        self.popsize = popsize
        self.fitness = fitness
        self.varlist = varlist
        self.constantpool = constantpool
        self.chromosomes = []
        self.funclist = funclist
        self.deep = deep
        self.maxdeep = maxdeep
        
    
    def createRandomPopulation(self):
        self.chromosomes = []
        for _ in range(self.popsize):
            ch = Chromosome(self.funclist, self.constantpool, self.varlist, self.deep)
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
            luckynum = random.choice(self.constantpool)
            offspring[random_index] = luckynum
        else:
            gpfunc = findFunction(element, self.funclist)
            if gpfunc != None:
                oldfunc = gpfunc
                while True:
                    luckyfun = random.choice(self.funclist)
                    if luckyfun.numparams == oldfunc.numparams:
                        break
                offspring[random_index] = luckyfun.name
            else:
                luckyvar = random.choice(list(self.varlist))
                offspring[random_index] = luckyvar
        return offspring

    def __str__(self):
        return(str(self.chromosomes))

    def iterate(self):
        for i in range(len(self.chromosomes)):
            f = self.fitness(self.chromosomes[i].code)
            self.chromosomes[i].fitness = f
        temppop = []
        bestsolution = self.getBest()
        temppop.append(copy.copy(bestsolution))
        temppop.append(copy.copy(bestsolution))
        for i in range(int( (len(self.chromosomes) - 2) / 2)):    
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
            ch1 = Chromosome(self.funclist, self.constantpool, self.varlist, self.deep)
            ch2 = Chromosome(self.funclist, self.constantpool, self.varlist, self.deep)
            ch1.code = offsprings[0]
            ch2.code = offsprings[1]
            ch1.cut(self.maxdeep)
            ch2.cut(self.maxdeep)
            temppop.append(ch1)
            temppop.append(ch2)    
        self.chromosomes = temppop

    def calculateFitness(self):
         for element in self.chromosomes:
            element.fitness = self.fitness(element.code)

    def getBest(self):
        bestf = float("-inf")
        bestc = None
        for element in self.chromosomes:
            if(element.fitness > bestf):
                bestf = element.fitness
                bestc = element
        return bestc

    def report(self):
        print("--- Results of GP ---")
        self.calculateFitness()
        best = self.getBest()
        print("Code: " + str(best.code))
        print("Fitness: " + str(best.fitness))
        varlist = copy.copy(self.varlist)
        for key in varlist:
            varlist[key] = str(key)
        print("Infix: " + str(postfix2infix(best.code, self.funclist, varlist)))

    def interactive(self):
        while True:
            cmd = input("GP: ")
            words = cmd.split(" ")
            print(words)
            if(len(words) == 1):
                word = words[0]
                if word == "iterate":
                    self.iterate()
                    self.report()
                elif word == "exit":
                    break
                elif word == "randomize":
                    self.createRandomPopulation()
                    self.calculateFitness()
                    self.report()
            elif len(words) == 2:
                if (words[0] == "iterate" and words[1] != ""):
                    for _ in range(int(words[1])):
                        self.iterate()
                    self.report()
