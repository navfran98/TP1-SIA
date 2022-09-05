import copy
from telnetlib import NOP
import time
import random
from FillZone import FillZone, Pair, Triple


class IDDFS:
    def __init__(self, fillzone, limit):
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [Triple(fillzone.get_state(), 0, 0)]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))
        # Camino Solucion
        self.path = []
        # Limite
        self.limit = limit
    
    def build_path(self, last):
        aux = last
        while aux.z != 0:
            self.path.insert(0, aux.x)
            aux = self.f[aux.z]
    
    def run(self):
        start_time = time.time()
        for idx, triple in enumerate(self.f):
            if triple.x not in self.v:
                if not triple.x.is_finished() and triple.y <= self.limit:
                    print("Profundidad --> " + str(triple.y))
                    print(triple.x.board)
                    self.v.append(triple.x)
                    # Expando
                    for i in self.available_colours:
                        if i != triple.x.current_colour:
                            newState = copy.deepcopy(triple.x)
                            newState.current_colour = i
                            newState.paint(i)
                            self.f.append(Triple(newState, triple.y+1, idx))
                else:
                    print(triple.x.board)
                    if triple.y >= self.limit:
                        print("--- PERDISTE ---")
                    else:
                        print("--- GANASTE ---")
                    self.build_path(triple)
                    t = (time.time() - start_time)
                    print("Tiempo: %s seconds" % t)
                    print(f"Nodos visitados: {len(self.v)}")
                    print(f"Nodos frontera: {len(self.f)}")
                    print(f"Camino Solucion: {self.path}")
                    print(f"Costo de la solucion: {len(self.path)}")
                    print("---------------")
                    return t, len(self.v),len(self.f), len(self.path)

class BFS:
    def __init__(self, fillzone):
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))

    def run(self):
        print("Running BFS...")
        start_time = time.time()
        for state in self.f:
            if state not in self.v:
                if not state.is_finished():
                    self.v.append(state)
                    # Expando
                    for i in self.available_colours:
                        if i != state.current_colour:
                            newState = copy.deepcopy(state)
                            newState.current_colour = i
                            newState.paint(i)
                            newState.path.append(state.current_colour)
                            self.f.append(newState)
                else:
                    state.path.append(state.current_colour)
                    print("--- GANASTE ---")
                    t = (time.time() - start_time)
                    print("Tiempo: %s seconds" % t)
                    print(f"Nodos visitados: {len(self.v)}")
                    print(f"Nodos frontera: {len(self.f)}")
                    print(f"Camino Solucion: {state.path}")
                    print(f"Costo de la solucion: {len(state.path)} Movimientos")
                    print("---------------")
                    return t, len(self.v),len(self.f), len(state.path)

class DFS:
    def __init__(self, fillzone):
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))
    
    def run(self):
        print("Running DFS...")
        start_time = time.time()
        for idx, state in enumerate(self.f):
            if not state.is_finished():
                if state not in self.v:
                    self.v.append(state)
                    # Expando
                    for i in self.available_colours:
                        if i != state.current_colour:
                            ns = copy.deepcopy(state)
                            ns.current_colour = i
                            ns.paint(i)
                            ns.path.append(state.current_colour)
                            self.f.insert(idx+1,ns)
                else:
                    self.f.pop(idx)
            else:
                state.path.append(state.current_colour)
                print("--- GANASTE ---")
                t = (time.time() - start_time)
                print("Tiempo: %s seconds" % t)
                print(f"Nodos visitados: {len(self.v)}")
                print(f"Nodos frontera: {len(self.f)}")
                print(f"Camino Solucion: {state.path}")
                print(f"Costo de la solucion: {len(state.path)} Movimientos")
                print("---------------")
                return t, len(self.v),len(self.f), len(state.path)

class Greedy:
    def __init__(self, fillzone):
        self.fillzone = fillzone
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))

    def run(self):
        print("Running Greedy...")
        start_time = time.time()
        for state in self.f:
            if state not in self.v:
                if not state.is_finished():
                    self.v.append(state)
                    # Expando teniendo en cuenta la heuristica
                    h_min = -1
                    next_state = -1
                    for i in self.available_colours:
                        if i != state.current_colour:
                            newState = copy.deepcopy(state)
                            newState.current_colour = i
                            newState.paint(i)
                            newState.path.append(state.current_colour)
                            aux = self.fillzone.run_heuristic(newState)
                            if aux <= h_min or h_min == -1:
                                if newState not in self.v:
                                    h_min = aux
                                    next_state = newState
                    self.f.append(next_state)
                else:
                    state.path.append(state.current_colour)
                    print(state.board)
                    print("--- GANASTE ---")
                    t = (time.time() - start_time)
                    print("Tiempo: %s seconds" % t)
                    print(f"Nodos visitados: {len(self.v)}")
                    print(f"Nodos frontera: {len(self.f)}")
                    print(f"Camino Solucion: {state.path}")
                    print(f"Costo de la solucion: {len(state.path)} Movimientos")
                    print("---------------")
                    return t, len(self.v),len(self.f), len(state.path)

class A:
    def __init__(self, fillzone):
        self.fillzone = fillzone
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))
    
    def get_min_from_f(self):
        min_state = self.f[0]
        for state in self.f:
            if state not in self.v:
                min_state = state
                break
        for state in self.f:
            # if state.cost_for_A < min_state.cost_for_A:
            diff = (state.moves_made + state.heuristic) - (min_state.moves_made + min_state.heuristic)
            if diff < 0 or (diff == 0 and state.heuristic < min_state.heuristic):
                if state not in self.v:
                    min_state = state
        min_state = copy.deepcopy(min_state)
        return min_state 

    def run(self):
        print("Running A*...")
        start_time = time.time()
        state = self.f[0]
        # Estoy verificando dos veces is_finished pero porq no lo pense todavia
        while True:
            # Expando y calculo su costo + heuristica y lo agrego a la frontera
            #if state not in self.v:
            if not state.is_finished():
                self.v.append(state)
                for i in self.available_colours:
                    if i != state.current_colour:
                        newState = copy.deepcopy(state)
                        newState.current_colour = i
                        newState.paint(i)
                        newState.moves_made += 1
                        newState.path.append(state.current_colour)
                        newState.heuristic = self.fillzone.run_heuristic(newState)
                        if newState not in self.v:
                            self.f.append(newState)
            else:
                state.path.append(state.current_colour)
                print("--- GANASTE ---")
                t = (time.time() - start_time)
                print("Tiempo: %s seconds" % t)
                print(f"Nodos visitados: {len(self.v)}")
                print(f"Nodos frontera: {len(self.f)}")
                print(f"Camino Solucion: {state.path}")
                print(f"Costo de la solucion: {len(state.path)} Movimientos")
                print("---------------")
                return t, len(self.v),len(self.f), len(state.path)
            state = self.get_min_from_f()
            # state.path.append(state)

