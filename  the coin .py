import random 
print('welcome to the coin guessing game! ')
print('choose a method to toss the coin :')
print('1. using random.random()')
print('2.using random.randint()')

user =int(input('inter you choise (1or 2):'))

if user == 1 :
	coin = random.random()
	if coin >= 0.5 :
		computer_result = 'head'
	else:
		computer_result = 'tails'
		
elif user ==2 :
		coin2 = random.randint(0,1)
		if coin2 == 0:
			computer_result= 'head'
		else :
			computer_result = 'tails'
			
else:
	print('please enter number (1or2)')
	
	
user_choice =input('inter your guessing (head or tails)')

if user_choice.lower() == computer_result.lower() :
	print('great , you win')
else :
	print('sorry , you lost')

print ('the computer result was :', {computer_result})