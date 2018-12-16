class Animo:

    def __init__(self):
        self.data = []

    def append(self):
        self.data.append('kuhui')


class Dog(Animo):
    def append(self):
        self.data.append("sdoicjs")




a = Animo()
dog = Dog()
a.append()
print(a.data)

for item in zip([3, 4], [52, 5]):
    print(item)
