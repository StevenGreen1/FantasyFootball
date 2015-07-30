#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import math

strikersList = [] 

print 'Git testing'

strikersList.append(10)
strikersList.append(8)
strikersList.append(7)
strikersList.append(6)
strikersList.extend([5.5] * 2)
strikersList.extend([5] * 6)
strikersList.extend([4.5] * 7)
strikersList.extend([4] * 15)
strikersList.extend([3.5] * 21)
strikersList.extend([3] * 40)
strikersList.extend([2.5] * 27)
strikersList.extend([2] * 21)
strikersList.extend([1.5] * 11)
strikersList.extend([1] * 2)

#print strikersList
#print len(strikersList)

fileName = "StrikersForNewSeason.txt"
file = open(fileName)
allLines = file.readlines()

team = ''
strikersDictionary = {}

count = 0

for line in allLines:
    regex = re.compile('(.*?) (.*?) (\d+) (\d+)(.*?)\n')
    q = regex.search(line) 
    count = count + 1
    if q is not None:
        team = q.group(1)
        player = q.group(2)
        goalsScored = int(q.group(3))
	gamesPlayed = int(q.group(4))
        strikersDictionary[(team,player)] = goalsScored * 38 / gamesPlayed
        print team + "   " + player

import operator
sorted_strikersDictionary = sorted(strikersDictionary.items(), key=operator.itemgetter(1))

print sorted_strikersDictionary

pricedStrikers = []

for idx, striker in enumerate(list(reversed(sorted_strikersDictionary))):
    pricedStrikers.append([striker[0],strikersList[idx],striker[1]])

for i in pricedStrikers:
    print str(i[0][0]) + ' ' + str(i[0][1]) + ' ' + str(i[1])

