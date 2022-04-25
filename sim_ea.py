import ea
import numpy as np

popsize = 100
genesize = 5
recombProb = 0.5
mutatProb = 0.1
generations = 100
tournaments = generations * popsize

def fitnessFunction(genotype):
    return np.sum(genotype)

ga = ea.Microbial(fitnessFunction, popsize, genesize, recombProb, mutatProb)

ga.run(tournaments)

ga.showFitness()
