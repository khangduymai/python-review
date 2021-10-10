#%%
class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Yahee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I am flying")
        else:
            print("I need to walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.5)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on, the water's lovely")

    def quack(self):
        print("Quack, quack, quack...")

    def fly(self):
        self._wing.fly()

        
class Penguin(object):

    def walk(self):
        print("ola, ola, ola")

    def swim(self):
        print("Swimming for life")

    def quack(self):
        print("I cannot quack")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)
    print()
    donald.fly()
    print()
    bello = Penguin()
    test_duck(bello)
# %%
