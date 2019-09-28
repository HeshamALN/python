from datetime import date

class Employee:
	def __init__(self, name, age, salary,employment_date):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date

	def get_working_years(self):
		return date.today().year - int(self.employment_date)
		# self.get_working_years = 2019 - self.employment_date

	def __str__(self):
		return "Employees\nName: %s, Age: %s, Salary: %s, Working Years: %s" % (self.name, self.age, self.salary, self.get_working_years())

class Manager(Employee):
	def __init__(self, name, age, salary,employment_date,bonus_percentage):
		super().__init__(name,age,salary,employment_date)
		self.bonus_percentage = bonus_percentage
	def get_bonus(self):
		return float(self.bonus_percentage) * float(self.salary)

	def __str__(self):
		return "Employees\nName: %s, Age: %s, Salary: %s, Working Years: %s, Bonus: %.3f" % (self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())


print("Welcome to HR Pro 2019")
print()

options = ['Show Employee', 'Show Managers', 'Add An Employee', 'Add A Manager', 'Exit']

for x in options:  #making a list
	i = 1+ options.index(x)   
	print(i,x)#3

employees = [] #2
managers = []  #2

# hesham = Employee("Hesham", 27, 100, "26/09/2019")


userselect = input("What would you like to do? ")
while userselect != '5':
	# userselect = input("What would you like to do? ")
	if userselect == '1':
		for employee in employees:
			print(employee)
		
	elif userselect == '2':
		for manager in managers:
			print(manager)
		
	elif userselect == '3': #6
		# print("-----------------")
		name = input("Name: ")
		age = input("Age: ")
		salary = input("Salary: ")
		employment_date = input("Employement year: ")
		employee = Employee(name,age,salary,employment_date)
		employees.append(employee)
		print("Employee added succesfully")
		
#If 3 was chosen, allow the HR employee to add a normal employee to the system (the employees list).
	elif userselect == '4': #7
		# print("-----------------")
		name = input("Name: ")
		age = input("Age: ")
		salary = input("Salary: ")
		employment_date = input("Employement year: ")
		bonus_percentage = input("Bonus Percentage: ")
		manager = Manager(name,age,salary,employment_date, bonus_percentage)
		managers.append(manager)
		print("Manager added succesfully")
	userselect = input("What would you like to do? ")
# #If 4 was chosen, allow the HR employee to add a manager to the system (the managers list).
# userselect == '5'	
# 	print("Thank you and goodbye!")a
# 	quit()

