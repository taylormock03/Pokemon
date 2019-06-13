DESCRIPTION:

	This is Pokemon generation 1 (Red/Blue). It is a command prompt version of the original games and contains all 151 of the original gen 1 pokemon (No I did not add MissingNo.) Due to this being an early build, I would appreciate any feedback, bug reports, or suggestions for further versions.


CHANGELOG:
	1.1.0:
		Added a store to buy pokemon
	
	1.0.1:
		Fixed minor bugs
		Small UI changes
	
	1.0:
		Initial release of Pokemon


KNOWN BUGS:
	
	Entering a non-integer value into the "Which attack would you like?" prompt during battles causes crashes. This is an easy fix 		but I'm too lazy to fix it so I probably won't fix it soon


	Some attacks don't interact as they should within the original games e.g double slap doesn't actually attack twice. 	Buffs/debuffs also didn't work as originally intended 	because some data was hard to find


	Wild pokemon can be over level 100


	You can get stuck in an endless crash if you use a level 100 pokemon who has earned 9,999,999,999,999,999,999,999 xp (Likely not 	going to fix this because that would require a 	tonne of grinding to reach in the first place as you earn ~5000-7000 xp per 	fight at that level)


	If you have less than 4 moves learned, you have to assign new moves to not explicitly mentioned options (e.g if you only have 2 	moves, the highest given option will be #1 but 	you need to enter #2 or #3)


	Only pokemon who dealt the last attack receive any XP	


	Magikarp is even harder to level up due to no XP share being implemented into the game


	You can currently catch an infinite amount of legendary pokemon, and they are just as common as any other pokemon in their area


	Attempting trainer battles after the final one is complete results in a crash


PLANNED FEATURES:

	Adding a multiple generations feature, allowing to play Gen 1 - 7


	[X] Adding a shop to buy pokemon, allowing to buy pokemon that aren't catchable in your generation (note: this will only be 	backwards compatible, not forwards so you can't get something like Arceus in Gen 1)


	Adding consumable items such as potions and berries


	Adding HM's and TM's (I'm not sure if there are any HM's or TM's currently available, although they are in the code)


	Adding Custom generations/gamemodes (note: this will likely require the user to manually code this, I don't currently plan on 	implementing a way to create new gamemodes within a python script)


	Adding graphics/GUI - depending on the scale and difficulty, I will either use a python library such as PyGame or use more 	simple ASCII representations of the pokemon	


	Rebalancing current pokemon - Many pokemon are way over/underpowered


	Adding infinite trainer battles
