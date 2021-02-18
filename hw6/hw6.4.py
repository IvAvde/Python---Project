class Car:
    speed = 0
    color = 'color'
    name = 'name'
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print('Машина повернула в' + direction)

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('превышен скоростной лимит')

class SportCar(Car):
    def show_speed(self):
        print(self.speed)

class WorkCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('превышен скоростной лимит')

class PoliceCar(Car):
    def show_speed(self):
        print(self.speed)

tc = TownCar()
tc.speed = 70
tc.color = 'black'
tc.name = 'Mini'
tc.go()
tc.show_speed()


sc = SportCar()
sc.speed = 120
sc.color = 'yellow'
sc.name = 'Mercedes'
sc.go()
sc.show_speed()

wc = WorkCar()
wc.speed = 30
wc.color = 'green'
wc.name = 'Skoda'
wc.go()
wc.show_speed()

pc = PoliceCar()
pc.speed = 90
pc.color = 'white'
pc.name = 'Ford'
pc.is_police = True
pc.go()
pc.show_speed()