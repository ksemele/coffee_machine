class CoffeeMachine:
	def __init__(self):
		self.water = 400
		self.milk = 540
		self.beans = 120
		self.cups = 9
		self.money = 550

	def status(self):
		print("The coffee machine has:")
		print(str(self.water) + " of water")
		print(str(self.milk) + " of milk")
		print(str(self.beans) + " of coffee beans")
		print(str(self.cups) + " of disposable cups")
		print("$"+str(self.money) + " of money")

	def buy(self):
		order = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
		if order == 1:
			self.water -= 250
			self.beans -= 16
			self.money += 4
			self.cups -= 1
		elif order == 2:
			self.water -= 350
			self.milk -= 75
			self.beans -= 20
			self.money +=7
			self.cups -= 1
		elif order == 3:
			self.water -= 200
			self.milk -= 100
			self.beans -= 12
			self.money += 6
			self.cups -= 1
		print("")
		self.status()

	def ft_fill(self):
		self.water += int(input("Write how many ml of water do you want to add: "))
		self.milk += int(input("Write how many ml of milk do you want to add: "))
		self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
		self.cups += int(input("Write how many grams of coffee beans do you want to add: "))
		print("\n")
		self.status()

	def ft_take(self):
		print("I gave you $" + str(self.money) + '\n')
		self.money = 0
		self.status()


def ft_user_input(machine):
	while True:
		command = input("\nWrite action (buy, fill, take, remaining, exit): ")
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
	machine.status()
	ft_user_input(machine)
