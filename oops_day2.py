#-------------------del(keyword)-----------------
from loguru import logger

class Student:
   def __init__(self, name):
      self.name = name


s1 = Student("gurmukh")
logger.info(s1.name)
del s1
logger.info(s1.name)



#----------------------------Private(like)-attribute and methods----------------

class Account():
   def __init__(self, acc_no, acc_pass):
      self.acc_no  = acc_no
      self.acc_pass = acc_pass
      self.__acc_pass = acc_pass#here u can see we've made this private by adding "__"

acc1 = Account(139400002, "abcde")
logger.info(acc1.acc_no)  
logger.info(acc1.acc_pass) 
logger.info(acc1.__acc_pass)#here I am calling the fuction but is giving me error bcz I've made this private
