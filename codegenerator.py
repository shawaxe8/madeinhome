'''
Text Tab Random Codegenerator
'''

import random
import sys

print("Where do you start to hold the fret?(Enter num)")
fret = int(input())
print("Where do it end?(Enter num (must be greater than start))")
fret2 = int(input())

if (fret2 <= fret):
	print("*Number must be greater than start*")
	sys.exit()

frets = list(range(fret, fret2 + 1))
frets.append("x")

if (fret != 0):
	print("Do you want to include open string?(Enter y/n)")
	open = input()
	
	if (open == "y"):
		frets.append(0)

print("How many codes do you need?(Enter num(Max 10))")
num = int(input())

if (num >= 10):
	print("*Number must be less than 10*")
	sys.exit()
	
print("E|", end="")
for code in range(num):
		print(random.choice(frets), end="-")
print("|\n", end="")

print("B|", end="")
for code in range(num):
		print(random.choice(frets), end="-")
print("|\n", end="")

print("G|", end="")
for code in range(num):
		print(random.choice(frets), end="-")
print("|\n", end="")

print("D|", end="")
for code in range(num):
		print(random.choice(frets), end="-")
print("|\n", end="")

print("A|", end="")
for code in range(num):
		print(random.choice(frets), end="-")
print("|\n", end="")

print("E|", end="")
for code in range(num):
		print(random.choice(frets), end="-")
print("|\n", end="")
