# Directorio Médico Salud Integral
# Descripción
Directorio Médico Salud Integral es una aplicación web, la cual da a conocer los especialistas médicos del centro médico "Salud Integral" y sus respectivas áreas de especialización como también sus antecedentes (educación y experiencia). Permite que los pacientes puedan agendar citas con algún especialista médico de manera informada.

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
docker compose -f .\docker-compose.dev.yml up --build --remove-orphans
```

# Uso
## Interfaz gráfica de la aplicación
- URL: [http://localhost:3000/](http://localhost:3000/)
## API de la aplicación
- URL: [http://localhost:8000/](http://localhost:8000/)
- Documentación de la API: [https://documenter.getpostman.com/view/21303535/2sA3JDfjuu](https://documenter.getpostman.com/view/21303535/2sA3JDfjuu)

# Soporte
Si tienes dudas o necesitas ayuda contactar a: [ignacio.alvaradome@usm.cl](mailto:ignacio.alvaradome@usm.cl)

# Cómo contribuir
Cualquier forma de contribución es muy bienvenida.

## Pull Requests
En este proyecto se trabaja con GitFlow, a continuación se muestra como contribuir con un PR:

- Crear una copia del repositorio haciendo un fork.
- Clonar el fork del repositorio .
- Crear una rama a partir de la rama develop:
    - El nombre de la rama debe cumplir con la estructura "feature/< branch-name >".
- Hacer los cambios en el código.
- Hacer un commit con los cambios.
- Crear un pull request para hacer un merge hacia la rama develop del repositorio original.
- Luego de esto revisaremos tu pull request.

## Issues
Una buena forma de contribuir al proyecto es crear una issue en este repositorio con el detalle del problema o la propuesta de alguna feature nueva. 

# Licencia
MIT License

Copyright (c) [2024] [DirectorioMédico]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.