import random

class Deck:

	figures = ['Ace','King','Queen','Jack','Ten','Nine','Eight','Seven','Six','Five','Four','Three','Two']
	suits = ['Clubs','Diamonds','Hearts','Spades']
	strengths = [11,10,10,10,10,9,8,7,6,5,4,3,2]*4

	def __init__(self):
		
		self.deck = []
		self.buffer = []
		for x in Deck.suits:
			for y in Deck.figures:
				self.deck.append(y+' of '+x)

		self.deck = list(zip(self.deck, Deck.strengths))

	def shuffle(self):

		random.shuffle(self.deck)

	def pick_card(self):

		if len(self.buffer) == 52:
			self.deck = self.buffer
			self.buffer = []
			random.shuffle(self.deck)

		card = self.deck.pop()
		self.buffer.append(card)

		return card

class Player:

	def __init__(self):

		self.balance = 100

	def place_bet(self):

		while True:
			try:
				self.bet = int(input(f'Your current balance is {self.balance}. Place your bet '))
			except:
				print('It has to be an integer. Try again')
				continue
			if self.bet <= self.balance:
				break
			else:
				print('Your bet cannot exceed your balance. Try again')
				continue

	def win(self,factor):

		self.balance += self.bet*factor
		print('You won!')

	def lose(self):

		self.balance -= self.bet
		print('You lost!')

		if self.balance == 0:
			print('GAME OVER!!!')

class PlayerHand:

	def __init__(self):

		self.cards = []
		self.total = 0
		self.check = False

	def add_card(self,card):

		self.cards.append(card)
		self.total += card[1]
		if self.total > 21 and 'Ace' in card[0]:
			self.total -= 10

	def full_display(self):

		for x in range(0,len(self.cards)):
			
			print(self.cards[x][0])

		print('SUM: {}\n'.format(self.total))

class DealerHand(PlayerHand):

	def __init__(self):

		PlayerHand.__init__(self)

	def partial_display(self):

		print(self.cards[0][0])
		print('<HIDDEN CARD>\n')

def hit_or_stand():

	while True:
		x = input('Do you want to (h)it or (s)tand? ')
		if x[0].lower() != 'h' and x[0].lower() != 's':
			print('Wrong letter, try another one')
			continue
		else: 
			return x[0].lower()

def check_1(hand_of_player,hand_of_dealer,object_of_player):

	if hand_of_player.total == hand_of_dealer.total == 21:
		print('DRAW!')
		return True
	elif hand_of_player.total == 21:
		print('BLACKJACK!')
		object_of_player.win(2)
		return True
	elif hand_of_player.total > 21:
		object_of_player.lose()
		return True
	elif hand_of_player.total < 21:
		return False


while True:

	print('\nWELCOME TO BLACKJACK - THE BEST GAME YOU WILL PLAY THIS DECADE')
	deck = Deck()
	player = Player()

	while True:
		if player.balance == 0:
			break
		player.place_bet()
		playerhand = PlayerHand()
		dealerhand = DealerHand()
		deck.shuffle()
		playerhand.add_card(deck.pick_card())
		playerhand.add_card(deck.pick_card())
		dealerhand.add_card(deck.pick_card())
		dealerhand.add_card(deck.pick_card())
		print('DEALER:')
		dealerhand.partial_display()
		print('PLAYER:')
		playerhand.full_display()
		if check_1(playerhand,dealerhand,player) == True:
			continue
		else:
			while True:
				if hit_or_stand() == 'h':
					playerhand.add_card(deck.pick_card())
					print('PLAYER:')
					playerhand.full_display()
					if check_1(playerhand,dealerhand,player) == False:
						continue
					else:
						break
				else:
					print('DEALER:')
					dealerhand.full_display()
					while dealerhand.total <= 17:
						dealerhand.add_card(deck.pick_card())
						print('DEALER:')
						dealerhand.full_display()
					if dealerhand.total > 21:
						player.win(1)
						break
					elif dealerhand.total > playerhand.total:
						player.lose()
						break
					elif dealerhand.total == playerhand.total:
						print('DRAW!')
						break
					else:
						player.win(1)
						break

			continue


	while True:

		x = input('Do you want to play again? (y/n) ')
		if x[0].lower() != 'y' and x[0].lower() != 'n':
			print('Wrong letter, try another one')
			continue
		else:
			break

	if x[0].lower() == 'y':
		continue
	else:
		break
print('Thanks for playing')




	




	
				




		




