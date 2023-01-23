import random


times = 0 
print('ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!')
while True:
	s = input()
	if s == "ПОКА!":
		times = times + 1
		if times == 3:
			print("ДО СВИДАНИЯ, МИЛЫЙ!")
			break
	elif s != "ПОКА!":
		times = 0
	if s.isdigit(): 
		print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
	elif s.islower():
	    print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
	if s.isupper():
		print(f'НЕТ, НИ РАЗУ С {random.randint(1930,1950)} ГОДА')

	    
		
 