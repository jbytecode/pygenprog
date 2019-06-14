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

    def __repr__(self):
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
        newch1 = code1[0:(op1_ind + 1)] + code2[(op2_ind + 1): len(code2)]
        newch2 = code2[0:(op2_ind + 1)] + code1[(op1_ind + 1): len(code1)]
        return [newch1, newch2]

    def mutateSingleNumberOrLiteral(self, offspring, index):
        element = offspring[index]
        t = type(element).__name__
        if(t == "int" or t == "float"):
            if random.uniform(0, 1) < 0.5:
                luckynum = random.choice(self.constantpool)
                offspring[index] = luckynum
            else:
                luckyvar = random.choice(list(self.varlist))
                offspring[index] = luckyvar
        
    def mutate(self, code: list):
        offspring = code.copy()
        random_index = random.choice(range(len(offspring)))
        element = offspring[random_index]
        t = type(element).__name__
        if(t == "int" or t == "float"):
            self.mutateSingleNumberOrLiteral(offspring, random_index)
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
                self.mutateSingleNumberOrLiteral(offspring, random_index)
        return offspring

    def __str__(self):
        return(str(self.chromosomes))

    def select(self, ch1, ch2):
        if ch1.fitness > ch2.fitness:
            return ch1
        elif ch1.fitness == ch2.fitness:
            if len(ch1.code) < len(ch2.code):
                return ch1
            else:
                return ch2
        else:
            return ch2

    def iterate(self):
        for i in range(len(self.chromosomes)):
            f = self.fitness(self.chromosomes[i].code)
            self.chromosomes[i].fitness = f
        temppop = []
        self.sortPopulation()
        temppop.append(copy.copy(self.chromosomes[0]))
        temppop.append(copy.copy(self.chromosomes[1]))
        for i in range(int( (len(self.chromosomes) - 2) / 2)):    
            indices1 = random.choice(range(len(self.chromosomes)))
            indices2 = random.choice(range(len(self.chromosomes)))
            parent1 = self.select(self.chromosomes[indices1], self.chromosomes[indices2])
            indices1 = random.choice(range(len(self.chromosomes)))
            indices2 = random.choice(range(len(self.chromosomes)))
            parent2 = self.select(self.chromosomes[indices1], self.chromosomes[indices2])
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
    
    def sortByFitness(self, ch):
        return ch.fitness

    def sortPopulation(self):
        self.chromosomes.sort(key = self.sortByFitness, reverse = True)

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

    def showPopulation(self):
        i = 1
        for element in self.chromosomes:
            print(str(i) + ": " + str(element.fitness) + ": " + str(element.code))
            i = i + 1

    def help(self):
        print("GP interative:")
        print("randomize")
        print("iterate")
        print("exit")
        print("iterate n")
        print("maxdeep n")
        print("deep n")
        print("popsize n")
        print("emptyconstantpool")
        print("constantpool")
        print("constantpool num1 num2 num3 ...")
        print("list")
    def interactive(self):
        while True:
            cmd = input("GP: ")
            words = cmd.split(" ")
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
                elif word == "constantpool":
                    print(str(self.constantpool))
                elif word == "emptyconstantpool":
                    self.constantpool.clear()
                elif word == "list":
                    self.sortPopulation()
                    self.showPopulation()
                elif word == "help":
                    self.help()
            elif len(words) >= 2:
                if (words[0] == "iterate" and words[1] != ""):
                    for _ in range(int(words[1])):
                        self.iterate()
                    self.report()
                if(words[0] == "maxdeep" and words[1] != ""):
                    self.maxdeep = int(words[1])
                    print("maxdeep is set to " + str(self.maxdeep))
                if(words[0] == "deep" and words[1] != ""):
                    self.deep = int(words[1])
                    print("deep is set to " + str(self.deep))
                if(words[0] == "popsize" and words[1] != ""):
                    self.popsize = int(words[1])
                    self.createRandomPopulation()
                    print("popsize is set to " + str(self.popsize) + " and randomized population")
                if(words[0] == "constantpool"):
                    tmpList = []
                    for tmpI in range(1, len(words)):
                        tmpList.append(float(words[tmpI]))
                    self.constantpool.clear()
                    self.constantpool.extend(tmpList)
                    print("Constant pool is now " + str(self.constantpool))
                
