from FillZone import FillZone
from SearchMethods import DFS,BFS,IDDFS,A,Greedy

f = FillZone(5, 5, 3)
print(f.get_state().board)
sm1 = BFS(f)
sm2 = A(f)
sm1.run()
sm2.run()