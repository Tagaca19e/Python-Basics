def one():
  #is -> is the same ID or the same object

  language = input("please enter your language: ")
  if language == 'python':
    print("the language is python")
  elif language == 'java':
    print("the language is java")
  else:
    print("the language is something else")

#one() 


def two():
  u = 'admin'
  o = False

  if u == 'admin' and o == True:
    print("The Admin is logged in")
  else:
    print("The Admin is not logged in")



#two()


def three():
  i = False

  if not i:
    print("I am an autobot")

  else:
    print("this is not 2nd")

#three()

#Challenge create a validator app for logging in


#def logging in 

def four():
  a = "this is not me"
  b = "this is not me"

  print(a is b)

  c = a
  print(a is c)

#four()

def five():
  #These are all false return false values
  o = {}
  a = []
  b = None
  c = 0

  if o:
    print("this is false")
  else:
    print("this is true")

five()