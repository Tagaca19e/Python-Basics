
#import sys
#sys.path.append('/path/to/your/file')

import mod
import random


from mod import valueChecker, name, person as clazz

#from mod import * 


data = [1,2,3,4,5]

target = 5
def one():
  res = valueChecker(target, data)

  print(res)


  print(name)

#one()

etagaca = clazz('eidmone', 19, 'CSUB')

#print(etagaca.age)


def two():
  for i in range(20):
    value = random.randint(1,2) 
    print(value)


#two()


import math

def three():
  val = math.ceil(4.23)

  print(val)


three()


import random
def four():
  val2 = random.choices([1,2,3,4,5])
  print(val2)
four()
