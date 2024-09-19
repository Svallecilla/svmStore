import unittest
from src.usuarios.domain.Usuario import Usuario
from src.usuarios.adapters.inmemory.InMemoryUsuarioRepository import InMemoryUsuarioRepository

class TestInMemoryUsuarioRepository(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryUsuarioRepository()

    def test_guardar_usuario(self):
        usuario = Usuario(id=None, nombre='Juan', apellido='Pérez')
        self.repository.guardar(usuario)
        result = self.repository.buscar_por_id(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.nombre, 'Juan')
        self.assertEqual(result.apellido, 'Pérez')

    def test_buscar_usuario_por_id(self):
        usuario = Usuario(id=1, nombre='Ana', apellido='García')
        self.repository.guardar(usuario)
        result = self.repository.buscar_por_id(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.nombre, 'Ana')

    def test_actualizar_usuario(self):
        usuario = Usuario(id=1, nombre='Luis', apellido='Martínez')
        self.repository.guardar(usuario)
        usuario.nombre = 'Luis Alberto'
        self.repository.actualizar(usuario)
        result = self.repository.buscar_por_id(1)
        self.assertEqual(result.nombre, 'Luis Alberto')

    def test_actualizar_usuario_no_existe(self):
        usuario_no_existente = Usuario(id=999, nombre='No Existente', apellido='Usuario')
        try:
            self.repository.actualizar(usuario_no_existente)
        except ValueError as e:
            print(e)  # Imprime la excepción
            self.assertIsInstance(e, ValueError)

    def test_eliminar_usuario(self):
        usuario = Usuario(id=None, nombre='Carlos', apellido='Sánchez')
        self.repository.guardar(usuario)  # Guarda el usuario primero
        self.repository.eliminar(1)  # Elimina el usuario
        with self.assertRaises(ValueError) as context:
            self.repository.buscar_por_id(1)
        print(context.exception)  # Imprime la excepción

    def test_eliminar_usuario_no_existe(self):
        with self.assertRaises(ValueError) as context:
            self.repository.eliminar(999)
        print(context.exception)  # Imprime la excepción
