###
##  While(!Condición de corte):
#       poblacion = seleccionar(poblacion)
#       crossover(poblacion)
##      mutacion(poblacion)
###
import json
from random import random as rnd
from Color import Color
from SelectionAlgorithms import RouletteSelection, ProbabilisticTourney, Elite
from MutationAlgorithms import MultigenMutation
from CrossoverAlgorithms import UniformCrossover
#from Color import Colors

def end_condition(selected_population,objective):
    best_color, idx = Color.get_best_individual(selected_population,objective)
    return objective.compare_colors(best_color) > 0.2


population = []
crossover = UniformCrossover(0.5)
K = 0 # numero de selección
objective = -1 #Color objetivo


with open("..\\LadoB\\params.json") as file:
    data = json.load(file)
    K = data['K']
    objective = Color(data['objective']['red'], data['objective']['green'], data['objective']['blue'])
    for color in data['palette']:
        population.append(Color(color['red'], color['green'], color['blue']))
    selection_method = data['selection']['name']
    if selection_method == "Probabilistic Tourney":
        threshold = data['selection']['threshold']



#selection = ProbabilisticTourney(0.7,K,objective)
#selection = Elite(K,objective)
if selection_method == "Probabilistic Tourney":
    selection = ProbabilisticTourney(threshold,K,objective)
elif selection_method == "Elite":
    selection = Elite(K,objective)
elif selection_method == "Roulette":
    selection = RouletteSelection(K,objective)


#print(crossover.cross(Color(0,0,0),Color(255,255,255)))

# #genero mi población inicial
# for i in range(0,N):
#     population.append(Color.generate_random_color())
    
mutation = MultigenMutation(population,0.01)



##Empieza loop hasta condicion de corte
print(objective)
selected_population = selection.select(population)
while(not end_condition(selected_population,objective)):
    
    population = crossover.get_new_crossed_population(selected_population)
    mutation.set_population(population)
    mutation.mutate_population()
    selected_population = selection.select(population)

rta, idx = Color.get_best_individual(selected_population,objective)
print(rta)




