class Road:
    _length = 1000
    _width = 5
    _depth = 1
    _mf1m = 10
    def mass(self):
        m = float(self._length) * float(self._width) * float(self._depth) * float(self._mf1m)
        return(m)

r = Road()
r._length = 100
r._width = 2.5
r._depth = 3



print(Road.mass(r))