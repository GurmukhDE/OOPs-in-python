class Car:
    brand = "Ford"
    model = "bronco"

car1 = Car

print(car1.brand, car1.model)


class Student:
    def __init__(self, fullname):
        self.name = fullname


s1= Student("gurmukh")

print(s1.name)


class Car:
    def __init__(self, brand,model, country):
        self.brand = brand
        self.model = model
        self.country = country

car_info = Car("Ford", "Bronco", "USA")
print(car_info.brand, car_info.model, car_info.country)

#----------------------------------------------------------

"""Q-  create Student class that takes name, and marks of 3 subjects as arguments in constructor then create
a method to print the avg of marks"""


class Student:#this is class
    def __init__(self, name, marks):#this is constructor
        self.name = name #these are attr1
        self.marks = marks#attr2

    def get_avg(self):# this the method for avg
        sum = 0
        for val in self.marks:
            sum+=val

        print("Hi", self.name, "your avg score is:", sum/3)

stu1 = Student("Gurmukh", [90,92,95])
stu1.get_avg()

stu1.name = "Noddy" 
stu1.marks = [75,86,93]
stu1.get_avg()

#-------------------------------------------------------------

class Student:# this is class name
  def __init__(self, name, marks):# this is constructor
    self.name = name #attr 1
    self.marks =marks #attr 2
    
  def get_avg(self):# this is method
    sum = 0
    for val in self.marks:
      sum+=val
    print("Hi", self.name, "your avg score is:", self.marks)

stu = Student("tom", [80,97,99])
stu.get_avg()

stu.name = "jerry"
stu.marks = [78,99,99]
stu.get_avg()

#-------------------------------------------------------------------

"""Q-  create Account class with 2 attributes - balance and account no.
       create method for debit, credit & printing the balance. """


class Account:
   def __init__(self, balance, account_no):
      self.balance = balance
      self.account_no =account_no

   def debit(self, amount):
      self.balance -= amount
      print("Rs", amount, "was debited")
      print("total balance = ", self.get_balance())
 
   def credit(self, amount):
      self.balance += amount
      print("Rs", amount, "was credited")
      print("total balance = ", self.get_balance())

   def get_balance(self):
      return self.balance

acc1 = Account(10000, 2049000000874)   
print(acc1.balance)   
print(acc1.account_no)
acc1.debit(2300)
acc1.credit(500) 
      
