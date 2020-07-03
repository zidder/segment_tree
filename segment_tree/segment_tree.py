from _segment_tree import ST

class SegmentTree:
    def __init__(self, min, max):
        self.ind = 0
        self.st = self._create(min, max)

    def update(self, l, r, val):
        self.st.update(l, r, val, self.ind)
        self.ind += 1

    def query(self, x):
        return self.st.query(x)[0]

    def _update(obj, val, ind):
        obj._val = val
        obj._updind = ind

    def _query(obj):
        return obj._val, obj._updind

    @classmethod
    def _create(self, l, r):
        return ST(l, r, self._update, self._query,
                  additional_keys=['_val', '_updind'])



class SegmentTree2D:
    def __init__(self, minx, maxx, miny, maxy):
        self.ind = 0
        self.st = ST(minx, maxx, self._update, self._query,
                     additional_keys=['_val'])
        self.miny = miny
        self.maxy = maxy

    def update(self, l, r, b, t, val):
        self.st.update(l, r, [b, t, val], self.ind)
        self.ind += 1

    def query(self, x, y):
        return self.st.query(x, y)[0]

    def _update(self, obj, val, ind):
        b, t, val = val
        if obj._val is None:
            obj._val = SegmentTree._create(self.miny, self.maxy)
        obj._val.update(b, t, val, ind)

    def _query(self, obj, y):
        if obj._val is None:
            return None, None
        return obj._val.query(y)
