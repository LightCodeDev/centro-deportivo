# Centro Deportivo CLI

Aplicación de línea de comandos en Python que calcula el precio final de un servicio de un centro deportivo según si el cliente es miembro, su edad y si la membresía está activa.

Este proyecto forma parte de mi portafolio de aprendizaje en backend y fue desarrollado para practicar arquitectura modular en Python.

--------------------------------------------------

🇺🇸 ENGLISH

PROJECT OVERVIEW

Centro Deportivo is a simple command-line Python application that calculates the final price for a sports center service.

The system determines the final price based on:

- Whether the client is a member
- The member's age
- Whether the membership is active

The project was built to practice modular architecture and separation of responsibilities in Python.

--------------------------------------------------

FEATURES

- Member lookup by ID
- Age-based discount calculation
- Validation of active memberships
- Modular Python structure
- CLI interaction

--------------------------------------------------

PROJECT STRUCTURE

centro_deportivo

src
- main.py
- services.py
- ui.py
- data.py

docs
- flujo_centro_deportivo_v1.txt
- orden_programacion_centro_deportivo_v1.txt

README.md
.gitignore

--------------------------------------------------

HOW TO RUN

Clone the repository

git clone https://github.com/LightCodeDev/centro-deportivo.git

Enter the project folder

cd centro-deportivo

Run the program

python src/main.py

--------------------------------------------------

EXAMPLE USAGE

Eres miembro? si/no
si

Cual es su ID de miembro?
A001

Cliente encontrado: Juan Perez
Precio final: $16.00

--------------------------------------------------

WHAT I PRACTICED

- Separation of responsibilities
- Modular project structure
- CLI interaction
- Basic business logic organization
- Clean project architecture

--------------------------------------------------

🇪🇸 ESPAÑOL

DESCRIPCIÓN DEL PROYECTO

Centro Deportivo es una aplicación de línea de comandos en Python que calcula el precio final de un servicio de un centro deportivo.

El sistema determina el precio final basado en:

- Si el cliente es miembro
- La edad del miembro
- Si la membresía está activa

Este proyecto fue creado como parte de mi portafolio de aprendizaje en backend.

--------------------------------------------------

CARACTERÍSTICAS

- Búsqueda de miembros por ID
- Cálculo de descuentos por edad
- Validación de membresías activas
- Arquitectura modular en Python
- Interacción mediante línea de comandos

--------------------------------------------------

CÓMO EJECUTARLO

Clonar el repositorio

git clone https://github.com/LightCodeDev/centro-deportivo.git

Entrar a la carpeta del proyecto

cd centro-deportivo

Ejecutar el programa

python src/main.py

--------------------------------------------------

EJEMPLO DE USO

Eres miembro? si/no
si

Cual es su ID de miembro?
A001

Cliente encontrado: Juan Perez
Precio final: $16.00

--------------------------------------------------

CONCEPTOS PRACTICADOS

- Separación de responsabilidades
- Arquitectura modular
- Organización de lógica de negocio
- Interacción CLI en Python

--------------------------------------------------

POSIBLES MEJORAS FUTURAS

- Validaciones más robustas
- Integración con base de datos
- Conversión a API
- Sistema de autenticación