from src.videojuegos.domain.Videojuego import Videojuego
from src.videojuegos.ports.VideojuegoRepository import VideojuegoRepository

class VideojuegoService:
    def __init__(self, repository: VideojuegoRepository):
        self.repository = repository

    def crear_videojuego(self, nombre: str, consola: str, cantidad: int) -> Videojuego:
        if not nombre or not consola or cantidad < 0:
            raise ValueError("Los datos del videojuego no son válidos.")
        nuevo_videojuego = Videojuego(id=None, nombre=nombre, consola=consola, cantidad=cantidad)
        self.repository.guardar(nuevo_videojuego)
        return nuevo_videojuego

    def obtener_videojuego(self, id: int) -> Videojuego:
        try:
            return self.repository.buscar_por_id(id)
        except ValueError:
            raise ValueError("Videojuego no encontrado.")

    def actualizar_videojuego(self, videojuego: Videojuego):
        self.repository.actualizar(videojuego)

    def eliminar_videojuego(self, id: int):
        self.repository.eliminar(id)

