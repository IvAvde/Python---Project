import time
class Trafficlight:
    __color = 'no color by default'

    def running(self):
        self.__color = 'red'
        print(self.__color)
        time.sleep(7)
        self.__color = 'yellow'
        print(self.__color)
        time.sleep(2)
        self.__color = 'green'
        print(self.__color)
        time.sleep(7)

trl = Trafficlight()

Trafficlight.running(trl)