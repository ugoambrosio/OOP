class Customer:
	def __init__(self):
		self.cid = ''
		self.cname = ''
		self.acc_no = ''
		self.phone = ''
		self.emailID = ''
		self.balance = 0
		self.credit_card = []
		self.debit_card = ''
	def adding_a_customer(self):
		self.cid = input('Write the id of the account\n')
		self.cname = input('Write the name of the account\n')
		self.acc_no = input('Write the account number\n')
		self.phone = input('Write the phone number of the account\n')
		self.emailID = input('Write the email of the account\n')
		self.balance = int(input('Write the balance of the account\n'))
		self.credit_card = input('Write the number of the credit card\n')
		self.debit_card = input('Write the number of the debit card\n')
	def transfer_to(self, amount, recipient):
		if amount <= 0:
			print("Amount must be positive")
			return False
		if self.balance >= amount:
			self.balance -= amount
			recipient.balance += amount
			print("Transferred $", amount,"from", self.cname, " to ",recipient.cname)
			return True
		else:
			print("Insufficient balance")
			return False
def transfer_money(self, amount, recipient_card):
	if amount <= 0:
		print("Amount must be positive")
		return False
	if self.balance >= amount:
		self.balance -= amount
		recipient_card.balance += amount
		print("Transferred ",amount,"using card")
		return True
	else:
		print("Insufficient balance on card")
		return False
class Cards:
	def __init__(self):
		self.type = ''
		self.card_no = ''
		self.cvv = ''
		self.expiry_date = ''
		self.balance = 0
	def adding_a_card(self):
		self.type = input('Write the type of the card\n')
		self.card_no = input('Write the number of the card\n')
		self.cvv = input('Write the cvv of the card')
		self.expiry_date = input('Write the expiry date of the card\n')
		self.balance = int(input('Write the balance of the card of the card\n'))










acc1 = Customer()
acc1.adding_a_customer()

acc2 = Customer()
acc2.adding_a_customer()

cards = Cards()
cards.adding_a_card()


cards2 = Cards()
cards2.adding_a_card()

acc1.transfer_to(100, acc2)


cards.transfer_money(50, cards2)