import unittest
import euler

class ToolTests(unittest.TestCase):
    def test_mult(self):
        self.assertEqual(euler.mult([4,8,7,2]), 448)
        self.assertEqual(euler.mult((4,8,7,2)), 448)
        self.assertEqual(euler.mult([4.7,8.2,7.9,2.1]), 448)
        self.assertEqual(euler.mult(True), 0)
        self.assertEqual(euler.mult(3), 3)
        self.assertEqual(euler.mult(3.4), 3.4)

    def test_fact(self):
        self.assertEqual(euler.fact(5), 120)
        self.assertEqual(euler.fact(87), 2107757298379527717213600518699389595229783738061356212322972511214654115727593174080683423236414793504734471782400000000000000000000)
        self.assertEqual(euler.fact(1.5), 1.329340388179137)
        self.assertEqual(euler.fact([1,2,3]), 0)
        self.assertEqual(euler.fact((1,2,3)), 0)
        self.assertEqual(euler.fact(True), 0)
        self.assertEqual(euler.fact('1.5'), 1.329340388179137)
        self.assertEqual(euler.fact('5'), 120)
        self.assertEqual(euler.fact('t'), 0)
        self.assertEqual(euler.fact('t.e'), 0)

    def test_string_sort(self):
        self.assertEqual(euler.string_sort('Tess'), 'Tess')
        self.assertEqual(euler.string_sort('Dovah'), 'Dahov')
        self.assertEqual(euler.string_sort('abcABC123'), '123ABCabc')
        self.assertEqual(euler.string_sort(5), 0)

    def test_n_pandigital(self):
        self.assertEqual(euler.n_pandigital('132', 3), True)
        self.assertEqual(euler.n_pandigital('132', 3.0), True)
        self.assertEqual(euler.n_pandigital('14523'), True)
        self.assertEqual(euler.n_pandigital('14523', 6), False)
        self.assertEqual(euler.n_pandigital('1234567890'), False)
        self.assertEqual(euler.n_pandigital('12p345'), False)


if __name__ == '__main__':
    unittest.main()
