#!/usr/bin/env python3

from Tournament import Tournament

class Bracket(object):
	"""docstring for Bracket"""
	def __init__(self, name, values, tournament, maxRounds = None):
		super(Bracket, self).__init__()
		self.name = name
		self.values = values
		self.tournament = tournament
		self.maxRounds = maxRounds if maxRounds is not None else tournament.numRounds
		self._constructPredictions(values, tournament, self.maxRounds)

	def _constructPredictions(self, values, tournament, maxRounds):
		self.gamePredictions = []
		for round in range(min(tournament.numRounds, maxRounds)):
			start, end = tournament.getRoundRange(round)

			for game in range(start, end):
				teamA, teamB = self.getTeamsFromGame(game)
				self.gamePredictions.append(teamA if values[game] else teamB)

	def getTeamsFromGame(self, game):
		#simple case of the first round
		if game < self.tournament.numTeams / 2:
			return (game * 2), (game * 2 + 1)

		#next rounds
		last_start, last_end = self.tournament.getRoundRange(0)

		for round in range(1, self.tournament.numRounds):
			start, end = self.tournament.getRoundRange(round)

			if game in range(start, end):
				first_game = (game - start) * 2 + last_start
				return self.gamePredictions[first_game], self.gamePredictions[first_game + 1]

			last_start = start

	def getPoints(self, other):
		points = 0

		for round in range(0, min(self.maxRounds, other.maxRounds)):
			start, end = self.tournament.getRoundRange(round)

			for game in range(start, end):
				if self.gamePredictions[game] == other.gamePredictions[game]:
					points += (2**round)

		return points

	def getStrGame(self, value):
		teamA, teamB = self.getTeamsFromGame(value)

		winner = self.gamePredictions[value]

		return f"In game between {self.tournament.getTeam(teamA).name} and {self.tournament.getTeam(teamB).name} picked {self.tournament.getTeam(winner).name}"

	def __str__(self):
		return self.name

	def printRound(self, round):
		start, end = self.tournament.getRoundRange(round)
		for i in range(start, end):
			print(self.getStrGame(i))


def main():
	tournament = Tournament()

	actual = LoadBracket("brackets/actual.bracket", tournament, 2)
	player = LoadBracket("brackets/rob.bracket", tournament)

	start, end = tournament.getRoundRange(3)
	for i in range(start, 63):
		print(player.getStrGame(i))

	# start, end = tournament.getRoundRange(1)
	# for i in range(start, end):
	# 	print(player.getStrGame(i))

	print(actual.getPoints(player))

def LoadBracket(fileName, tournament, maxRounds=None):
	bools = []
	with open(fileName) as bracketFile:
		for row in bracketFile:
			bools.append(row[0] == "T" or row[0] == "t")

	return Bracket(fileName, bools, tournament, maxRounds)

if __name__ == '__main__':
	main()
