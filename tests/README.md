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
- Ejecutar contenedores
```
docker compose -f .\docker-compose.dev.yml up
```

# 4. Ejecutar tests
- Entrar al directorio tests
```
cd tests
```
- Resetar la BD
```
python3 reset_bd.py
```
- Agregar data inicial a la 
```
python3 populate_bd.py
```
## 4.1 Backend tests
- Entrar al directorio backend/doctor
```
cd backend/doctor
```
- Ejecutar tests
```
robot .
```
- Si quieres ejecutar el test nuevamente o ejecutar otro test, es necesario resetear la BD y cargar los datos iniciales nuevamente (paso 4).

## 4.2 System tests
- Entrar al directorio system
```
cd system
```
- Ejecutar tests
```
robot .
```
- Si quieres ejecutar el test nuevamente o ejecutar otro test, es necesario resetear la BD y cargar los datos iniciales nuevamente (paso 4).
