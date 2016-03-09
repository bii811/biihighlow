#!/usr/bin/python
#High Low Game
#Author: bii811

import random, os, sys

winScore = 0
loseScore = 0
maxWin = 0

while(1):
	os.system("clear")
	os.system("cls")
	random.seed()

	print("#"*55)
	print("#######  Welcome to High Low Game              ########")
	print("#######  Author: bii811                        ########")
	print("#"*55,"\n")

	print("="*23)
	print("   Max win in a row: %s" % maxWin)
	print("   Win:  %s" % winScore)
	print("   Lose: %s" % loseScore)
	print("="*23)
	
	rndnum1 = random.randint(0, 10);
	print("\nGuess next number will be lower or higher than [ %s ] ?" % rndnum1)
	rndnum2 = random.randint(0, 10);
	input_lh = ""
	cpResult = ""

	while(input_lh != "l") and (input_lh != "h") and (input_lh != "t"):
		print("(l = Lower, h = Higher, t = Equal , q = Quit)")
		input_lh = input("Input l, h or t: ")
		if(input_lh == "q"):
			print("\n-- Thank you for playing! See you later :) --")
			sys.exit()

	print("\n>>>>     %s    <<<<" % rndnum2)

	if(rndnum1 < rndnum2):
		print(">>>>   Higher  <<<<")
		cpResult = "h"
	elif(rndnum1 > rndnum2):
		print(">>>>   Lower   <<<<")
		cpResult = "l"
	else:
		print(">>>>    Tie    <<<<")
		cpResult = "t"

	if(input_lh == cpResult):
		winScore += 1
		maxWin += 1
		print(">>>> You Win!  <<<<")
	else:
		loseScore += 1
		maxWin = 0
		print(">>>> You Lose! <<<<")
		
	input("\nPress Enter to continue...")
