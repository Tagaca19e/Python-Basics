dic = { 
  "name" : "john",
  "age" : 25,
  "race" : "asian"
}




print(dic["age"])

print(dic.get('name'))


print(dic.get('phone', 'this is default'))

#updating values of the keys


dic["age"] = 19

print(dic)

#to update all in one

dic.update({
  "height" : 11,
  "phone" : 6613017863
 })


print(f"this is updated dic {dic}")


#del dic["name"]

dic.pop('name')

print(dic)

print(f"this is the length {len(dic)}")

print(f"this is the values only {dic.values()}")

print(f"this is the keys {dic.keys()}")

print(f"this is the item {dic.items()}")


for i, val in dic.items():
  print(i, val)


new = [(1, 2), (3,4), (5,6)]


for key, value in new:
  print(key, value)

for vala in dic.values():
    print(f"this is values {vala}")

for keys in dic:
    print(f"this is the key {keys}")


sValues = dic.values()

print(f"this is the values {sValues}")

