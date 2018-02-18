import random
com_games = 0
def bingonumbers(tixaiosari,x):
	ari8mos = True
	game = 0
	z = [0]*80
	while ari8mos:
		game = game+1
		y = random.sample(x,1)
		x.remove(y[0])
		for c in range(0,80):
			if y[0] in tixaiosari[c]:
				z[c] += 1
				if z[c] == 5:
					ari8mos=False
	return game
def player(x):
		ari8moi = []
		for c in range(100):
			ari8moi.append(random.sample(x,5))
		return ari8moi
for c in range(1000):
	x=range(1,81)
	paixtes = player(x)
	com_games += bingonumbers(paixtes,x)
mo=com_games/1000
print mo
