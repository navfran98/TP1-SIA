from FillZone import FillZone
from SearchMethods import BFS, DFS, IDDFS, Greedy, A

f = FillZone(4, 6, 1)
g = IDDFS(f,4)
g.run()