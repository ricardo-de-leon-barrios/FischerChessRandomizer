# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 00:13:05 2023

@author: Ricardo
"""
import random as rn

positions = [0,1,2,3,4,5,6,7]

rook1 = rn.choice(positions)
positions.remove(rook1)

if rook1 == 0: positions.remove(rook1+1)
elif rook1 == 7: positions.remove(rook1-1)
else:
    positions.remove(rook1-1)
    positions.remove(rook1+1)

rook2 = rn.choice(positions)
positions.remove(rook2)

minRook = min(rook1,rook2)
maxRook = max(rook1,rook2)

kingPositions = []
for i in range(maxRook):
    if i > minRook: kingPositions.append(i)
king = rn.choice(kingPositions)

newPositions = [0,1,2,3,4,5,6,7]
newPositions.remove(rook1), newPositions.remove(rook2), newPositions.remove(king)

bishop1 = rn.choice(newPositions)
newPositions.remove(bishop1)

secondPositions = []
if bishop1 % 2 == 0:
    for l in newPositions:
        if l % 2 != 0: secondPositions.append(l)
elif bishop1 % 2 != 0:
    for x in newPositions:
        if x % 2 == 0: secondPositions.append(x)

bishop2 = rn.choice(secondPositions)
newPositions.remove(bishop2)

knight1 = rn.choice(newPositions)
newPositions.remove(knight1)

knight2 = rn.choice(newPositions)
newPositions.remove(knight2)

queen = newPositions[0]

order = {
    rook1: "Rook",
    rook2: "Rook",
    king: "King",
    bishop1: "Bishop",
    bishop2: "Bishop",
    knight1: "Knight",
    knight2: "Knight",
    queen: "Queen"}

finalOrder = []
for y in range(8):
    finalOrder.append(order[y])

print(finalOrder)