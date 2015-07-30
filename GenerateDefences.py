#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import math

goalKeepersList = [] 
defencesList = []

goalKeepersList.append(7)
goalKeepersList.append(6)
goalKeepersList.append(5)
goalKeepersList.append(4.5)
goalKeepersList.append(5)
goalKeepersList.extend([4.5] * 3)
goalKeepersList.extend([4] * 5)
goalKeepersList.extend([3.5] * 5)
goalKeepersList.extend([3] * 8)

defencesList.append(14)
defencesList.append(12)
defencesList.append(10)
defencesList.append(9.5)
defencesList.extend([9] * 4)
defencesList.extend([8.5] * 2)
defencesList.append(7.5)
defencesList.extend([7] * 3)
defencesList.extend([6.5] * 5)
defencesList.extend([5] * 7)

print goalKeepersList
print defencesList

fileName = "PreviousSeasonResults.txt"
file = open(fileName)
allLines = file.readlines()

team = ''
teamGoalDictionary = {}

for line in allLines:
    regex = re.compile('(.*?) (\d+) (\d+)\n')
    q = regex.search(line) 
    if q is not None:
        team = q.group(1)
        goalsConceded = int(q.group(2))
        gamesPlayed = int(q.group(3))
        teamGoalDictionary[team] = float(float(goalsConceded)/float(gamesPlayed))

import operator
sorted_teamGoalDictionary = sorted(teamGoalDictionary.items(), key=operator.itemgetter(1))

pricedTeams = []

for idx, teamGoalDictionaryInstance in enumerate(sorted_teamGoalDictionary):
    pricedTeams.append([teamGoalDictionaryInstance[0],defencesList[idx],goalKeepersList[idx],teamGoalDictionaryInstance[1] ])

for i in pricedTeams:
	print i[0] + ' :  Defence ' + str(i[1]) + ' : Goalkeeper ' + str(i[2])

