'''
Pruebas Libreria CNYT
Operaciones con Vectores y Matrices
Andrea Durán Vivas
'''

import LibEspacioVectorial as lev
import unittest

class TestCplxOperations (unittest.TestCase):
    def testSumavec (self):
        suma = lev.sumavec([(0,3), (0,0), (2,8)], [(1,1), (2,1), (0,1)])
        self.assertAlmostEqual(suma, [(1,4), (2,1), (2,9)])

        suma2 = lev.sumavec([(5, -3), (8, 9), (4, -8), (0, -3)], [(20, 2), (0, 7), (6, 0), (0, 0)])
        self.assertAlmostEqual(suma2, [(25, -1), (8, 16), (10, -8), (0, -3)])

    def testRestavec (self):
        resta = lev.restavec([(0, 3), (0, 0), (2, 8)], [(1, 1), (2, 1), (0, 1)])
        self.assertAlmostEqual(resta, [(-1, 2), (-2, -1), (2, 7)])

        resta2 = lev.restavec([(5, -3), (8, 9), (4, -8), (0, -3)], [(20, 2), (0, 7), (6, 0), (0, 0)])
        self.assertAlmostEqual(resta2, [(-15, -5), (8, 2), (-2, -8), (0, -3)])

    def testInversovec (self):
        inverso = lev.inverso([(0,3), (0,0), (2,8)])
        self.assertAlmostEqual(inverso, [(0, -3), (0, 0), (-2, -8)])

        inverso2 = lev.inverso([(5, -3), (8, 9), (4, -8), (0, -3)])
        self.assertAlmostEqual(inverso2, [(-5, 3), (-8, -9), (-4, 8), (0, 3)])

    def testMultEscalvec (self):
        mult = lev.multiplicacionEscalar((1,2), [(0,3), (0,0), (2,8)])
        self.assertAlmostEqual(mult, [(-6, 3), (0, 0), (-14, 12)])

        mult2 = lev.multiplicacionEscalar((3,2),[(6,3),(0,0),(5,1),(4,0)])
        self.assertAlmostEqual(mult2, [(12,21),(0,0),(13,13),(12,8)])

    def testSumaMatr (self):
        suma = lev.sumaMatrices([[(0,2), (0,1)], [(1,2), (2,4)]], [[(1,0), (1,1)], [(8,0), (0,0)]])
        self.assertAlmostEqual(suma, [[(1, 2), (1, 2)], [(9, 2), (2, 4)]])

        suma2 = lev.sumaMatrices([[(-5,8),(10,9),(0,0)],[(2,7),(-14,8),(9,6)],[(-6,0),(3,6),(8,9)]],
                                 [[(-8,4),(3,7),(4,9)],[(-9,1),(7,2),(-5,3)],[(15,0),(-3,5),(0,7)]])
        self.assertAlmostEqual(suma2,
                               [[(-13,12),(13,16),(4,9)],[(-7,8),(-7,10),(4,9)],[(9,0),(0,11),(8,16)]])

    def testRestaMatr (self):
        resta = lev.restaMatrices([[(0, 2), (0, 1)], [(1, 2), (2, 4)]], [[(1, 0), (1, 1)], [(8, 0), (0, 0)]])
        self.assertAlmostEqual(resta, [[(-1, 2), (-1, 0)], [(-7, 2), (2, 4)]])

        resta2 = lev.restaMatrices([[(-5,8),(10,9),(0,0)],[(2,7),(-14,8),(9,6)],[(-6,0),(3,6),(8,9)]],
                                 [[(-8,4),(3,7),(4,9)],[(-9,1),(7,2),(-5,3)],[(15,0),(-3,5),(0,7)]])
        self.assertAlmostEqual(resta2,
                               [[(3, 4), (7, 2), (-4, -9)], [(11, 6), (-21, 6), (14, 3)], [(-21, 0), (6, 1), (8, 2)]])

    def testInversoMatr (self):
        inverso = lev.inversoMatrices([[(0,2), (0,1)], [(1,2), (2,4)]])
        self.assertAlmostEqual(inverso, [[(0, -2), (0, -1)], [(-1, -2), (-2, -4)]])

        inverso2 = lev.inversoMatrices([[(-5,0),(10,0),(0,0)],[(2,0),(-14,0),(9,0)],[(-6,0),(3,0),(8,0)]])
        self.assertAlmostEqual(inverso2,
                               [[(5, 0), (-10, 0), (0, 0)], [(-2, 0), (14, 0), (-9, 0)], [(6, 0), (-3, 0), (-8, 0)]])

    def testMultEscMatr (self):
        mult = lev.multEscalarMatrices((1,2), [[(0,3), (0,0), (2,8)], [(0,3), (0,0), (2,8)]])
        self.assertAlmostEqual(mult, [[(-6, 3), (0, 0), (-14, 12)], [(-6, 3), (0, 0), (-14, 12)]])

        mult2 = lev.multEscalarMatrices((3, 0),
                                        [[(-5, 8), (10, 9), (0, 0)], [(2, 7), (-14, 8), (9, 6)],[(-6, 0), (3, 6), (8, 9)]])
        self.assertAlmostEqual(mult2,
                               [[(-15, 24), (30, 27), (0, 0)], [(6, 21), (-42, 24), (27, 18)], [(-18, 0), (9, 18), (24, 27)]])

    def testTranspuestaMatr (self):
        trans = lev.transpuesta([[(0,2), (0,1)], [(1,2), (2,4)]])
        self.assertAlmostEqual(trans, [[(0, 2), (1, 2)], [(0, 1), (2, 4)]])

        trans2 = lev.transpuesta([[(1,0)],[(2,0)],[(3,0)]])
        self.assertAlmostEqual(trans2, [[(1,0),(2,0),(3,0)]])

    def testConjugadoMatr (self):
        conj = lev.conjugadoMatVec([[(0,2), (0,1)], [(1,2), (2,4)]])
        self.assertAlmostEqual(conj, [[(0, -2), (0, -1)], [(1, -2), (2, -4)]])

        conj2 = lev.conjugadoMatVec([[(1, 1)], [(2, -1)], [(3, 7)]])
        self.assertAlmostEqual(conj2, [[(1, -1)], [(2, 1)], [(3, -7)]])

    def testAdjuntaMatr(self):
        daga = lev.adjunta([[(0,2), (0,1)], [(1,2), (2,4)]])
        self.assertAlmostEqual(daga, [[(0, -2), (1, -2)], [(0, -1), (2, -4)]])

        daga2 = lev.adjunta([[(1, -1)], [(2, 1)], [(3, -7)]])
        self.assertAlmostEqual(daga2, [[(1, 1), (2, -1), (3, 7)]])



if __name__ == '__main__':
    unittest.main()