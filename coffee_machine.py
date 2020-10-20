class CoffeeMachine:
	def __init__(self):
		self.water = 400
		self.milk = 540
		self.beans = 120
		self.cups = 9
		self.money = 550

	def status(self):
		print("\nThe coffee machine has:")
		print(str(self.water) + " of water")
		print(str(self.milk) + " of milk")
		print(str(self.beans) + " of coffee beans")
		print(str(self.cups) + " of disposable cups")
		print("$"+str(self.money) + " of money")

	def reduce_resources(self, water_, milk_, beans_, cost):
		if self.water - water_ < 0:
			print("Sorry, not enough water!")
			return False
		elif self.milk - milk_ < 0:
			print("Sorry, not enough milk!")
			return False
		elif self.beans - beans_ < 0:
			print("Sorry, not enough beans!")
			return False
		elif self.cups - 1 < 0:
			print("Sorry, not enough cups!")
			return False
		else:
			self.water -= water_
			self.milk -= milk_
			self.beans -= beans_
			self.cups -= 1
			self.money += cost
			return True

	def buy(self):
		order = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
		res = False
		if order == '1':
			res = self.reduce_resources(250, 0, 16, 4)
		elif order == '2':
			res = self.reduce_resources(350, 75, 20, 7)
		elif order == '3':
			res = self.reduce_resources(200, 100, 12, 6)
		elif order == 'back':
			return
		if res:
			print("I have enough resources, making you a coffee!")

	def fill(self):
		self.water += int(input("Write how many ml of water do you want to add: \n"))
		self.milk += int(input("Write how many ml of milk do you want to add: \n"))
		self.beans += int(input("Write how many grams of coffee beans do you want to add: \n"))
		self.cups += int(input("Write how many grams of coffee beans do you want to add: \n"))

	def take(self):
		print("I gave you $" + str(self.money) + '\n')
		self.money = 0


def ft_user_input(machine):
	while True:
		command = input("\nWrite action (buy, fill, take, remaining, exit): \n")
		if command == "buy":
			machine.buy()
		elif command == "fill":
			machine.fill()
		elif command == "take":
			machine.take()
		elif command == "remaining":
			machine.status()
		elif command == "exit":
			exit(0)


if __name__ == '__main__':  # something like main() in C
	machine = CoffeeMachine()
	ft_user_input(machine)
