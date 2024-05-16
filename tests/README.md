# Instrucciones de para realizar testing
## 1. Crear entorno virtual de python
- Entrar al repositorio
```
cd proyecto-pruebas-sw
```
- Crear entorno virtual
```
python3 -m venv ./tests/env
```
- Activar entorno virtual
```
source ./tests/env/bin/activate
```

## 2. Instalar requerimientos
- Instalar requerimientos en requirements.txt
```
pip3 install -r ./tests/requirements.txt
```

## 3. Ejecutar aplicación
- Borrar contenedores anteriores (NECESARIO para resetear la BD)
```
docker compose -f .\docker-compose.dev.yml down
```
- Ejecutar contenedores
```
docker compose -f .\docker-compose.dev.yml up
```

## 4. Cargar datos iniciales a la BD
- Entrar al directorio tests/backend/doctor
```
cd tests/backend/doctor
```
- Ejecutar data.py
```
python3 data.py
```

## 5. Ejecutar tests
- Ejecutar el siguiente comando
```
robot .
```
- Para volver a ejecutar los test debes volver al paso 3 (Ejecutar aplicación).
