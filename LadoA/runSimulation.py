from os import lseek
from FillZone import FillZone
from SearchMethods import DFS,BFS,IDDFS,A,Greedy

colors = 5
# N = [4,5,6,7]
N = [7]
Algorithms = [4]
heuristic = 2
for n in N: 
    for alg in Algorithms:
        with open("Files/" + str(n) + "_" + str(alg) + ".csv", "w") as file:
            file.write("time,v_nodes,f_nodes,path_len\n")
            for i in range(0, 4):
                f = FillZone(n, colors, heuristic)
                if alg == 1:
                    sm = BFS(f)
                elif alg == 2:
                    sm = DFS(f)
                elif alg == 3:
                    sm = Greedy(f)
                elif alg == 4:
                    sm = A(f)
                t, v, fr, pl = sm.run()
                file.write(str(t) + "," + str(v) + "," + str(fr) + "," + str(pl) + "\n") 
        file.close()