from src.usuarios.domain.Usuario import Usuario
from src.usuarios.ports.UsuarioRepository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def crear_usuario(self, nombre: str, apellido: str) -> Usuario:
        if not nombre or not apellido:
            raise ValueError("El nombre y el apellido no pueden estar vacíos.")
        nuevo_usuario = Usuario(id=None, nombre=nombre, apellido=apellido)
        self.repository.guardar(nuevo_usuario)
        return nuevo_usuario

    def obtener_usuario(self, id: int) -> Usuario:
        usuario = self.repository.buscar_por_id(id)
        if usuario is None:
            raise ValueError("No se encuentra usuario.")
        return usuario

    def actualizar_usuario(self, usuario: Usuario):
        usuario_existente = self.repository.buscar_por_id(usuario.id)
        if usuario_existente is None:
            raise ValueError("Usuario no encontrado.")
        self.repository.actualizar(usuario)

    def eliminar_usuario(self, id: int):
        usuario_existente = self.repository.buscar_por_id(id)
        if usuario_existente is None:
            raise ValueError("Usuario no encontrado.")
        self.repository.eliminar(id)

