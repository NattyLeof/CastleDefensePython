## Option 4 CASTLE DEFENSE - NATHANIEL LEOF P7
## This is like castle defense but changed. Instead of stockpiling for one huge battle it is a constant war with the goal of survival. You must survive 100 days. There are also different upgrades. 
import random

def Help(  ):
	print ("")
	print ("CASTLE DEFENSE is a game about strategic upgrading. The goal of the game is to upgrade your castle to allow you to survive attacks from zombies for 100 days.")
	print ("")
	print ("At the start of each day your population grows by one. You start with 10 people.")
	print ("")
	print ("You then have the chance to exchange your people for buildings and upgrades. To see potential upgrades, type -upgrades-.")
	print ("")
	print ("When you are asked what you want to do, you can respond with -help-, -upgrades-, and upgrade such as -armour-.")
	print ("")
	print ("After upgrading, there is a chance you will be attacked. During an attack, you and the zombies will roll a die. Whoever rolls a lower number will lose.")
	print ("")
	print ("If you lose or draw a battle, you will lose people.")
	print ("")
	print ("To end the day, type -done-, or -d-.")
	print ("")
	print ("To see your upgrades and people, type -army-.")
	print ("")
	print ("The amount of people lost when attacked in based off what day it is and how many barracks you have. ")
	print ("")
	print ("If you ever want to read these messages again, just type -help-")
	print ("")
	
def Upgrades (  ):
	print ("")
	print ("barracks")
	print ("COST: 10 PEOPLE")
	print ("EFFECT: The barrack allows you to recruit one more unit a turn.")
	print ("")
	print ("weaponry")
	print ("COST: 15 PEOPLE")
	print ("EFFECT: You roll a one higher sided die than before.")
	print ("")
	print ("armour")
	print ("COST: 6  PEOPLE")
	print ("EFFECT: If any of your units are to die, one less dies instead.")
	print ("")
	print ("espionage")
	print ("COST: 20 PEOPLE")
	print ("EFFECT: The zombies roll a five sided die, not a six. This upgrade can only be bought once.")
	print ("")
	print ("fortune-teller")
	print ("COST: 35 PEOPLE")
	print ("EFFECT: The fortune-teller will warn you at the start of your day if you will be attacked that night. This upgrade can only be bought once.")
	print ("")
	print ("lucky-clover")
	print ("COST: 10 PEOPLE")
	print ("Whenever you roll a multiple of 4 on your die, you will gain people equal to the current number of people recruited each turn.")
	print ("")
	print ("beer")
	print ("COST: 4 PEOPLE")
	print ("EFFECT: If you are attacked the night of buying beer, you will roll a die with one more side.")
	print ("")
	print ("gamble")
	print ("COST: 3 PEOPLE")
	print ("EFFECT: 50% Chance to gain 5 people. If you gamble 5 times in one turn you get a free beer. ")
    
while True:
	name = input("Hello! What is your name?: ")
	Help()
	print ("Welcome to CASTLE DEFENSE {}!".format(name))
	day = 0
	people = 10
	playerdie = 6
	zombiedie = 6
	barracks = 0
	weaponry = 0
	espionage = 0
	fortuneteller = 0
	recruitment = 1
	armour = 0
	battleswon = 0
	battleslost = 0
	battlesdrawn = 0
	luckyclover = 0
	while day <= 99 and people > 0:
		day = day + 1
		people = people + recruitment
		attacking = 0
		dailybeer = 0
		dailygamble = 0
		if day > 89:
			random2 = random.randint(1,2)
			if random2 == 2:
				attacking = 1
		if day > 74 and day < 90:
			random3 = random.randint(1,3)
			if random3 == 3:
				attacking = 1
		else:
			random4 = random.randint(1,4)
			if random4 == 4:
				attacking = 1
		print ("It is day {}".format(day))
		if recruitment == 1:
			print ("You have recruited 1 new person.".format(recruitment))
		else:
			print ("You have recruited {} new people.".format(recruitment))
		print ("You have {} people.".format(people))
		if fortuneteller == 1:
			if attacking == 1:
				print ("You are going to be attacked tonight!")
			else: 
				print ("You are not going to be attacked tonight!")
		while True: 
			action = input("What do you want to do? ")
			if (action == "help") or (action == "upgrades") or (action == "done") or (action == "barracks") or (action == "weaponry") or (action == "armour") or (action == "espionage") or (action == "fortune-teller") or (action == "beer") or (action == "gamble") or (action == "army") or (action == "d") or (action == "lucky-clover"): 
				if action == "help":
					Help()
				if action == "upgrades":
					Upgrades()
				if action == "barracks":
					if people > 10:
						people = people - 10 
						recruitment = recruitment + 1
						barracks = barracks + 1
						print ("You now have {} barracks. You will recruit {} people a day.".format(barracks, recruitment))
					else:
						print ("You do not have enough people to purchase a barrack.")
				if action == "weaponry":
					if people > 15:
						people = people - 15
						weaponry = weaponry + 1
						playerdie = playerdie + 1
						print ("You know have {} weaponries. You will now roll a {} sided die".format(weaponry,playerdie))
					else:
						print ("You do not have enough people to purchase a weaponry")
				if action == "armour":
					if people > 6:
						people = people - 6
						armour = armour + 1
						print ("You now have {} sets of armour. You will lose {} less people whenever you are to lose any.".format(armour,armour))
					else:
						print ("You do not have enough people to purchase a set of armour")
				if action == "espionage":
					if people > 20 and espionage == 0:
						people = people - 20
						espionage = espionage + 1
						zombiedie = zombiedie - 1
						print ("The zombies will now roll a 5 sided die.")
					elif espionage == 1:
						print ("You have already purchased the espionage upgrade.")
					else: 
						print ("You do not have enough people to purchase the espionage upgrade.")
				if action == "gamble":
					if people > 3:
						dailygamble = dailygamble + 1
						random2 = random.randint(1,2)
						if random2 == 2:
							people = people + 2
							print ("You won the gamble! You have been given 5 people! You now have {} people.".format(people))
						else:
							people = people - 3
							print ("You lost the gamble! You lost your 3 person investment. You now have {} people.".format(people))
						if dailygamble == 5:
							dailybeer = dailybeer + 1
							playerdie = playerdie + 1
							print ("You have gambled 5 times today! Have a free beer. You now have now drunk {} beers today. You will roll a {} sided die today".format(dailybeer,playerdie))
					else: 
						print ("You do not have enough people to gamble.")
				if action == "beer":
					if people > 4:
						people = people - 4
						dailybeer = dailybeer + 1
						playerdie = playerdie + 1
						print ("You have now drunk {} beers today. You will roll a {} sided die today.".format(dailybeer,playerdie))
					else:
						print ("You do not have enough people to buy a beer.")
				if action == "army":
					if people == 1:
						print ("You have 1 person.")
					else:
						print ("You have {} people.".format(people))
					if barracks == 1:
						print ("You have 1 barrack")
					else: 
						print ("You have {} barracks.".format(barracks))
					if weaponry == 1:
						print ("You have 1 weaponry.")
					else:
						print ("You have {} weaponries.".format(weaponry))
					if armour == 1:
						print ("You have 1 set of armour.")
					else:
						print ("You have {} sets of armour.".format(armour))
					if espionage == 1:
						print ("You have purchased the espionage upgrade.")
					else:
						print ("You have not purchased the espionage upgrade.")
					if fortuneteller == 1:
						print ("You have a fortune teller in your army.")
					else:
						print ("You have not recruited a fortune-teller.")
					if luckyclover == 1:
						print ("You have a lucky-clover")
					else:
						print ("You do not have a lucky-clover.")
				if action == "fortune-teller":
					if fortuneteller == 0 and people > 35:
						fortuneteller = 1
						people = people - 35
						print ("You have purchased a fortune teller. will now be told at the start of your turn if you will be attacked at night. You now have {} people.".format(people))
					elif fortuneteller == 1:
						print ("You have already purchased a fortune-teller")
					else:
						print ("You do not have enough people to purchase a fortune-teller.")
				if action == "lucky-clover":
					if luckyclover == 0 and people > 10:
						luckyclover = 1
						people = people - 10
						print ("You have purchased a lucky-clover. You will gain people equal to the current number of people gained each day when you roll a multiple of four.")
						print ("You now have {} people.".format(people))
					elif luckyclover == 1:
						print ("You have already purchased a lucky-clover.")
					else: 
						print ("You do not have enough people to purchase a lucky-clover.")
				if action == "done" or action == "d":
					break
			else:
				print ("I do not understand that command. Type -help- for help or -upgrades- for upgrades. Remember to answer with all lower-case letters. Thank you {}!".format(name))
		if attacking == 1:
			print ("You have been attacked!")
			playerroll = random.randint(1,playerdie)
			zombieroll = random.randint(1,zombiedie)
			if playerroll > zombieroll:
				print ("You won the battle! You rolled a {} on your {} sided die. The zombies rolled a {} on their {} sided die.".format(playerroll,playerdie,zombieroll,zombiedie))
				battleswon = battleswon + 1
			if playerroll == zombieroll: 
				peoplelost = recruitment 
				people = people - peoplelost
				print ("The battle ended in no one being victorious. You rolled a {} on your {} sided die. The zombies rolled a {} on their {} sided die. You lost {} people. You now have {} people.".format(playerroll,playerdie,zombieroll,zombiedie,peoplelost,people))
				battlesdrawn = battlesdrawn + 1
			if playerroll < zombieroll:
				if day > 0 and day < 10:
					peoplelost = 3
					people = people - peoplelost
				if day > 9 and day < 20:
					peoplelost = 6
					people = people - peoplelost
				if day > 19 and day < 40:
					if recruitment < 3:
						peoplelost = 12
					else:
						peoplelost = recruitment * 3
						peoplelost = peoplelost + 2
					people = people - peoplelost
				if day > 39 and day < 60:
					random2 = random.randint(0,2)
					if recruitment < 5: 
						peoplelost = 18
					else:
						peoplelost = recruitment * 4
						peoplelost = peoplelost + 4
					people = people - peoplelost
				if day > 59 and day < 90:
					if recruitment < 5:
						peoplelost = 35
					else:
						peoplelost = recruitment * 5
						peoplelost = peoplelost + 6
					people = people - peoplelost
				if day > 89:
					if recruitment < 6:
						peoplelost = 45
					else:
						peoplelost = recruitment * 6
					people = people - peoplelost
				if armour > 0:
					if armour < peoplelost:
						people = people + armour 
						peoplelost = peoplelost - armour
						print ("After using your {} sets of armour, you lost {} people. You rolled a {} on your {} sided die. The zombies rolled a {} on their {} sided die. You now have {} people.".format(armour,peoplelost,playerroll,playerdie,zombieroll,zombiedie,people))
					else:
						people = people + peoplelost
						peoplelost = 0
						print ("You had armour for all of your people that would have died! You lost {} people. You now have {} people.".format(peoplelost,people))
				else:
					print ("You lost the battle. You rolled a {} on your {} sided die. The zombies rolled a {} on their {} sided die. You lost {} people. You now have {} people.".format(playerroll,playerdie,zombieroll,zombiedie,peoplelost,people))
				battleslost = battleslost + 1
			if luckyclover == 1 and playerroll % 4 == 0:
				people = people + recruitment
				if recruitment == 1:
					print ("You rolled a {}! Because of your lucky-clover, you have recruited 1 person. You now have {} people.".format(playerroll,people))
				else:
					print ("You rolled a {}! Because of your lucky-clover, you have recruited {} people. You now have {} people.".format(playerroll,recruitment,people))
			
		else:
			print ("You were not attacked tonight!")
		print ("")
		playerdie = playerdie - dailybeer
	if day >= 100:
		print ("")
		print (" _     _  _____  _   _ ")
		print ("( )   ( )(  _  )( ) ( )")
		print ("`\`\_/'/'| ( ) || | | |")
		print ("  `\ /'  | | | || | | |")
		print ("   | |   | (_) || (_) |")
		print ("   (_)   (_____)(_____)")
		print ("")
		print (" _       _  _  _   _  _ ")
		print ("( )  _  ( )(_)( ) ( )( )")
		print ("| | ( ) | || || `\| || |")
		print ("| | | | | || || , ` || |")
		print ("| (_/ \_) || || |`\ || |")
		print ("`\___x___/'(_)(_) (_)(_)")
		print ("                     (_)")
		print ("")		
		print ("Congratulations, you survived!")
		print ("You ended the game with:")
		if people == 1:
			print (" 1 person.")
		else:
			print (" {} people.".format(people))
		if barracks == 1:
			print (" 1 barrack.")
		else:	
			print (" {} barracks.".format(barracks))
		if weaponry == 1:
			print (" 1 weaponry.")
		else:
			print (" {} weaponries.".format(weaponry))
		if armour == 1:
			print (" 1 set of armour.")
		else:
			print (" {} sets of armour.".format(armour))
		if espionage == 1:
			print (" 1 unit trained in espionage.")
		else:
			print (" 0 units trained in espionage.")
		if fortuneteller == 1:
			print (" 1 fortune-teller.")
		else:
			print (" 0 fortune-tellers.")
		if luckyclover == 1:
			print (" 1 lucky-clover.")
		else: 	
			print (" 0 lucky-clovers")
		print (" {} battles ended in you being victorious.".format(battleswon))
		print (" {} battles ended in no one being victorious.".format(battlesdrawn))
		print (" {} battles ended in the zombies being victorious.".format(battleslost))
	else:
		print ("")
		print (" _     _    ")
		print ("( )   ( ) ")
		print ("`\`\_/'/'_    _   _ ")
		print ("  `\ /'/'_`\ ( ) ( )")
		print ("   | |( (_) )| (_) |")
		print ("   (_)`\___/'`\___/'")
		print ("")
		print (" _                 _   ")
		print ("(_ )              ( )_ ")
		print (" | |    _     ___ | ,_)")
		print (" | |  /'_`\ /',__)| | ")
		print (" | | ( (_) )\__, \| |")
		print ("(___)`\___/'(____/`\__)")
		print ("") 
		print ("You were defeated on day {}.".format(day))
		print ("You ended the game with:")
		if barracks == 1:
			print (" 1 barrack.")
		else:	
			print (" {} barracks.".format(barracks))
		if weaponry == 1:
			print (" 1 weaponry.")
		else:
			print (" {} weaponries.".format(weaponry))
		if armour == 1:
			print (" 1 set of armour.")
		else:
			print (" {} sets of armour.".format(armour))
		if espionage == 1:
			print (" 1 unit trained in espionage.")
		else:
			print (" 0 units trained in espionage.")
		if fortuneteller == 1:
			print (" 1 fortune-teller.")
		else:
			print (" 0 fortune-tellers.")
		if luckyclover == 1:
			print (" 1 lucky-clover.")
		else: 	
			print (" 0 lucky-clovers")
		print (" {} battles ended in you being victorious.".format(battleswon))
		print (" {} battles ended in no one being victorious.".format(battlesdrawn))
		print (" {} battles ended in the zombies being victorious.".format(battleslost))
	while True:
		action = input("Would you like to play again? -y/n- ")
		if (action == "y") or (action == "n"):
			print ("Thank you for playing {}!".format(name))
			break
		else:
			print ("I do not understand your answer. Please respond with -y- for yes or -n- for no.")
	if action == "n":
		break
		print ("Thank you for playing {}!".format(name))
	
			
	

			
            


        
    
    
    
	
	
	
