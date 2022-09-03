import copy
import time
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
                    # for i in self.path:
                    #     print(str(i.current_colour) + " ")
                    print("Tiempo: %s seconds " % (time.time() - start_time))
                    print(f"Nodos visitados: {len(self.v)}")
                    print(f"Camino Solucion: {self.path}")
                    print("---------------")
                    return
            else:
                print("PASE POR UN ESTADO REPETIDO/VISITADO")

class BFS:
    def __init__(self, fillzone):
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [Pair(fillzone.get_state(), 0)]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))
        # Camino solucion
        self.path = []
    
    def build_path(self, last):
        aux = last
        while aux.y != 0:
            self.path.insert(0, aux.x)
            aux = self.f[aux.y]
    
    def run(self):
        start_time = time.time()
        for idx, pair in enumerate(self.f):
            if pair.x not in self.v:
                if not pair.x.is_finished():
                    print("Area pintada con ---> " + str(pair.x.current_colour))
                    print(pair.x.board)
                    self.v.append(pair.x)
                    # Expando
                    for i in self.available_colours:
                        if i != pair.x.current_colour:
                            newState = copy.deepcopy(pair.x)
                            newState.current_colour = i
                            newState.paint(i)
                            self.f.append(Pair(newState, idx))
                else:
                    print(pair.x.board)
                    self.build_path(pair)
                    for i in self.path:
                        print(str(i.current_colour) + " ")
                    print("--- GANASTE ---")
                    print("Tiempo: %s seconds " % (time.time() - start_time))
                    print(f"Nodos visitados: {len(self.v)}")
                    print(f"Camino Solucion: {self.path}")
                    print("---------------")
                    return
            else:
                print("PASE POR UN ESTADO REPETIDO/VISITADO")

class DFS:
    def __init__(self, fillzone):
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))
        # Camino solucion
        self.path = []
    
    def run(self):
        start_time = time.time()
        for idx, state in enumerate(self.f):
            if not state.is_finished():
                if state not in self.v:
                    print(state.board)
                    self.v.append(state)
                    # Expando
                    for i in self.available_colours:
                        if i != state.current_colour:
                            ns = copy.deepcopy(state)
                            ns.current_colour = i
                            ns.paint(i)
                            self.f.insert(idx+1,ns)
                    self.path.append(state)
                else:
                    self.f.pop(idx)
            else:
                self.path.append(state)
                print(state.board)
                print("--- GANASTE ---")
                print("Tiempo: %s seconds " % (time.time() - start_time))
                print(f"Nodos visitados: {len(self.v)}")
                print(f"Camino Solucion: {self.path}")
                print("---------------")
                return

class Greedy:
    def __init__(self, fillzone):
        self.fillzone = fillzone
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))
        # Camino solucion
        self.path = []

    def run(self):
        start_time = time.time()
        for state in self.f:
            if state not in self.v:
                if not state.is_finished():
                    print(state.board)
                    self.v.append(state)
                    # Expando teniendo en cuenta la heuristica
                    h_min = state.size * state.size
                    next_state = -1
                    for i in self.available_colours:
                        if i != state.current_colour:
                            newState = copy.deepcopy(state)
                            newState.current_colour = i
                            newState.paint(i)
                            aux = self.fillzone.run_heuristic(newState, i)
                            # print(str(i) + " --> " + str(aux))
                            if aux <= h_min:
                                h_min = aux
                                next_state = newState
                    # print("El mejor es --> " + str(next_state))
                    self.f.append(next_state)
                    self.path.append(state)
                else:
                    self.path.append(state)
                    print(state.board)
                    print("--- GANASTE ---")
                    print("Tiempo: %s seconds " % (time.time() - start_time))
                    print(f"Nodos visitados: {len(self.v)}")
                    print(f"Camino Solucion: {self.path}")
                    print("---------------")
                    return
            else:
                print("PASE POR UN ESTADO REPETIDO/VISITADO")

class A:
    def __init__(self, fillzone):
        self.fillzone = fillzone
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))
        # Camino solucion
        self.path = []
    
    def get_min_from_f(self):
        min_state = self.f[0]
        for state in self.f:
            # if state.cost_for_A < min_state.cost_for_A:
            diff = (state.moves_made + state.heuristic) - (min_state.moves_made + min_state.heuristic)
            if diff < 0 or (diff == 0 and state.heuristic < min_state.heuristic):
                min_state = copy.deepcopy(state)
        return min_state 

    def run(self):
        start_time = time.time()
        state = self.f[0]
        self.path.append(state)
        # Estoy verificando dos veces is_finished pero porq no lo pense todavia
        while True:
            if state not in self.v:
            # Expando y calculo su costo + heuristica y lo agrego a la frontera
                if not state.is_finished():
                    print(state.board)
                    print(state.moves_made)
                    self.v.append(state)
                    next_state = -1
                    for i in self.available_colours:
                        if i != state.current_colour:
                            newState = copy.deepcopy(state)
                            newState.current_colour = i
                            newState.paint(i)
                            newState.moves_made += 1
                            newState.heuristic = self.fillzone.run_heuristic(newState, i)
                            # newState.cost_for_A = newState.moves_made + newState.heuristic1(i)
                            self.f.append(newState)
                    self.f.pop(self.f.index(state))
                else:
                    print(state.board)
                    print("--- GANASTE ---")
                    print("Tiempo: %s seconds" % (time.time() - start_time))
                    print(f"Nodos visitados: {len(self.v)}")
                    print(f"Camino Solucion: {self.path}")
                    print("---------------")
                    return
            else:
                print("PASE POR UN ESTADO REPETIDO/VISITADO")
            state = self.get_min_from_f()
            self.path.append(state)