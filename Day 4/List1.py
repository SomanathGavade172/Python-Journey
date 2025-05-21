import sys

Values = [10, 20, 30, 40]

print(Values)

print(type(Values))

print(len(Values))

print(sys.getsizeof(Values))

Values.insert(2, 11)
print("Data After Insert : ", Values)

Values.insert(15, 86)
print(Values)
print("Size of list is now : ", len(Values))
print("Data after insert i5 is : ", Values)

print(Values[0])
print(Values[1])
print(Values[2])
print(Values[3])
print(Values[4])


Values.append(50)

print(Values)

Values.remove(20)

print(Values)

print(type(Values[0]))

Values.append(90.89)

print(Values)