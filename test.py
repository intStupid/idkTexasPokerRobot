from hands import selected_hand
from hands import card
from hands import hand
import random

def random_compare_test():
	# use to count how many regeneration of card has occured
	regen_count = 0
	test_hand1 = selected_hand([])
	test_hand2 = selected_hand([])

	for i in range(5):
		test_hand1.cards.append(card("A23456789JQK"[random.randrange(0,12)] + "hsdc"[random.randrange(0,4)]))
		while test_hand1.cheat_test():
			test_hand1.cards[-1] = (card("A23456789JQK"[random.randrange(0,12)] + "hsdc"[random.randrange(0,4)]))
			regen_count += 1
			# avoid regenerate too much because randrange bugs
			if regen_count > 1000:
				print("too much regenerate")
				return None

	for i in range(5):
		test_hand2.cards.append(card("A23456789JQK"[random.randrange(0,12)] + "hsdc"[random.randrange(0,4)]))
		while test_hand2.cheat_test():
			test_hand2.cards[-1] = (card("A23456789JQK"[random.randrange(0,12)] + "hsdc"[random.randrange(0,4)]))
			regen_count += 1
			# avoid regenerate too much because randrange bugs
			if regen_count > 1000:
				print("too much regenerate")
				return None

	hand1_rank = test_hand1.detailed_rank()
	hand2_rank = test_hand2.detailed_rank()

	print("hand1:", test_hand1, "rank:", hand1_rank)
	print("hand2:", test_hand2, "rank:", hand2_rank)

	if hand1_rank > hand2_rank:
		return "hand1 wins"
	elif hand1_rank < hand2_rank:
		return "hand2 wins"
	else:
		return "draw"

def random_selection_test():
	# use to count how many regeneration of card has occured
	regen_count = 0
	test_hand = hand([])

	#generate private cards
	for i in range(2):
		test_hand.cards.append(card("A23456789JQK"[random.randrange(0,12)] + "hsdc"[random.randrange(0,4)]))
		while test_hand.cheat_test():
			test_hand.cards[-1] = (card("A23456789JQK"[random.randrange(0,12)] + "hsdc"[random.randrange(0,4)]))
			regen_count += 1
			# avoid regenerate too much because randrange bugs
			if regen_count > 1000:
				print("too much regenerate")
				return None

	#generate public cards
	for i in range(5):
		test_hand.cards.append(card("A23456789JQK"[random.randrange(0,12)] + "hsdc"[random.randrange(0,4)]))
		while test_hand.cheat_test():
			test_hand.cards[-1] = (card("A23456789JQK"[random.randrange(0,12)] + "hsdc"[random.randrange(0,4)]))
			regen_count += 1
			# avoid regenerate too much because randrange bugs
			if regen_count > 1000:
				print("too much regenerate")
				return None

	best_hand = selected_hand(test_hand.find_best_hand())

	return "full hand: " + str(test_hand) + "\nbest possible hand: " + str(best_hand)


########################################
#            used for test             #
########################################

print(random_compare_test())
print()
print(random_selection_test())