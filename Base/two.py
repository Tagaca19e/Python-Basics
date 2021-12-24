tuples = [(4, 5), (6, 1), (9, 0)]
#This cannot be modified

#print(tuples[0][0])


#================================

def hello1(name, age):
  print("hello " + name + " " +  age)


#name = input("Please enter your name: ")
#age = input("Please enter your age: ")
#hello1(name, age)

def cube(num):
  return pow(num, 3)

hello = cube(3)

#print(hello)

#IF statements===============

def maleFunc():
  isMale = True
  isTall = False
  if isMale and isTall:
    print("damn your a guy and you are tall")
  elif not isTall:
    print("You are a girl")
  else:
    print("this is our final condition")


maleFunc()





def heightFunc(inp):
  
 # inp = float(inp)

  if inp == "5.7":
    print("damn you are short")
  elif inp == "5.0" or inp == "5":
    print("damn you are really short")
  else:
    print("Damn you are tall")

#what = input("Enter your height: ")
#heightFunc(what)

def max_num(num1, num2, num3):
  one = max(num1, num2)
  return max(one, num3)


def max_num1(num1, num2, num3):

  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  else:
    return num3


num1 = 7
num2 = 1
num3 = 10


rex = max_num1(num1, num2, num3)
res = max_num(num1, num2, num3)


#print(rex, res)


def calculator(num1, num2, op):

  num1 = int(num1)
  num2 = int(num2)
  if op == "+":
     return num1 + num2
  elif op == "-":
      return num1 - num2
  elif op == "/":
      return num2 / num1
  elif op == "*":
      return num1 * num2

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
op = input("Enter operator: ")
print(calculator(num1, num2, op))