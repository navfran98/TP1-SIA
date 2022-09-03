###
##  While(!Condición de corte):
#       poblacion = seleccionar(poblacion)
#       crossover(poblacion)
##      mutacion(poblacion)
###

from random import random as rnd
from Color import Color
from SelectionAlgorithms import RouletteSelection, ProbabilisticTourney, Elite
from MutationAlgorithms import MultigenMutation
from CrossoverAlgorithms import UniformCrossover
#from Color import Colors

def end_condition(selected_population,objective):
    best_color, idx = Color.get_best_individual(selected_population,objective)
    return objective.compare_colors(best_color) > 0.2



K = 4 # numero de selección
N = 20 # numero de población

objective = Color(245,172,33) # Color objetivo

crossover = UniformCrossover(0.5)
#selection = ProbabilisticTourney(0.7,K,objective)
#selection = Elite(K,objective)
selection = RouletteSelection(K,objective)


#print(crossover.cross(Color(0,0,0),Color(255,255,255)))

population = []
#genero mi población inicial
for i in range(0,N):
    population.append(Color.generate_random_color())
    
mutation = MultigenMutation(population,0.01)



##Empieza loop hasta condicion de corte
print(objective)
selected_population = selection.select(population)
while(not end_condition(selected_population,objective)):
    
    population = crossover.get_new_crossed_population(selected_population)
    mutation.set_population(population)
    mutation.mutate_population()
    selected_population = selection.select(population)

print(selected_population)




