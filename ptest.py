import _trueskill
from pprint import pprint
from timeit import timeit

players = []
for i in range(4):
    players.append((25., 25./3., i+1))

def test():
    return _trueskill.adjust_players(players)

ITER = 1000000
print('{} iterations in {}s'.format(ITER, timeit(test, number=ITER)))

pprint(test())
