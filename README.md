# SVMStore

SVMStore es una tienda de videojuegos desarrollada utilizando arquitectura hexagonal con vertical slicing en Python. Este proyecto demuestra la implementación de servicios para manejar usuarios y videojuegos, con almacenamiento en memoria para pruebas.

## Estructura del Proyecto

- **src/**: Contiene el código fuente de la aplicación.
  - **usuarios/**: Módulo para la gestión de usuarios.
    - **domain/**: Definiciones de dominio para usuarios.
    - **ports/**: Interfaces de repositorio para usuarios.
    - **adapters/**: Implementaciones de repositorio en memoria para usuarios.
    - **services/**: Lógica del negocio para usuarios.
  - **videojuegos/**: Módulo para la gestión de videojuegos.
    - **domain/**: Definiciones de dominio para videojuegos.
    - **ports/**: Interfaces de repositorio para videojuegos.
    - **adapters/**: Implementaciones de repositorio en memoria para videojuegos.
    - **services/**: Lógica del negocio para videojuegos.

- **tests/**: Contiene pruebas unitarias para el proyecto.
- **.gitignore**: Archivo para ignorar archivos y carpetas no deseados en Git.
- **requirements.txt**: Lista de dependencias del proyecto.
- **README.md**: Este archivo.

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone <url-del-repositorio>
   cd svmStore

2. **Puedes crear un entorno virtual**

    python -m venv venv
    source venv/bin/activate ***En Windows usa venv\Scripts\activate***

3. **Instalacion de requirements**
    pip install -r requirements.txt

4. **Ejecución de Pruebas**
    ***Para ejecutar las pruebas y verificar la cobertura del código:***
    coverage run -m unittest discover -s tests
    coverage report

5. **Uso**
    Puedes interactuar con la API utilizando Postman para probar las funcionalidades de la tienda, como la creación, actualización, obtención y eliminación de usuarios y videojuegos.

6. **Cobertura de Código en Repositorios**

Las líneas con pass en los archivos src/usuarios/ports/UsuarioRepository.py y src/videojuegos/ports/VideojuegoRepository.py corresponden a métodos abstractos en clases base abstractas. Este comportamiento es normal y esperado, ya que estos métodos están destinados a ser implementados por subclases.

***Razones por las que no obtienen cobertura:***

***Métodos Abstractos:*** Los métodos abstractos no se implementan en la clase base y, por lo tanto, no pueden ser invocados ni ejecutados en las pruebas.
