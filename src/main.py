import unroll as ur
# Sample python code for github
print("Hello!, Good Morning!")

person = ur.Person()

CLAY = ur.Person('Clayton Lin')
person.addFriend(CLAY)

ERIKA = ur.Person('Erika Rosero')
person.addFriend(ERIKA)

print (person.friends)