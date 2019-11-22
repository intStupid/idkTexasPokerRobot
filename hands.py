class card:
	def __init__(self,card_value):
		#card is encoded in the form of rank + suit
		#rank is A234567890JQK
		#suit is h(hearts "hong tao") s(spades "hei tao") d(diamonds "fang pian") c(clubs "cao hua")
		#ex. "0h" is heart 10 ("hong tao shi")
		self.card_value = card_value
		self.rank = card_value[0].upper()
		self.suit = card_value[1].lower()

	def __str__(self):
		return self.card

	#turn the rank into int for comparion
	def int_rank(self):
		return "234567890JQKA".find(self.rank)

	#compare the suit of two cards
	def same_suit(self,other):
		if self.suit == other.suit:
			return True
		else:
			return False

	#define eq as the same card:
	def __eq__(self, other):
		if self.card_value == other.card_value:
			return True
		else:
			return False

class selected_hand:
	def __init__(self, hands=[]):
		#hands attribute should be a list of card object
		#number of cards in selected hand should be 5
		self.cards = hands

	def __str__(self):
		output = []
		for item in self.cards:
			output.append(item.card_value)
		return str(output)

	#return the number of cards 
	def num_cards(self):
		return len(self.cards)

	#sort the hand from low to high in terms of rank
	def sort(self):
		self.cards.sort(key = card.int_rank)

	#to test if there are the same card in the hand
	def cheat_test(self):
		for i in range(len(self.cards)):
			for j in range(i+1, len(self.cards)):
				if self.cards[i] == self.cards[j]:
				#print("You nei gui, zhong zhi jiao yi")
					return True
		return False

	#flush test
	def flush(self):
		for i in range(len(self.cards) - 1):
			if not self.cards[i].same_suit(self.cards[i+1]):
				return False
		return True

	#straight test
	def straight(self):
		self.sort()
		temp = ""
		for item in self.cards:
			temp += item.rank
		if temp in "234567890JQKA" or temp == "2345A":
			return True
		else:
			return False

	#count the cards with same rank, returns the pattern of the hand in form of list
	#the parttern means that the number in the list is representing the multiplicity of the sorted hand
	#for example, KKKAA should be [3,3,3,2,2]
	def same_rank_count(self):
		self.sort()
		count = 1
		output = []
		for i in range(1,len(self.cards)):
			if self.cards[i].rank == self.cards[i-1].rank:
				count += 1
			else:
				#append the count into the list count times 
				for j in range(count):
					output.append(count)
				count = 1
		#to append the multiplicity of the last card in the hand
		for j in range(count):
			output.append(count)
		return output

	#determin the type of the hand
	def hand_type(self):
		#test if there are 5 cards
		if self.num_cards() > 5:
			print("Too many cards!")
			return None
		elif self.num_cards() < 5:
			print("Not enough cards!")
			return None

		# 9 => Royal Flush
		# 8 => Straight Flush
		# 7 => Four of A Kind
		# 6 => Full House
		# 5 => Flush
		# 4 => Straight
		# 3 => Three of A Kind
		# 2 => Two Pair
		# 1 => One Pair
		# 0 => High Card

		#retrive the list of card pattern and calculate the product of the pattern as a way to determin the pattern
		self.eigenlist = self.same_rank_count()
		eigenvalue = 1
		for value in self.eigenlist:
			eigenvalue = eigenvalue * value

		isFlush = self.flush()
		isStraight = self.straight()

		if self.cards[4].rank == "A" and isFlush and isStraight:
			return 9

		elif isFlush and isStraight:
			return 8

		elif 4 in self.eigenlist:
			return 7

		#eigenlist [3,3,3,2,2] 
		elif eigenvalue == 108:
			return 6

		elif isFlush:
			return 5

		elif isStraight:
			return 4

		#eigenlist [3,3,3,1,1] 
		elif eigenvalue == 27:
			return 3

		#eigenlist [2,2,2,2,1] 
		elif eigenvalue == 16:
			return 2

		#eigenlist [2,2,1,1,1] 
		elif eigenvalue == 4:
			return 1

		else:
			return 0

	#calculating the rank of the hands in case there are the same type on table
	#bigger hands will have higher rank
	def detailed_rank(self):
		#get hand type
		hand_type = self.hand_type()
		card_go_overed = 0
		#the hand typr is still the dominant factor of the rank, so it will be put on the highest significant digit with five zeros on its left
		#the zeros on the left will be filled the rank of individual card in hexadecimal in the sequence determined below
		output = hand_type * 0x100000

		#the rank of individual card will fill the zeros from left to right in order of: 1. the multiplicity from small to large; 2. the position in sorted list from right to left
		for i in [1,2,3,4]:
			for j in range(len(self.eigenlist)):
				if self.eigenlist[j] == i:
					output += self.cards[j].int_rank()*(0x10**card_go_overed)
					card_go_overed += 1

		return output

class hand:
	def __init__(self, hands=[]):
		#hands attribute should be a list of card object
		#number of cards in selected hand should be 5
		self.cards = hands

	def __str__(self):
		output = []
		for item in self.cards:
			output.append(item.card_value)
		return str(output)

	#return the number of cards 
	def num_cards(self):
		return len(self.cards)

	#sort the hand from low to high in terms of rank
	def sort(self):
		self.cards.sort(key = card.int_rank)

	#to test if there are the same card in the hand
	def cheat_test(self):
		for i in range(len(self.cards)):
			for j in range(i+1, len(self.cards)):
				if self.cards[i] == self.cards[j]:
				#print("You nei gui, zhong zhi jiao yi")
					return True
		return False

	#return the best combo in given cards in forms of list and its rank together in forms of tuple
	def find_best_hand(self):
		#verify the number of cards in the hand since it has O(n^5)
		if self.num_cards() > 7:
			print("too many card")
			return None

		self.sort()
		temp_best_rank = 0
		temp_best_hand = []

		for i in range(len(self.cards) - 4):
			for j in range(i + 1, len(self.cards) - 3):
				for k in range(j + 1, len(self.cards) - 2):
					for l in range(k + 1, len(self.cards) - 1):
						for m in range(l + 1, len(self.cards)):
							temp_hand = selected_hand([self.cards[i],self.cards[j],self.cards[k],self.cards[l],self.cards[m]])
							temp_rank = temp_hand.detailed_rank()
							if temp_rank > temp_best_rank:
								temp_best_rank = temp_rank
								temp_best_hand = [self.cards[i],self.cards[j],self.cards[k],self.cards[l],self.cards[m]]
		return temp_best_hand

########################################
#            used for test             #
########################################

# test = selected_hand([card("4h"),card("4s"),card("5d"),card("5h"),card("9s")])
# print(test.detailed_rank())
# print(test.eigenlist)