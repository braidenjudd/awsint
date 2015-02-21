import math

numbers = range(899, 902)
numbers_as_words = []

numbers_to_words_reference = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
	6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', \
	13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
    19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', \
    70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: 'Zero', 100: 'Hundred', 1000: 'Thousand', 1000000: 'Million'}

def number_less_than_1000_to_word(number):
	remainder = number
	word = ''

	while remainder != 0:
		if remainder >= 0 and remainder < 20:
			word += numbers_to_words_reference[remainder]
			remainder = 0

		if remainder >= 20 and remainder <= 99:
			tens, ones = divmod(remainder, 10)
			word += '{0}-{1}'.format(numbers_to_words_reference[tens * 10], numbers_to_words_reference[ones])
			remainder = 0

		if remainder > 99 and remainder < 1000:
			hundreds, remainder = divmod(remainder, 100)
			word += '{0} {1}'.format(numbers_to_words_reference[hundreds], numbers_to_words_reference[100])
			if remainder != 0:
				word += ' and '

	return(word)

def get_highest_magnitude_and_size(number):
	remainder = number
	number_size_thousands = 0
	
	while remainder >= 1000:
		remainder = int(math.floor(remainder / 1000))
		number_size_thousands += 1

	return (remainder, number_size_thousands)

def number_to_word(number):
	if number < 0 or number > 1000:
		raise Exception('{0} is out of range'.format(number))

	if number < 1000:
		return number_less_than_1000_to_word(number)
	else:
		while k in (k, v) > 0:
				

print(get_highest_magnitude_and_size(100000))
#print(map(number_to_word, numbers))