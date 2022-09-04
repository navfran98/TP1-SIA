# import sys
# from FillZone import FillZone
# from SearchMethods import BFS, DFS, IDDFS, Greedy, A

# #python main.py -CantColors 6 -Size 4 - Heuristic 1 -SearchMethod 1 (-Limit 5)
# if len(sys.argv) == 5 or len(sys.argv) == 6:
#     colors = int(sys.argv[1])
#     if colors < 4 or colors > 8:
#         print("Wrong number of colors. Must be between 4 and 8.")
#         exit()
#     size = int(sys.argv[2])
#     if size < 3 or size > 10:
#         print("Wrong size of the board. Must be between a 3x3 and 10x10.")
#         exit()
#     heuristic = int(sys.argv[3])
#     if heuristic < 1 or heuristic > 2:
#         print("Wrong heuristic selected. Available options are 1 or 2.")
#         exit()
#     if sys.argv[4] == str(1):
#         print("o")
#         f = FillZone(size, colors, heuristic)
#         sm = BFS(f)
#         sm.run()
#     elif sys.argv[4] == str(2):
#         f = FillZone(size, colors, heuristic)
#         sm = DFS(f)
#         sm.run()
#     elif sys.argv[4] == str(3):
#         f = FillZone(size, colors, heuristic)
#         sm = Greedy(f)
#         sm.run()
#     elif sys.argv[4] == str(4):
#         f = FillZone(size, colors, heuristic)
#         sm = A(f)
#         sm.run()
#     elif sys.argv[4] == str(5):
#         if int(sys.argv[5]) > 0:
#             f = FillZone(size, colors, heuristic)
#             sm = IDDFS(f, int(sys.argv[5]))
#             sm.run()
#         else:
#             print("Wrong limit value. Must be a positive number.")
#             exit()
#     else:
#         print("Wrong search method selected. Must be between 1 and 5.")
#         exit()
# else:
#     print("Wrong number of arguments.")
#     print("Example: python3 Main.py 6 4 1 1")
#     exit()

import argparse
from FillZone import FillZone
from SearchMethods import BFS, DFS, IDDFS, Greedy, A

parser = argparse.ArgumentParser(description='Run the Fillzone Game.')
req_args = parser.add_argument_group('required arguments')
req_args.add_argument("-c", "--colors", help="Number of colors that the game will have.", required=True)
req_args.add_argument("-s", "--size", help="Size of the game board (NxN).", required=True)
req_args.add_argument("-he", "--heuristic", help="Heuristic selected (Values -> 1 or 2).", required=True)
req_args.add_argument("-sm", "--searchMethod", help="Search Method selected (Values -> 1 - BFS | 2 - DFS | 3 - Greedy | 4 - A* | 5 - IDDFS).", required=True)
req_args.add_argument("-l", "--limit", help="Limit for IDDFS.", required=True)
args = parser.parse_args()

#python main.py -CantColors 6 -Size 4 - Heuristic 1 -SearchMethod 1 (-Limit 5)
colors = int(args.colors)
size = int(args.size)
heuristic = int(args.heuristic)
search_method = args.searchMethod
if colors < 4 or colors > 8:
    print("Wrong number of colors. Must be between 4 and 8.")
    exit()
if size < 3 or size > 10:
    print("Wrong size of the board. Must be between a 3x3 and 10x10.")
    exit()
if heuristic < 1 or heuristic > 2:
    print("Wrong heuristic selected. Available options are 1 or 2.")
    exit()
if search_method == str(1):
    print("o")
    f = FillZone(size, colors, heuristic)
    sm = BFS(f)
    sm.run()
elif search_method == str(2):
    f = FillZone(size, colors, heuristic)
    sm = DFS(f)
    sm.run()
elif search_method == str(3):
    f = FillZone(size, colors, heuristic)
    sm = Greedy(f)
    sm.run()
elif search_method == str(4):
    f = FillZone(size, colors, heuristic)
    sm = A(f)
    sm.run()
elif search_method == str(5):
    if int(args.limit) > 0:
        f = FillZone(size, colors, heuristic)
        sm = IDDFS(f, int(args.limit))
        sm.run()
    else:
        print("Wrong limit value. Must be a positive number.")
        exit()
else:
    print("Wrong search method selected. Must be between 1 and 5.")
    exit()
# else:
#     print("Wrong number of arguments.")
#     print("Example: python3 Main.py 6 4 1 1")
#     exit()