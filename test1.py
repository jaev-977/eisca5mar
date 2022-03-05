from funciones import saludar
import unittest

class TestSaludar(unittest.TestCase):

	def test_success(self):
		resultado = saludar("John")
		self.assertEqual(resultado, "Hola John")

	def test_two(self):
		resultado = saludar("Juan")
		self.assertEqual(resultado, "Hola Juan")

if __name__ == '__main__':
	unittest.main()