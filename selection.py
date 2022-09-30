import random
import numpy as np

# Parent selection functions---------------------------------------------------
def uniform_random_selection(population, n, **kwargs):
    parents = [""]*n
    hold = (len(population))-1
    for i in range(n):
        x = random.randint(0,hold)
        parents[i] = population[x]
    return parents

def k_tournament_with_replacement(population, n, k, **kwargs):
    parents = list()
    for i in range(n):
        options = random.sample(population,k)
        holdfit = -10000000
        holdindividual = None
        for individual in options:
            if individual.fitness >= holdfit:
                holdfit = individual.fitness
                holdindividual = individual
        parents.append(holdindividual)
    return parents

def fitness_proportionate_selection(population, n, **kwargs):
    Minmaxlist = list()
    for individual in population:
        Minmaxlist.append(individual.fitness)
    fitchange = min(Minmaxlist)
    fitchange = 1.5*fitchange
    for i in range(len(Minmaxlist)):
        Minmaxlist[i] = Minmaxlist[i] - fitchange
    total = 0
    for i in range(len(Minmaxlist)):
        total = total + Minmaxlist[i]
        
    for i in range(len(Minmaxlist)):
        Minmaxlist[i] = Minmaxlist[i]/total
    holdindex = np.random.choice(len(population), n, True, Minmaxlist)
    parents = [""]*len(holdindex)
    for i in range(len(holdindex)):
        parents[i] = population[holdindex[i]]
    return parents
    


# Survival selection functions-------------------------------------------------
def truncation(population, n, **kwargs):
    survivors = list()
    population.sort(key=lambda x:x.fitness, reverse = True)
    survivors = population[:n]

    return survivors
#Note that once an individual is selected from the population it can't be selected again with this implementation 
def k_tournament_without_replacement(population, n, k, **kwargs):
    survivors = [""]*n
    for i in range(n):
        tourny = random.sample(population, k=k)
        holding =sorted(tourny, key = lambda x: x.fitness, reverse = True)[:1]
        survivors[i] = holding

    
    return survivors

# Yellow deliverable parent selection function---------------------------------
def stochastic_universal_sampling(population, n, **kwargs):
    # Recall that yellow deliverables are required for students in the grad
    # section but bonus for those in the undergrad section.
    # TODO: select n individuals using stochastic universal sampling
    pass
