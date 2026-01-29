#---------------------------------------Multiple inheritance----------------------------

"""In multiple inheritance a child class can inherit from 2 parent class see example below"""


class A:
    varA = "welcome to the class A"

class B:
    varB =  "welcome to class B"

class C(A, B):
    varC = "welcome to class C"



c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)
