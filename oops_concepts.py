# Employee - Class
# emp1 - instance
# num_of_emps - class variable
# first - instance varaible
# class method from_string alternate constructor used to create a new instance by performing operation on an input
# takes class as an argument rather than the instance
# static method is weekday is not related to 


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()

# print(Employee.num_of_emps)
# # adds to namespace of instance
# emp_1.raise_amount = 1.05
# # Prints the class variables
# print(Employee.raise_amt)
# # Applies class methods to the instance
# emp_1.apply_raise()
# # Accessing the instance attribute
# print(emp_1.pay)
# # Accessing the class variable using the instance
# print(emp_1.raise_amt)
# # Accessing the instance attribute
# print(emp_1.raise_amount)
# # Print name space of instance note the variable raise_amount
# print(emp_1.__dict__)
# # Print name space of class note the variable raise_amt and num_of_emps
# print(Employee.__dict__)

# emp_str_1="Rica-KRM-70000"
# emp_str_2="Sammy-NRK-75000"
# new_emp_1=Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)

# my_date=datetime.date(2020,1,18)
# print(Employee.is_weekday(my_date))