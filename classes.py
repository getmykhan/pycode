

class NameForm():
	"""The class will keep track of the employees that are passed"""

	sal_increment = 10
	def __init__(self, fname, lname, age, sex, salary):
		self.fname = fname
		self.lname = lname
		self.age = lname
		self.sex = sex
		self.salary = salary

	def name_format(self):
		name_formatted = self.fname + self.lname
		return(name_formatted)

	def salary_increment(self):
		self.salary = int(self.salary) + sal_increment
		return(self.salary)




if __name__ == '__main__':
	fname = input("Enter your fname")
	lname = input("Enter your lname")
	age = input("Enter your Age")
	sex = input("Enter Sex: M or F")
	salary = input("Enter the salary")



	emp1 = NameForm(fname, lname, age, sex = sex, salary = salary)

	print(NameForm.__doc__)