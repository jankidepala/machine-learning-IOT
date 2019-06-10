testingArray = ["Duck", "Hen", "Chicken" ]

print("Farm Animal",testingArray)

testingArray.append('Alpaca')
print("Appended",testingArray)

print("remove >>", testingArray.pop(1))
print("add Dog >>", testingArray.insert(1, "dog"))

car = ["Toyota, Camry"]
testingArray.extend(car)
print (testingArray.reverse())
print("New Farm Animal",testingArray)
print("Length >>",len(testingArray))