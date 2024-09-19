import unittest
from unittest.mock import MagicMock
from assertpy import assert_that
from src.usuarios.domain.Usuario import Usuario
from src.usuarios.ports.UsuarioRepository import UsuarioRepository
from src.usuarios.services.usuarioService import UsuarioService

class TestUsuarioService(unittest.TestCase):
    def setUp(self):

        self.repository = MagicMock(spec=UsuarioRepository)
        self.service = UsuarioService(self.repository)

    def test_crear_usuario_exitoso(self):

        nuevo_usuario = Usuario(id=1, nombre='Juan', apellido='Pérez')
        self.repository.guardar.return_value = None  
        self.repository.buscar_por_id.return_value = nuevo_usuario  
        usuario = self.service.crear_usuario('Juan', 'Pérez')

        assert_that(usuario).is_not_none()
        assert_that(usuario.nombre).is_equal_to('Juan')
        assert_that(usuario.apellido).is_equal_to('Pérez')

        self.repository.guardar.assert_called_once_with(usuario)

    def test_crear_usuario_datos_invalidos(self):
        with self.assertRaises(ValueError):
            self.service.crear_usuario('', 'Pérez')

        with self.assertRaises(ValueError):
            self.service.crear_usuario('Juan', '')

    def test_obtener_usuario_exitoso(self):
        usuario = Usuario(id=1, nombre='Ana', apellido='García')
        self.repository.buscar_por_id.return_value = usuario

        usuario_obtenido = self.service.obtener_usuario(1)

        assert_that(usuario_obtenido.nombre).is_equal_to('Ana')
        assert_that(usuario_obtenido.apellido).is_equal_to('García')

    def test_obtener_usuario_no_existe(self):
        self.repository.buscar_por_id.return_value = None

        with self.assertRaises(ValueError):
            self.service.obtener_usuario(999)

    def test_actualizar_usuario_exitoso(self):
        usuario = Usuario(id=1, nombre='Luis', apellido='Martínez')
        self.repository.buscar_por_id.return_value = usuario
        self.repository.actualizar.return_value = None

        usuario.nombre = 'Luis Alberto'
        self.service.actualizar_usuario(usuario)

        assert_that(usuario.nombre).is_equal_to('Luis Alberto')
        self.repository.actualizar.assert_called_once_with(usuario)

    def test_actualizar_usuario_no_existe(self):
        usuario = Usuario(id=999, nombre='No', apellido='Existe')
        self.repository.buscar_por_id.return_value = None

        with self.assertRaises(ValueError):
            self.service.actualizar_usuario(usuario)

    def test_eliminar_usuario_exitoso(self):
        usuario = Usuario(id=1, nombre='Carlos', apellido='Sánchez')
        self.repository.buscar_por_id.return_value = usuario
        self.repository.eliminar.return_value = None

        self.service.eliminar_usuario(1)
        self.repository.eliminar.assert_called_once_with(1)

    def test_eliminar_usuario_no_existe(self):
        self.repository.buscar_por_id.return_value = None

        with self.assertRaises(ValueError):
            self.service.eliminar_usuario(999)

