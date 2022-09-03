import sys
from FillZone import FillZone
from SearchMethods import BFS, DFS, IDDFS, Greedy, A

#python main.py -CantColors 6 -Size 4 - Heuristic 1 -SearchMethod 1 (-Limit 5)
if len(sys.argv) == 5:
    colors = int(sys.argv[1])
    size = int(sys.argv[2])
    heuristic = int(sys.argv[3])
    print(sys.argv[4])
    if sys.argv[4] == str(1):
        print("o")
        f = FillZone(size, colors, heuristic)
        sm = BFS(f)
        sm.run()
    elif sys.argv[4] == str(2):
        f = FillZone(size, colors, heuristic)
        sm = DFS(f)
        sm.run()
    elif sys.argv[4] == str(3):
        f = FillZone(size, colors, heuristic)
        sm = Greedy(f)
        sm.run()
    elif sys.argv[4] == str(4):
        f = FillZone(size, colors, heuristic)
        sm = A(f)
        sm.run()
    else:
        print("Wrong Configuration")
        print("Example: python3 Main.py 6 4 1 1")
# elif len(sys.argv) == 6:

# else:
    
# f = FillZone(4, 6, 1)
# g = IDDFS(f,4)
# g.run()