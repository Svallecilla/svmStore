import unittest
from src.videojuegos.adapters.inmemory.InMemoryVideojuegoRepository import InMemoryVideojuegoRepository
from src.videojuegos.domain.Videojuego import Videojuego

class TestInMemoryVideojuegoRepository(unittest.TestCase):
    
    def setUp(self):
        self.repository = InMemoryVideojuegoRepository()
    
    def test_guardar_videojuego(self):
        videojuego = Videojuego(id=None, nombre='Zelda', consola='Switch', cantidad=10)
        self.repository.guardar(videojuego)
        result = self.repository.buscar_por_id(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.nombre, 'Zelda')
        self.assertEqual(result.consola, 'Switch')
        self.assertEqual(result.cantidad, 10)
    
    def test_buscar_por_id_no_existe(self):
        with self.assertRaises(ValueError) as context:
            self.repository.buscar_por_id(999)
        print(context.exception)
    
    def test_actualizar_videojuego(self):
        videojuego = Videojuego(id=None, nombre='Mario', consola='Switch', cantidad=5)
        self.repository.guardar(videojuego)
        videojuego.nombre = 'Mario Kart'
        self.repository.actualizar(videojuego)
        result = self.repository.buscar_por_id(1)
        self.assertEqual(result.nombre, 'Mario Kart')
    
    def test_actualizar_videojuego_no_existe(self):
        videojuego = Videojuego(id=999, nombre='Need For Speed', consola='Switch', cantidad=0)
        with self.assertRaises(ValueError) as context:
            self.repository.actualizar(videojuego)
        print(context.exception)
    
    def test_eliminar_videojuego(self):
        videojuego = Videojuego(id=None, nombre='Metroid', consola='Switch', cantidad=3)
        self.repository.guardar(videojuego)
        self.repository.eliminar(1)
        with self.assertRaises(ValueError) as context:
            self.repository.buscar_por_id(1)
        print(context.exception)
    
    def test_eliminar_videojuego_no_existe(self):
        with self.assertRaises(ValueError) as context:
            self.repository.eliminar(999)
        print(context.exception) 
