# Instalación
## Opción 1: Docker
### Requerimientos
- Docker
### Pasos para la instalación
- Clonar el repositorio
```
git clone https://github.com/proyecto-pruebas-sw/proyecto-pruebas-sw
```
- Entrar al repositorio clonado
```
cd proyecto-pruebas-sw
```
- Ejecutar contenedores
```
docker compose -f .\docker-compose.dev.yml up
```
- URL Frontend: [http://localhost:3000/](http://localhost:3000/)
- URL Backend: [http://localhost:8000/](http://localhost:8000/)