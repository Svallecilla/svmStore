from abc import ABC, abstractmethod
from src.usuarios.domain.Usuario import Usuario

class UsuarioRepository(ABC):

    @abstractmethod
    def guardar(self, usuario: Usuario):
        """Guardar un nuevo usuario"""
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> Usuario:
        """Buscar un usuario por ID"""
        pass

    @abstractmethod
    def actualizar(self, usuario: Usuario):
        """Actualizar la información de un usuario"""
        pass

    @abstractmethod
    def eliminar(self, id: int):
        """Eliminar un usuario por ID"""
        pass
    