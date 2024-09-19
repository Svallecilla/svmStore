import unittest
from src.videojuegos.domain.Videojuego import Videojuego
from src.videojuegos.adapters.inmemory.InMemoryVideojuegoRepository import InMemoryVideojuegoRepository
from src.videojuegos.services.videojuegoService import VideojuegoService

class TestVideojuegoService(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryVideojuegoRepository()
        self.service = VideojuegoService(self.repository)

    def test_crear_videojuego(self):
        videojuego = self.service.crear_videojuego('Zelda', 'Switch', 10)
        self.assertIsNotNone(videojuego)
        self.assertEqual(videojuego.nombre, 'Zelda')
        self.assertEqual(videojuego.consola, 'Switch')
        self.assertEqual(videojuego.cantidad, 10)
        
        result = self.repository.buscar_por_id(videojuego.id)
        self.assertIsNotNone(result)
        self.assertEqual(result.nombre, 'Zelda')
        self.assertEqual(result.consola, 'Switch')
        self.assertEqual(result.cantidad, 10)

    def test_obtener_videojuego(self):
        self.service.crear_videojuego('Mario', 'Switch', 5)
        videojuego = self.service.obtener_videojuego(1)
        self.assertIsNotNone(videojuego)
        self.assertEqual(videojuego.nombre, 'Mario')

    def test_actualizar_videojuego(self):
        videojuego = self.service.crear_videojuego('Metroid', 'Switch', 2)
        videojuego.cantidad = 3
        self.service.actualizar_videojuego(videojuego)
        result = self.repository.buscar_por_id(videojuego.id)
        self.assertEqual(result.cantidad, 3)

    def test_eliminar_videojuego(self):
        self.service.crear_videojuego('Splatoon', 'Switch', 20)
        self.service.eliminar_videojuego(1)
        with self.assertRaises(ValueError):
            self.repository.buscar_por_id(1)

    def test_crear_videojuego_invalido(self):
        with self.assertRaises(ValueError):
            self.service.crear_videojuego('', 'PS5', -1)

    def test_obtener_videojuego_no_existe(self):
        with self.assertRaises(ValueError):
            self.service.obtener_videojuego(999)

    def test_actualizar_videojuego_no_existe(self):
        videojuego = Videojuego(id=999, nombre='No Existe', consola='PS5', cantidad=1)
        with self.assertRaises(ValueError):
            self.service.actualizar_videojuego(videojuego)

    def test_eliminar_videojuego_no_existe(self):
        with self.assertRaises(ValueError):
            self.service.eliminar_videojuego(999)

