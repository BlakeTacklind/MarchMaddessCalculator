#!/usr/bin/env python3

from Tournament import Tournament
from LoadBracket import LoadBracket, Bracket

BITS = 15
NUM_IDS = 2**BITS

class GeneratedBracket(Bracket):
	"""docstring for GeneratedBracket"""
	def __init__(self, thisId, start, tournament):
		self.thisId = thisId
		super(GeneratedBracket, self).__init__(str(thisId), start.values + GeneratedBracket.getValuesFromID(thisId), tournament)
		self.probability = 1
		for i in range(tournament.numGames - BITS, tournament.numGames):
			
			teamA, teamB = self.getTeamsFromGame(i)
			winner = self.gamePredictions[i]

			if teamA == winner:
				self.probability *= tournament.getTeam(teamA).probability(tournament.getTeam(teamB))
			if teamB == winner:
				self.probability *= tournament.getTeam(teamB).probability(tournament.getTeam(teamA))


	@staticmethod
	def getValuesFromID(thisId, bits=BITS):
		values = []
		for val in range(bits):
			values.append((thisId & (1 << val)) > 0)

		return values

def main():
	tournament = Tournament()

	startingPoint = LoadBracket('brackets/actual.bracket', tournament, 2)
	player = LoadBracket("brackets/ferd.bracket", tournament)

	for i in range(50):
	# for i in range(2**(BITS - 5)):
		gen = GeneratedBracket(i, startingPoint, tournament)
		print(i, gen.probability, gen.getPoints(player))
		# print(gen.getPoints(player))

	# for i in range(100):
	# 	GeneratedBracket(i)
	# print(GeneratedBracket.getValuesFromID(512))

if __name__ == '__main__':
	main()
