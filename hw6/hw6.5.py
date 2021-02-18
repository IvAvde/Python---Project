class Stationery:
    title = 'title'

    def draw():
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw():
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw():
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw():
        print('Запуск отрисовки маркером')

pen = Pen
pen.draw()

pc = Pencil
pc.draw()

h = Handle
h.draw()
