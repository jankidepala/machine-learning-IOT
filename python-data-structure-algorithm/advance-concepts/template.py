from string import Template

def Main():
    cart = []
    cart.append(dict(item="Coke", price=8, qty=2))
    cart.append((dict(item="Cake", price=12, qty=1)))
    cart.append((dict(item="Fist", price=20, qty=5)))
    t = Template("$qty x $item = $price")
    total = 0
    print("cart ::")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("Total" + str(total))

Main()

Student = [('Tom', 90), ('Croby', 78), ('Bob', 92)]
t = Template('Hi $name, you have got $marks marks')

for i in Student:
    print(t.substitute(name=i[0], marks=i[1]))
