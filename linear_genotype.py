import random

class LinearGenotype():
    def __init__(self):
        self.fitness = None
        self.gene = None

    def random_initialization(self, length, x_bounds, y_bounds):
        # Simple one liner to generate random solutions in the bounds provided.
        self.gene = [(random.uniform(x_bounds[0],x_bounds[1]), random.uniform(y_bounds[0], y_bounds[1])) for i in range(length)]
        pass

    def recombine(self, mate, method, **kwargs):
        child = LinearGenotype()
        
        # TODO: Recombine genes of self with mate and assign to child's gene member variable
        assert method.casefold() in {'uniform', '1-point crossover', 'bonus'}
        if method.casefold() == 'uniform':
            # perform uniform recombination
            pass
        elif method.casefold() == '1-point crossover':
            child.gene = self.gene.copy()
            crosspoint = random.randint(0,len(self.gene.copy()))
            counter = 0
            for i in range(crosspoint):
                child.gene[counter] = self.gene.copy()[counter]
                counter = counter + 1
            for i in range(len(self.gene.copy())-crosspoint):
                child.gene[counter] = mate.gene[counter]
                counter = counter + 1
        elif method.casefold() == 'bonus':
            ''' 
            This is a red deliverable (i.e., bonus for anyone).

            Implement the bonus crossover operator as described in deliverable
            Red 1 of Assignment 1b.
            '''
            pass

        return child

    def mutate(self, x_bounds, y_bounds, bonus=None, **kwargs):
        copy = LinearGenotype()
        copy.gene = self.gene.copy()
        x = len(self.gene)-1
        if bonus is None:
            mutate0 = random.randint(0,x)
            mutategene1 = ()
            mutategene2 = ()
            mutategene1 = random.randint(x_bounds[0],x_bounds[1])
            mutategene2 = random.randint(y_bounds[0], y_bounds[1])
            mutatefullgene = (mutategene1,mutategene2)
            copy.gene[mutate0] = mutatefullgene

            
        else:
            ''' 
            This is a red deliverable (i.e., bonus for anyone).

            Implement the bonus crossover operator as described in deliverable
            Red 1 of Assignment 1b.
            '''
            pass

        return copy.gene

    @classmethod
    def initialization(cls, mu, *args, **kwargs):
        population = [cls() for _ in range(mu)]
        for i in range(len(population)):
            population[i].random_initialization(*args, **kwargs)
        return population