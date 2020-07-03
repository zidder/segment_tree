class ST:
    def __init__(self, l, r, _update, _query, additional_keys=None):
        self.l = l
        self.r = r
        self.m = (l + r) // 2
        self.left = None
        self.right = None
        self._update = _update
        self._query = _query
        self.additional_keys = additional_keys
        if additional_keys is not None:
            for key in additional_keys:
                setattr(self, key, None)

    def update(self, l, r, val, ind):
        if r <= self.l or l >= self.r:
            return
        if self.l >= l and self.r <= r:
            self._update(self, val, ind)
            return
        if l < self.m:
            if self.left is None:
                self.left = self._create(self.l, self.m)
            self.left.update(l, r, val, ind)
        if r > self.m:
            if self.right is None:
                self.right = self._create(self.m, self.r)
            self.right.update(l, r, val, ind)

    def query(self, x, *args, **kwargs):
        assert self.l <= x < self.r
        if x < self.m and self.left is not None:
            v, ind = self.left.query(x, *args, **kwargs)
        elif x >= self.m and self.right is not None:
            v, ind = self.right.query(x, *args, **kwargs)
        else:
            v, ind = None, None
        val, vind = self._query(self, *args, **kwargs)
        if val is None and v is None:
            return None, None
        if v is None:
            return val, vind
        if val is None:
            return v, ind
        if vind > ind:
            return val, vind
        return v, ind

    def _create(self, l, r):
        return ST(l, r, self._update, self._query,
                  additional_keys=self.additional_keys)
