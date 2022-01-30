import LibEspacioVectorial as lev
import unittest

class TestCplxOperations (unittest.TestCase):
    def testTranspuestaMatr (self):
        matriz = [[(1, 0), (2, 0), (3, 0)], [(4, 0), (5, 0), (6, 0)]]
        vector = [[(1, 0)], [(2, 0)], [(3, 0)]]
        transpuesta = lev.transpuesta(matriz)
        self.assertAlmostEqual(transpuesta, [[(1, 0), (4, 0)], [(2, 0), (5, 0)], [(3, 0), (6, 0)]])
        transpuesta2 = lev.transpuesta(vector)
        self.assertAlmostEqual(transpuesta2, [[(1, 0), (2, 0), (3, 0)]])

if __name__ == '__main__':
    unittest.main()