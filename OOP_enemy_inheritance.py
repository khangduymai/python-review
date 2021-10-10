class Enemy:

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self.alive = False


    def __str__(self):
        return "Name: {0._name}, Hit points: {0._hit_points}, Lives: {0._lives}".format(self)


# CASE1: When the Troll class has no __init__
# class Troll(Enemy):
#     pass


# CASE2: When the Troll class has defined __init__ with parameter name
class Troll(Enemy):
    
    def __init__(self, name):
        # Enemy.__init__(self, name=name, hit_points=23, lives=1)
        # super(Troll, self).__init__(name=name, hit_points=23, lives=1)
        super().__init__(name=name, hit_points=23, lives=1)


    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))
        

class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        import random
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodged *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


