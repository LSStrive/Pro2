# class A():
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#
#     def __str__(self):
#         return self.name + " " + self.password
#
#     def print(self):
#         print('The user username and password are：', self.name, 'and',  self.password)

class TriangleArea():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def sum(self):
        return (self.a + self.b + self.c)/2
    def area(self):
        s = self.sum()
        return (s * (s - self.a) * (s - self.b) * (s - self.c))**0.5

