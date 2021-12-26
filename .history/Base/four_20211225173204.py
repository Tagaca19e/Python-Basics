def one():
  courses = ["math", "english", "cs"]
  cr = [1, 2, 3, 4]
  #print(courses[0:2])

  courses.append("hello")
  #print(courses)


  courses.insert(1, "beat")
  #print(courses)

  courses.extend(cr)
  print(courses)

  courses.remove("cs")
  print(courses)

  gg =courses.pop()
  print(gg)

  courses.pop()

  print(courses)

#one()


def sorting():

  al = ['g', 'a' ,'b']
  n = [2 ,1, 0]
  #al.sort(reverse=True)
  n.sort(reverse=True)
  hello = sorted(al)

  print(f"this is hello {hello}")
  print(al)
  print(n)

  ourSum = sum(n)
  print(f"this is our sum {ourSum}")


#sorting()


def searching():
  my = ["meme", "hehe", "huhu"]
  word = "I am eidmone tagaca"
  print(my.index("meme"))
  print(word.find('am'))

#searching()
#=====================


def looping():


  my = ['cs', 'english', 'math']


  for i, val in enumerate(my):
    print(f"{i} and {val}")
    print(i, val)

  my2 = [[1,2], [3, 4], [5, 6]]


  for i, val3 in enumerate(my2):
    a, b = val3

    print(f"This is val3 {a} , {b}")

  for val2 in my2:
    one, two = val2

    print(one, two)

#looping()


def looping2():
  my = ['cs', 'english', 'math']

  for j in my[1:]:
    print(f"This is my {j}")

  for a in my[:2]:
    print(f"This is hello {a}")

  for i, cr in enumerate(my, start =1):
    print(i, cr)

#looping2()


def joining():
  my = ['cs', 'english', 'math']

  hello2 = "My name is eidmone"
  hello = ', '.join(my)


  newList = hello.split(', ')
  newList2 = hello2.split(' ')
  print(my)
  print(hello)
  print(newList)
  print(newList2)
#joining()


def tuples():

  my = ('cs', 'english', 'math')

  print(my[1])

tuples()


def setts():
  #sets only value is part of the sets not how many quantities does it have
  
  cs = {'cmps1', 'cmps2', 'cmps3', 'cmps4', 'cmps4'}


  art = {'cmps1', 'cmps2', 'hist', 'art'}

  num = {1, 2, 3, 4, 4}

  print(num)
  print(cs.intersection(art))

  print(cs.difference(art))

  print(cs.union(art))

  print('cmps1' in cs)
  

  empty = set()

  empty.add(1)
  empty.add(2)


  print(f"This is my set {empty}")

setts()