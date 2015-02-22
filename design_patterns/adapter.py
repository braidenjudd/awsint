class UserAdapter:
	def __init__(self, userClass):
		self.__user = userClass()

	def setName(self, firstname, lastname):
		if self.__user.__class__.__name__ == 'BrokenUser1':
			self.__user.setName(firstname, lastname)

		if self.__user.__class__.__name__ == 'BrokenUser2':
			self.__user.setName(firstname + lastname)

	def setAddress(self, streetAddress, postcode, suburb):
		if self.__user.__class__.__name__ == 'BrokenUser1':
			self.__user.setAddress(' '.join([streetAddress, suburb, postcode]))

		if self.__user.__class__.__name__ == 'BrokenUser2':
			self.__user.setAddress(streetAddress, postcode, suburb)

	def printAddressLabel(self):
		if self.__user.__class__.__name__ == 'BrokenUser1':
			self.__user.printAddressLabel()

		if self.__user.__class__.__name__ == 'BrokenUser2':
			self.__user.displayAddressLabel()

class BrokenUser1:
	def __init__(self):
		self.__firstname = ''
		self.__lastname = ''
		self.__address = ''

	def setName(self, firstname, lastname):
		self.__firstname = firstname
		self.__lastname = lastname

	def setAddress(self, address):
		self.__address = address

	def printAddressLabel(self):
		print("{0} {1} \n{2}".format(self.__firstname, self.__lastname, self.__address))

class BrokenUser2:
	def __init__(self):
		self.__name = ''
		self.__streetAddress = ''
		self.__postcode = ''
		self.__suburb = ''

	def setName(self, name):
		self.__name = name

	def setAddress(self, streetAddress, postcode, suburb):
		self.__streetAddress = streetAddress
		self.__postcode = postcode
		self.__suburb = suburb

	def displayAddressLabel(self):
		print("{0} \n{1}\n{2}, {3}".format(self.__name, self.__streetAddress, self.__suburb, self.__postcode))

bu = BrokenUser1()
bu2 = BrokenUser2()

bu.setName('Braiden', 'Judd')
bu.setAddress('11 Arnan Court Samford 4520')
bu.printAddressLabel()

bu2.setName('Braiden Judd')
bu2.setAddress('11 Arnan Court', 'Samford', '4520')
bu2.displayAddressLabel()

bu_adapter = UserAdapter(BrokenUser1)
bu_adapter.setName('Braiden', 'Judd')
bu_adapter.setAddress('11 Arnan Court', 'Samford', '4520')
bu_adapter.printAddressLabel()

bu_adapter2 = UserAdapter(BrokenUser2)
bu_adapter2.setName('Braiden', 'Judd')
bu_adapter2.setAddress('11 Arnan Court', 'Samford', '4520')
bu_adapter2.printAddressLabel()
