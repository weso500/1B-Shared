from bridge_fitness import *

# 1b TODO: evaluate the population and assign fitness and bridge as described in the Assignment 1b notebook
def basic_population_evaluation(population, **fitness_kwargs):
    it = 0
    sav = len(population)
    individual = [""]*sav
    for i in range(sav):
        individual[it] = population[it].fitness, population[it].bridge = basic_simulation(population[it].gene, **fitness_kwargs)
        it = it + 1

    pass

# 1c TODO: evaluate the population and assign fitness, raw_fitness, and bridges as described in the constraint satisfaction segment of Assignment 1c
def constraint_satisfaction_population_evaluation(population, penalty_coefficient, yellow = None, **fitness_kwargs):
    if yellow == None:
        # GREEN deliverable logic goes here
        pass
    else:
        # YELLOW deliverable logic goes here
        pass

# 1c TODO: evaluate the population and assign objectives and bridges as described in the multi-objective segment of Assignment 1c
def multi_objective_population_evaluation(population, yellow = None, red = None, **fitness_kwargs):
    pass