# Instalación
## Opción 1: Docker
### Requerimientos
- Docker
### Pasos para la instalación
- Clonar el repositorio
```
git clone https://github.com/nanonacho/proyecto-pruebas-sw
```
- Entrar al repositorio clonado
```
cd proyecto-pruebas-sw
```
- Ejecutar contenedores
```
docker compose -f .\docker-compose.dev.yml up
```

## Opción 2:
### Requerimientos
- Python 3.11.9
- Node 20.12.2
### Pasos para la instalación
- Clonar el repositorio
```
git clone https://github.com/nanonacho/proyecto-pruebas-sw
```
- Entrar al repositorio clonado
```
cd proyecto-pruebas-sw
```

#### Backend
- Entrar a la carpeta backend
```
cd services/backend
```
- Crear un entorno virtual
```
python3 -m venv env
```
- Activar entorno virtual
```
source env/bin/activate
```
- Instalar dependecias
```
pip3 install -r requirements.txt
```
- Ejecutar servidor
```
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
- Entrar a la carpeta frontend
```
cd frontend
```
- Instalar dependencias
```
npm install
```
- Ejecutar servidor
```
npm run dev
```