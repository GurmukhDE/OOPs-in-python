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
