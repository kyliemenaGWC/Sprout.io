print("Welcome you are a cow! Type start when you are ready")
start = input()

while start != "start":
	print ("Please type start")
	start = input()

print ("are you a 'female' or 'male'?")
gender = input()

while gender != ("female" or "male"):
	print ("please answer me")
	gender = input()

if gender == "female":
	print("You are taken to an auction site and taken away from your mother")
	print("what will you do? You can 'cry' or 'kick the nearest human'")
	choice1= input()
	
	while choice1 != ("cry" or "kick the nearest human"):
		print ("please answer me")
		choice1 = input()

	if choice1 == "cry":
		print ("you spend the rest of the car ride crying to yourself until you get to a new farm")
	elif choice1 == "kick the nearest human":
		print ('''You kick the man loading your friend into the truck
		 and break her free. Since he was the only guy around you two 
		 have some spare time and use it to free the rest of the cows
		 nearby. You all make a break for it and run until sundown. 
		 You are safe but your mother isn't. Since you saved all the
		 other cows you have become the rebel leader for the 'cow freedom movement' 
		 a radical new organizatino that does its best to save as many 
		 cows as possible. Your first mission is to go undercover as a 
		 lost cow and save your mother. You need to pick your undercover 
		 outfit do you go in a 'black suit' or the 'cow suit' or go 'naked' ''')

		choice2= input ()
		while choice2 != ("black suit" or "cow suit" or "naked"):
			print ("please answer me")
			choice2 = input()
		if choice2 == "black suit":
			print ('''Omg a passerby sees you and takes a selfie with you. 
				You are now the talk of the country. You are given a manager 
				and have to manage your new multi-million dollar company. 
				Crap! Your mom is still at the farm! She could be dead for 
				all you know it. The entire world donates so you can 'buy' 
				your mother from the farmer and you are successful but that 
				still isn't good enough. The world is full of other innocent 
				cows that are being slaughtered everyday. You begin a campaign 
				to make the whole entire world vegan but it doesn't work. 
				Sorry girl. ''')
		elif choice2 == "cow suit":
			 print(''' 
			 	You walk up to the farm and wait.... 
			 	and wait... 
			 	and wait... 
			 	several days pass and nobody has noticed you. 
			 	You think something happened to the farm until 
			 	you hear a child say 'what a cute statue!' 
			 	Crap! Your plan failed and you weren't able to save your mom''')
		elif choice2 == "naked":
			print ('''
				 A farmer cries of joy when they find you 
				and hold you in a pen for the rest of the night. 
				You overhear that you will be sent away the next 
				morning so you need to move fast. You look for your 
				mother. 
				Where is she? 
				WHERE IS SHE? 
				Finally a familiar smell guides you to the slaughter 
				house! You break in just in time before your mother 
				was chopped to bits! You use your sharp hooves to 
				break the machine and knock the dude unconscious. 
				Then you kick over a tnt pack lying randomly on the 
				floor and get the heck out of there. Your mother 
				follows quickly and while the slaughter house burns 
				and the humans are distracted you and the rest of 
				the cows make a break for it. You head back to base. 
				Phew! You're safe..''')	 		
elif gender == "male":
	print('''amn dood feels bad you do get to stay with your mother for most
	 of your life but... your life isn't very long.. if you catch my drift.....''') 
