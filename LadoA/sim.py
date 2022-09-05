from FillZone import FillZone
from SearchMethods import DFS,BFS,IDDFS,A,Greedy

f = FillZone(5, 5, 3)
print(f.state.board)
sm1 = Greedy(f)
sm2 = A(f)
sm3 = BFS(f)
sm1.run()
sm2.run()
sm3.run()