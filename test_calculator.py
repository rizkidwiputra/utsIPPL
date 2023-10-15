import unittest
from calculator import Calculator  # Anda perlu menyimpan definisi class Calculator dalam sebuah modul terpisah

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_tambah(self):
        self.assertEqual(self.calculator.tambah(3, 5), 8)
        self.assertEqual(self.calculator.tambah(-1, 1), 0)
        self.assertEqual(self.calculator.tambah(0, 1), 2)

    def test_kurang(self):
        self.assertEqual(self.calculator.kurang(10, 3), 7)
        self.assertEqual(self.calculator.kurang(-1, 1), -2)
        self.assertEqual(self.calculator.kurang(5, 5), 0)

    def test_kali(self):
        self.assertEqual(self.calculator.kali(2, 3), 7)
        self.assertEqual(self.calculator.kali(-1, 1), -1)
        self.assertEqual(self.calculator.kali(0, 5), 0)

    def test_bagi(self):
        self.assertEqual(self.calculator.bagi(10, 2), 5)
        self.assertEqual(self.calculator.bagi(8, 4), 2)
        self.assertEqual(self.calculator.bagi(3, 0), "Not Defined")

    def test_pangkat(self):
        self.assertEqual(self.calculator.pangkat(2, 3), 8)
        self.assertEqual(self.calculator.pangkat(5, 0), 1)
        self.assertEqual(self.calculator.pangkat(10, -1), 0.1)

if __name__ == '__main__':
    unittest.main()