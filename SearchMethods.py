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

    def run(self):
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
                            aux = newState.heuristic1(i)
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
    
    def run(self):
        state = self.f[0]
        while not state.is_finished():


f = FillZone(3, 6)
g = Greedy(f)
g.run()

#t = [1,2,3]
#t.insert(1, 42)
#print(t)