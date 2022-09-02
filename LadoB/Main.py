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

K = 5 # numero de selección
N = 20 # numero de población

objective = Color(245,172,33) # Color objetivo
print(objective)

crossover = UniformCrossover(0.5)
selection = ProbabilisticTourney(0.7,K,objective)


palette = []
#genero mi población inicial
for i in range(0,N):
    palette.append(Color.generate_random_color())
    
population = palette

mutation = MultigenMutation(population,0.01)


##Empieza loop hasta condicion de corte
print(objective)

for i in range(0, 100):
    selected_population = selection.select(population)
    population = crossover.get_new_crossed_population(selected_population)
    #mutation.set_population(population)
    #mutation.mutate_population()

selected_population = selection.select(population)
#population = crossover.get_new_crossed_population(selected_population)
print(selected_population)




