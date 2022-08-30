import copy
from FillZone import FillZone

class BFS:
    def __init__(self, fillzone):
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))
    
    def run(self):
        for state in self.f:
            if state not in self.v:
                if not state.is_finished():
                    print("Area pintada con ---> " + str(state.current_colour))
                    print(state.board)
                    self.v.append(state)
                    # Expando
                    for i in self.available_colours:
                        if i != state.current_colour:
                            newState = copy.deepcopy(state)
                            newState.current_colour = i
                            newState.paint(i)
                            self.f.append(newState)
                    self.f.pop(0)
                else:
                    print(state.board)
                    print("FIN")
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
                
    
    def run(self):
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
                else:
                    self.f.pop(idx)
            else:
                print(state.board)
                print("GANASTE")
                return

class Greedy:
    def __init__(self, fillzone):
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))

    def run(self,heuristic):
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
                            aux = heuristic(i)
                            print(str(i) + " --> " + str(aux))
                            if aux <= h_min:
                                h_min = aux
                                next_state = newState
                    print("El mejor es --> " + str(next_state))
                    self.f.append(next_state)
                else:
                    print(state.board)
                    print("FIN")
                    return
            else:
                print("PASE POR UN ESTADO REPETIDO/VISITADO")

class A:
    def __init__(self, fillzone):
        # Nodos visitados
        self.v = []
        # Nodos frontera
        self.f = [fillzone.get_state()]
        # Array con la cantidad de colores disponible
        self.available_colours = list(range(0, fillzone.state.colours))
    
    def get_min_from_f(self):
        min_state = self.f[0]
        for state in self.f:
            # if state.cost_for_A < min_state.cost_for_A:
            diff = (state.moves_made + state.heuristic) - (min_state.moves_made + min_state.heuristic)
            if diff < 0 or (diff == 0 and state.heuristic < min_state.heuristic):
                min_state = copy.deepcopy(state)
        return min_state 

    def run(self):
        state = self.f[0]
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
                            newState.heuristic = newState.heuristic1(i)
                            # newState.cost_for_A = newState.moves_made + newState.heuristic1(i)
                            self.f.append(newState)
                    self.f.pop(self.f.index(state))
                else:
                    print(state.board)
                    print("FIN")
                    return
            else:
                print("PASE POR UN ESTADO REPETIDO/VISITADO")
            state = self.get_min_from_f()


f = FillZone(5, 6)
g = A(f)
g.run()

#t = [1,2,3]
#t.insert(1, 42)
#print(t)