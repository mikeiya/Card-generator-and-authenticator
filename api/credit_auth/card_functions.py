"""
The different validation functions...
and a function for generating card numbers

a better card_iin and card_mii method would use
REGEX to match the start of the card_number
and find the matching key-value pair in mii_list and
nii_list respectively
"""
from random import randint,choice

mii_list = {
    '0':        'ISO/TC 68 and other industry assignments',
    '1':	'Airlines',
    '2':	'Airlines and other industry assignments',
    '3':        'Travel and entertainment',
    '4':	'Banking and financial',
    '5':	'Banking and financial',
    '6':	'Merchandizing and banking',
    '7':	'Petroleum',
    '8':	'Telecommunications and other industry assignments',
    '9':	'National assignment'
    }

iin_list = {
    '37':       'Amex',
    '4':        'Visa',
    '5':        'Mastercard',
    '6011':   'Discover',
    '65':      'Discover'
    }


generated_cards = {}

def generate_card(type=None):
	"""
	Prefill some values based on the card type
	"""
	card_types = ["amex","visa","mastercard"]

	def prefill(t):
		"""
		Prefill with initial numbers and return it including the total number of digits
		remaining to fill
		"""
		# typical number of digits in credit card
		def_length = 16
		
		if t == card_types[0]:
		    # american express starts with 3 and is 15 digits long
		    # override the def lengths
		    return [3, randint(4,7)], 13
		
		elif t == card_types[1] or t == card_types[2]:
		    # visa starts with 4
		    return [4], def_length - 1
		
		elif t == card_types[2]:
		    # master card start with 5 and is 16 digits long
		    return [5, randint(1,5)], def_length - 2
		# choose any of the three card types if type not specified
		return prefill(choice(card_types))

	def finalize(nums):
		"""
		Make the current generated list pass the Luhn check by checking and adding
		the last digit appropriately by calculating the check sum
		"""
		check_sum = 0
		"""
		Reason for this check offset is to figure out whther the final list is going
		to be even or odd which will affect calculating the check_sum.
		This is mainly also to avoid reversing the list back and forth which is specified
		on the Luhn algorithm.
		"""
		check_offset = (len(nums) + 1) % 2
		
		for i, n in enumerate(nums):
		    if (i + check_offset) % 2 == 0:
		        n_ = n*2
		        check_sum += n_ -9 if n_ > 9 else n_
		    else:
		        check_sum += n
		return nums + [10 - (check_sum % 10) ]

	initial, rem = prefill(type)
	def card_generator(initial,rem):
		"""
		create the full card number using the prefilled list and 
		a list of random integers of size remaining(rem)
		"""
		so_far = initial + [randint(1,9) for x in range(rem - 1)]
		return "".join(map(str,finalize(so_far)))

	result = card_generator(initial,rem)
	# to avoid generating duplicate cards
	while result in generated_cards:
		result = card_generator(initial,rem)
	else:
		generated_cards[result] = 1
	return result

def get_card_info(card,card_number):
    """
    card data generator
    """
    card['MII'] = card_mii(card_number)
    card['IIN'] = card_iin(card_number)
    card['Personal_Account_Number'] = card_number
    return

def card_is_valid(card_numbers):
    """
    a simple checksum to verify card_number
    and returns the check_digit
    """
    if len(card_number) < 13 or len(card_number) > 16:
        return False,0
    nSum = 0
    isSecond = False
    for  i in card_numbers[::-1]:
        try:
            digit = int(i)
        except:
            return False
        if isSecond == True:
            digit *= 2
        #add two digits to handle
        #cases that make two digits after
        # doubling
        nSum += digit // 10
        nSum += digit % 10
        isSecond = not isSecond
    return (nSum % 10 == 0),nSum

def  card_mii(card_number):
    """
    returns The Major Industry Identifier
    """
    return 'unknown mii' if card_number[0] not in mii_list else mii_list[card_number[0]]

def  card_iin(card_number):
    """
    returns The Issuer Identification Number
    """
    return 'unknown iin' if card_number[0] not in iin_list else iin_list[card_number[0]]

def  card_pan(card_number):
    """
    returns The personal account number
    """
    return card_number
