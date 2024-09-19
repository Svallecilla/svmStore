from typing import Dict, Optional
from src.videojuegos.domain.Videojuego import Videojuego
from src.videojuegos.ports.VideojuegoRepository import VideojuegoRepository

class InMemoryVideojuegoRepository(VideojuegoRepository):
    def __init__(self):
        self.videojuegos: Dict[int, Videojuego] = {}
        self.next_id = 1

    def guardar(self, videojuego: Videojuego):
        if videojuego.id is None:
            videojuego.id = self.next_id
            self.next_id += 1
        self.videojuegos[videojuego.id] = videojuego

    def buscar_por_id(self, id: int) -> Optional[Videojuego]:
        videojuego = self.videojuegos.get(id)
        if videojuego is None:
            raise ValueError(f"Videojuego con ID {id} no encontrado.")
        return videojuego

    def actualizar(self, videojuego: Videojuego):
        if videojuego.id not in self.videojuegos:
            raise ValueError(f"Videojuego con ID {videojuego.id} no encontrado para actualización.")
        self.videojuegos[videojuego.id] = videojuego

    def eliminar(self, id: int):
        if id not in self.videojuegos:
            raise ValueError(f"Videojuego con ID {id} no encontrado para eliminación.")
        del self.videojuegos[id]
