from abc import ABC, abstractmethod
from src.videojuegos.domain.Videojuego import Videojuego

class VideojuegoRepository(ABC):
    
    @abstractmethod
    def guardar(self, videojuego: Videojuego):
        """Guardar un nuevo videojuego"""
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> Videojuego:
        """Buscar un videojuego por ID"""
        pass
    
    @abstractmethod
    def actualizar(self, videojuego: Videojuego):
        """Actualizar la información de un videojuego"""
        pass
    
    @abstractmethod
    def eliminar(self, id: int):
        """Eliminar un videojuego por ID"""
        pass
