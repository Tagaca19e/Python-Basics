import random
from scond import person
from scond import student
def quiz(): 
  q = [
    "What is the color of my hair? \n a. blue \n b. yellow \n c. red",
    "What is the color of my car? \n a. gray \n b. white \n c. black",
    "What is my name? \n a. eidmone \n b. adrian \n c. jake",
  ]
  count = 0
  class questions:
    def __init__(self, choices, ans):
      self.choices = choices
      self.ans = ans


  alpha = "abc"
  r = random.randint(0, 2)
  for i in range(len(q)):

    num = questions(q[i], alpha[r])
    print(num.choices)
    word = input("Please enter your answer: ")
    if word == num.ans:
      count+= 1
  
  print("You got " + str(count) + "/3!")


#quiz()

def classFunctions():
  s1 = person("eidmone" , 3.65, "male")
  s2 = student("jake", 3.4, "female", "business")
  print(s1.wHonors())

  print(s2.wHonors())
  print(s2.hello())




classFunctions()

class hello:

  def __init__(self, a,b,c):
    self.a = a
    self.b = b
    self.c = c
class hello2(hello):
  def __init__(self, a, b, c, d):
    hello.__init__(self, a, b, c)
    self.d = d
