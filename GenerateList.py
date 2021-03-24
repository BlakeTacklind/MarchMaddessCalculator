#!/usr/bin/env python3


from Tournament import Tournament
from LoadBracket import LoadBracket
from GenSteps import GeneratedBracket, NUM_IDS, BITS


class PlayerHandler(object):
	ALL = []
	"""docstring for PlayerHandler"""
	def __init__(self, name, bracketPath, tournament):
		super(PlayerHandler, self).__init__()
		self.name = name
		self.bracketPath = bracketPath
		self.bracket = LoadBracket(bracketPath, tournament)
		PlayerHandler.ALL.append(self)
		self.winProbablity = 0.0
		self.tieProbablity = 0.0

	def __str__(self):
		return f"\"{self.name}\" has a {round(self.winProbablity * 100, 3)} % chance of winning. Goes to tie breaker {round(self.tieProbablity * 100, 3)} % of the time"

def main():
	tournament = Tournament()
	startingPoint = LoadBracket('brackets/actual.bracket', tournament, 2)

	PlayerHandler("__^__^_//*v*//", "brackets/blake.bracket", tournament)
	PlayerHandler("Little Dribble", "brackets/adam.bracket", tournament)
	PlayerHandler("winner_ganadora", "brackets/an.bracket", tournament)
	PlayerHandler("At Least No Duke", "brackets/duke.bracket", tournament)
	PlayerHandler("The 'Eyes Have It", "brackets/eyes.bracket", tournament)
	PlayerHandler("Thundering Ferd", "brackets/ferd.bracket", tournament)
	PlayerHandler("JakeSickAFBracket", "brackets/jake.bracket", tournament)
	PlayerHandler("Wackabrack", "brackets/spence.bracket", tournament)
	PlayerHandler("Steven Kerr", "brackets/steve.bracket", tournament)
	PlayerHandler("TLaw and Order", "brackets/tlaw.bracket", tournament)
	PlayerHandler("Animal Fries", "brackets/rob.bracket", tournament)

	totalProbabilty = 0.0
	# for i in range(50):
	# for i in range(2**(BITS - 5)):
	for i in range(NUM_IDS):
		gen = GeneratedBracket(i, startingPoint, tournament)

		curMax = 0

		for player in PlayerHandler.ALL:
			playerValue = gen.getPoints(player.bracket)
			if playerValue > curMax:
				maxList = [player]
				curMax = playerValue
			elif playerValue == curMax:
				maxList.append(player)

		if len(maxList) == 1:
			maxList[0].winProbablity += gen.probability
		else:
			for player in maxList:
				player.tieProbablity += gen.probability

		totalProbabilty += gen.probability

		#print to screen
		# print(f"{i},{gen.probability}", end="")
		# for player in PlayerHandler.ALL:
		# 	print(f",{gen.getPoints(player.bracket)}", end="")
		# print()

	print(totalProbabilty)
	for player in sorted(PlayerHandler.ALL, key=lambda player: -player.winProbablity):
		print(player)

if __name__ == '__main__':
	main()
