import numpy as np
 
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def __hash__(self):
        return hash(str(self.x) + str(self.y))

    def __str__(self):
        return "(" + str(self.x) + " " + str(self.y) + ")"
    
    def __repr__(self):
        return "(" + str(self.x) + " " + str(self.y) + ")"

class Triple:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __str__(self):
        return "(" + str(self.x) + " " + str(self.y) + " " + str(self.z) + ")"
    
    def __repr__(self):
        return "(" + str(self.x) + " " + str(self.y) + " " + str(self.z) + ")"

class State:
    def __init__(self, size, colours):
        self.board = np.random.randint(colours, size=(size, size))
        self.colours = colours
        # Conjunto de pairs, cordenadas de las casillas
        # que ya pinte
        self.painted = []
        # Ya dejamos agregada esta casilla que simpre va
        self.painted.append(Pair(0,0))
        self.size = size
        self.current_colour = self.board[0][0]
        # Calculamos el area inicial que esta pintada
        self.paint(self.current_colour)
        # Deberiamos agregar cantidad de mov hechos para llegar a este estado
        self.moves_made = 0
        self.heuristic = 0
        self.path = []
    
    def __eq__(self, other):
        return set(self.painted) == set(other.painted) and self.current_colour == other.current_colour
    
    def __str__(self):
        return str(self.current_colour)
    
    def __repr__(self):
        return str(self.current_colour)

    # Cantidad de casillas que me faltan pintar
    def add_to_paint(self,new_colour, aux: list[Pair]):
        for coord in aux:
            if ((coord.x+1) < self.size):
                if Pair(coord.x+1, coord.y) not in aux and self.board[coord.x+1][coord.y] == new_colour:
                    aux.append(Pair(coord.x+1, coord.y))
            # Izquierda
            if ((coord.x-1) > 0):
                if Pair(coord.x-1, coord.y) not in aux and self.board[coord.x-1][coord.y] == new_colour:
                    aux.append(Pair(coord.x-1, coord.y))
            # Abajo
            if ((coord.y+1) < self.size):
                if Pair(coord.x, coord.y+1) not in aux and self.board[coord.x][coord.y+1] == new_colour:
                    aux.append(Pair(coord.x, coord.y+1))
            # Arriba
            if ((coord.y-1) > 0):
                if Pair(coord.x, coord.y-1) not in aux and self.board[coord.x][coord.y-1] == new_colour:
                    aux.append(Pair(coord.x, coord.y-1))
        return aux
            
    
    def heuristic1(self, new_colour):
        aux = []
        for s in self.painted:
            aux.append(s)
        self.add_to_paint(new_colour,aux)
        return self.size*self.size - len(aux)
        
    def heuristic2(self, new_colour):
        aux = []
        for s in self.painted:
            aux.append(s)
        self.add_to_paint(new_colour,aux)
        colours_left_to_paint = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] not in colours_left_to_paint and Pair(i,j) not in aux:
                    colours_left_to_paint.append(self.board[i][j])
        print("Colours left to paint:" + str(len(colours_left_to_paint)))
        return len(colours_left_to_paint)
        
    
                    
                
        
        

    def paint(self, new_colour):
        for coord in self.painted:
            self.board[coord.x][coord.y] = new_colour
            # Derecha
            if ((coord.x+1) < self.size):
                if Pair(coord.x+1, coord.y) not in self.painted and self.board[coord.x+1][coord.y] == new_colour:
                    self.painted.append(Pair(coord.x+1, coord.y))
            # Izquierda
            if ((coord.x-1) > 0):
                if Pair(coord.x-1, coord.y) not in self.painted and self.board[coord.x-1][coord.y] == new_colour:
                    self.painted.append(Pair(coord.x-1, coord.y))
            # Abajo
            if ((coord.y+1) < self.size):
                if Pair(coord.x, coord.y+1) not in self.painted and self.board[coord.x][coord.y+1] == new_colour:
                    self.painted.append(Pair(coord.x, coord.y+1))
            # Arriba
            if ((coord.y-1) > 0):
                if Pair(coord.x, coord.y-1) not in self.painted and self.board[coord.x][coord.y-1] == new_colour:
                    self.painted.append(Pair(coord.x, coord.y-1))             
    
    def is_finished(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if(self.board[i][j] != self.board[0][0]):
                    return False
        return True
        
    def remaining_blocks(self):
        return (self.size*self.size) - self.painted
        
class FillZone:
    def __init__(self, size, colours, heuristic):
        self.state = State(size, colours)
        self.selected_heuristic = heuristic

    def get_state(self):
        return self.state

    def run_heuristic(self, state, new_colour):
        if self.selected_heuristic == 1:
            return self.heuristic1(state, new_colour)
        elif self.selected_heuristic == 2:
            return self.heuristic2(state, new_colour)
        
    def heuristic1(self, state, new_colour):
        aux = []
        for s in state.painted:
            aux.append(s)
        for coord in aux:
            # Derecha
            if ((coord.x+1) < state.size):
                if Pair(coord.x+1, coord.y) not in aux and state.board[coord.x+1][coord.y] == new_colour:
                    aux.append(Pair(coord.x+1, coord.y))
            # Izquierda
            if ((coord.x-1) > 0):
                if Pair(coord.x-1, coord.y) not in aux and state.board[coord.x-1][coord.y] == new_colour:
                    aux.append(Pair(coord.x-1, coord.y))
            # Abajo
            if ((coord.y+1) < state.size):
                if Pair(coord.x, coord.y+1) not in aux and state.board[coord.x][coord.y+1] == new_colour:
                    aux.append(Pair(coord.x, coord.y+1))
            # Arriba
            if ((coord.y-1) > 0):
                if Pair(coord.x, coord.y-1) not in aux and state.board[coord.x][coord.y-1] == new_colour:
                    aux.append(Pair(coord.x, coord.y-1))
            return state.size*state.size - len(aux)
        
    def heuristic2(self,state, new_colour):
        aux = []
        for s in state.painted:
            aux.append(s)
        state.add_to_paint(new_colour,aux)
        colours_left_to_paint = []
        for i in range(len(state.board)):
            for j in range(len(state.board)):
                if state.board[i][j] not in colours_left_to_paint and Pair(i,j) not in aux:
                    colours_left_to_paint.append(state.board[i][j])
        print("Colours left to paint:" + str(len(colours_left_to_paint)))
        return len(colours_left_to_paint)