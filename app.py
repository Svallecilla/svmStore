from flask import Flask, request, jsonify
from src.usuarios.services.usuarioService import UsuarioService
from src.videojuegos.services.videojuegoService import VideojuegoService
from src.usuarios.adapters.inmemory.InMemoryUsuarioRepository import InMemoryUsuarioRepository
from src.videojuegos.adapters.inmemory.InMemoryVideojuegoRepository import InMemoryVideojuegoRepository

app = Flask(__name__)

usuario_repository = InMemoryUsuarioRepository()
videojuego_repository = InMemoryVideojuegoRepository()

usuario_service = UsuarioService(usuario_repository)
videojuego_service = VideojuegoService(videojuego_repository)

# Rutas para Usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    try:
        usuario = usuario_service.crear_usuario(data['nombre'], data['apellido'])
        return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'apellido': usuario.apellido}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    try:
        usuario = usuario_service.obtener_usuario(id)
        return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'apellido': usuario.apellido})
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    usuario = usuario(id=id, nombre=data['nombre'], apellido=data['apellido'])
    try:
        usuario_service.actualizar_usuario(usuario)
        return '', 204
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    try:
        usuario_service.eliminar_usuario(id)
        return '', 204
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

# Rutas para Videojuego
@app.route('/videojuegos', methods=['POST'])
def crear_videojuego():
    data = request.json
    try:
        videojuego = videojuego_service.crear_videojuego(data['nombre'], data['consola'], data['cantidad'])
        return jsonify({'id': videojuego.id, 'nombre': videojuego.nombre, 'consola': videojuego.consola, 'cantidad': videojuego.cantidad}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/videojuegos/<int:id>', methods=['GET'])
def obtener_videojuego(id):
    try:
        videojuego = videojuego_service.obtener_videojuego(id)
        return jsonify({'id': videojuego.id, 'nombre': videojuego.nombre, 'consola': videojuego.consola, 'cantidad': videojuego.cantidad})
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/videojuegos/<int:id>', methods=['PUT'])
def actualizar_videojuego(id):
    data = request.json
    videojuego = videojuego(id=id, nombre=data['nombre'], consola=data['consola'], cantidad=data['cantidad'])
    try:
        videojuego_service.actualizar_videojuego(videojuego)
        return '', 204
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/videojuegos/<int:id>', methods=['DELETE'])
def eliminar_videojuego(id):
    try:
        videojuego_service.eliminar_videojuego(id)
        return '', 204
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
