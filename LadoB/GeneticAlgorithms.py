
###
##  While(!Condición de corte):
#       poblacion = seleccionar(poblacion)
#       crossover(poblacion)
##      mutacion(poblacion)
###

from random import random as rnd
from Color import Color
from  SelectionAlgorithms import RouletteSelection, ProbabilisticTourney, Elite
#from Color import Colors




objective = Color(245,172,33)
palette = []
K = 4 # numero de selección
N = 7 # numero de población
#genero mi población inicial
for i in range(0,N):
    palette.append(Color.generate_random_color())
print(palette)
selection = RouletteSelection(K,objective).select(palette)
print(selection)




