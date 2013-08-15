#!/usr/bin/python

import random

class DiceRoller(object) :

  def rollDice(self):

		print """
Enter the type of die
d2\nd3\nd4\nd6\nd8\nd10\nd20\nd100\nScatter
		"""
		diceType = raw_input("> ")
		print "Enter the number of rolls"
		diceRoll = raw_input("> ")

		diceType = str.lower(diceType)
		diceRoll = int(diceRoll)
		diceTotal = 0

		while diceRoll != 0 :
			if diceType == 'd2' :
				coin = random.randint(1, 2)
				if coin == 1 :
					print "Heads"
				else :
					print "Tails"
			elif diceType == 'd3' :
				print random.randint(1, 3)
			elif diceType == 'd4' :
				print random.randint(1, 4)
			elif diceType == 'd6' :
				print random.randint(1, 6)
			elif diceType == 'd8' :
				print random.randint(1, 8)
			elif diceType == 'd10' :
				print random.randint(1, 10)
			elif diceType == 'd20' :
				print random.randint(1, 20)
			elif diceType == 'd100' :
				print random.randint(1, 100)
			elif diceType == 'scatter' :
				scatterDie = random.randint(1, 6)
				if scatterDie == 1 :
					print "Hit"
				elif scatterDie == 6 :
					print "Hit"
				else :
					print "Miss"
			else :
				print "Input correct dice type."
			diceRoll = diceRoll - 1

	def startMenu(self) :
		
		menuOption = -1

		while menuOption != 0 :
			print """
Please make your selection:
	1.) Roll Dice
	2.) Show Totals
	0.) Exit Program
			"""
			menuOption = raw_input("> ")
			menuOption = int(menuOption)
			if menuOption == 1 :
				self.rollDice()
			elif menuOption == 2 :
				pass
			elif menuOption == 0 :
				print "Exiting program..."
				break
			else :
				print "Please make a valid selection"

runProg = DiceRoller()
runProg.startMenu()

