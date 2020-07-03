from unittest import TestCase

from segment_tree import SegmentTree
from segment_tree import SegmentTree2D

import numpy as np

class SegmentTreeTest(TestCase):
    def test_stress(self):
        n = 1000
        epochs = 100
        arr = np.zeros(n)
        tree = SegmentTree(0, n)
        tree.update(0, n, 0)
        for i in range(epochs):
            l, r = np.random.randint(0, n, 2)
            l, r = sorted([l, r])
            r += 1
            val = np.random.random()
            tree.update(l, r, val)
            arr[l: r] = val
            for i in range(n):
                self.assertEqual(arr[i], tree.query(i))

class SegmentTree2DTest(TestCase):
    def test_stress(self):
        n = 100
        epochs = 100
        arr = np.zeros((n, n))
        tree = SegmentTree2D(0, n, 0, n)
        tree.update(0, n, 0, n, 0)
        for i in range(epochs):
            l, r, b, t = np.random.randint(0, n, 4)
            l, r = sorted([l, r])
            b, t = sorted([b, t])
            r += 1
            t += 1
            val = np.random.random()
            tree.update(l, r, b, t, val)
            arr[l: r, b: t] = val
            for x in range(n):
                for y in range(n):
                    self.assertEqual(arr[x, y], tree.query(x, y))
