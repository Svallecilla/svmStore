from typing import Dict, Optional
from src.usuarios.domain.Usuario import Usuario
from src.usuarios.ports.UsuarioRepository import UsuarioRepository

class InMemoryUsuarioRepository(UsuarioRepository):
    def __init__(self):
        self.usuarios: Dict[int, Usuario] = {}
        self.next_id = 1

    def guardar(self, usuario: Usuario):
        if usuario.id is None:
            usuario.id = self.next_id
            self.next_id += 1
        self.usuarios[usuario.id] = usuario

    def buscar_por_id(self, id: int) -> Optional[Usuario]:
        usuario = self.usuarios.get(id)
        if usuario is None:
            raise ValueError(f"Usuario con ID {id} no encontrado.")
        return usuario

    def actualizar(self, usuario: Usuario):
        if usuario.id not in self.usuarios:
            raise ValueError(f"Usuario con ID {usuario.id} no encontrado para actualización.")
        self.usuarios[usuario.id] = usuario

    def eliminar(self, id: int):
        if id not in self.usuarios:
            raise ValueError(f"Usuario con ID {id} no encontrado para eliminación.")
        del self.usuarios[id]
