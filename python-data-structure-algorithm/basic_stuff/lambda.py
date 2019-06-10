# Lambda is implicit
# no return
x = lambda a : a + 10
print(x(5))

mx = lambda x, y, z:x if x>y else y
print(mx(5, 1, 0))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Class
class P:
    def __init__(self, n):
        self.newObk = n
    def newF(self, m):
        print("New func", m)

p1 = P("Some name")
print("AS",p1)
p1.newF("SDxx")

del p1
print("AS",p1)