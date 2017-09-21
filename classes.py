

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
		self.salary = int(self.salary) + self.sal_increment
		return(self.salary)

	@classmethod
	def set_class_sal_increment(cls):
		cls.sal_increment = 100
			



if __name__ == '__main__':
	fname = input("Enter your fname")
	lname = input("Enter your lname")
	age = input("Enter your Age")
	sex = input("Enter Sex: M or F")
	salary = input("Enter the salary")



	emp1 = NameForm(fname, lname, age, sex = sex, salary = salary)
	emp2 = NameForm(fname, lname, age, sex = sex, salary = salary)
	#print("Salary incremented from {} to {}".format(salary, emp1.salary_increment()))