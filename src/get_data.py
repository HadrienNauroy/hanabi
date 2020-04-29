""" Algorithm to collect statistic from an ia and to sum it up in a bar histogram"""

import time
import hanabi
import matplotlib.pyplot as plt

start_time = time.time()
n=10
nb_players=5
results=26*[0]


for k in range(n):
	game=hanabi.Game(nb_players)
	ai=hanabi.ai.Strat1_ai(game)
	game.ai=ai
	game.run()
	res=game.score
	results[res]+=1


print("Temps d execution pour %d parties : %s secondes " %(n,round(time.time() - start_time,2)))
target=[k for k in range(26)]
plt.clf()
plt.bar(target,results)
plt.show()

