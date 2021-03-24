#!/usr/bin/env python3

import csv
import math

FILE_NAME = "players.csv"

class Team(object):
	"""docstring for Team"""
	def __init__(self, name, rank, location, power):
		super(Team, self).__init__()
		self.name = name
		self.rank = int(rank)
		self.location = location

		if self.location == "West":
			self.locationValue = 0
		elif self.location == "East":
			self.locationValue = 1
		elif self.location == "South":
			self.locationValue = 2
		elif self.location == "Midwest":
			self.locationValue = 3
		else:
			raise "No such location"

		self.power = float(power)

	def __str__(self):
		return f"{self.name} ({self.power}) - {self.location} {self.rank}"

	@property
	def weight(self):
		#total guess
		return 1/((100 - self.power) ** 2.5)

	def probability(self, other):
		return self.weight / (self.weight + other.weight)

	def __eq__(self, other):
		return self.number == other.number

class Tournament(object):
	"""docstring for Tournament"""
	def __init__(self):
		super(Tournament, self).__init__()
		self.teams = Tournament.tournamentSort(Tournament.LoadTeams(FILE_NAME))

		for i in range(self.numTeams):
			self.teams[i].number = i

	def getTeam(self, team):
		return self.teams[team]

	@property
	def numRounds(self):
		return int(math.log(self.numTeams, 2))

	@property
	def numGames(self):
		return self.numTeams - 1

	@property
	def numTeams(self):
		return len(self.teams)

	def getRoundRange(self, round):
		if round > self.numRounds:
			raise "Nope"

		return self.numGames-(2**(self.numRounds - round)) + 1, self.numGames-(2**(self.numRounds - round - 1)) + 1

	@staticmethod
	def LoadTeams(fileName):
		teams = []
		with open(fileName) as csvfile:
			read = csv.reader(csvfile)
			for name, rank, location, power in read:
				teams.append(Team(name, rank, location, power))

		return teams

	@staticmethod
	def tournamentSort(teams):
		regions = [list(),list(),list(),list()]

		for team in teams:
			regions[team.locationValue].append(team)

		sortedList = list()
		for region in regions:
			ranked = sorted(region, key=lambda team: team.rank)

			sortedList.append(ranked[1 - 1])
			sortedList.append(ranked[16 - 1])

			sortedList.append(ranked[8 - 1])
			sortedList.append(ranked[9 - 1])

			sortedList.append(ranked[5 - 1])
			sortedList.append(ranked[12 - 1])

			sortedList.append(ranked[4 - 1])
			sortedList.append(ranked[13 - 1])

			sortedList.append(ranked[6 - 1])
			sortedList.append(ranked[11 - 1])

			sortedList.append(ranked[3 - 1])
			sortedList.append(ranked[14 - 1])

			sortedList.append(ranked[7 - 1])
			sortedList.append(ranked[10 - 1])

			sortedList.append(ranked[2 - 1])
			sortedList.append(ranked[15 - 1])

		return sortedList



def testRange():
	print(Tournament().getRoundRange(0))
	print(Tournament().getRoundRange(0) == (0,32))
	print(Tournament().getRoundRange(1))
	print(Tournament().getRoundRange(1) == (32,48))
	print(Tournament().getRoundRange(2))
	print(Tournament().getRoundRange(2) == (48,56))
	print(Tournament().getRoundRange(3))
	print(Tournament().getRoundRange(3) == (56,60))
	print(Tournament().getRoundRange(4))
	print(Tournament().getRoundRange(4) == (60,62))
	print(Tournament().getRoundRange(5))
	print(Tournament().getRoundRange(5) == (62,63))
	# print(Tournament().getRoundRange(6) == (0,31))


if __name__ == '__main__':
	testRange()
