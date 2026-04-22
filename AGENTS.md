# AGENTS.md

## Proyecto
Este repositorio contiene una aplicación web construida con Django y PostgreSQL.

## Stack
- Python 3.12
- Django
- PostgreSQL
- Tailwind CSS

## Objetivo
Construir una app mantenible, clara y escalable, con frontend basado en templates.

## Comandos principales
- `python -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

## Convenciones de código
- Seguir PEP 8.
- Nombres descriptivos en inglés.
- Preferir funciones y clases pequeñas.
- Reutilizar componentes y utilidades existentes.
- Evitar lógica duplicada.

## Base de datos
- Usar variables de entorno para configuración.
- No escribir credenciales en el código.
- No alterar migraciones antiguas sin revisión.

## Frontend
- Usar templates de Django.
- Mantener estilos consistentes.
- Priorizar accesibilidad básica.
- Evitar JavaScript innecesario.

## Restricciones
- No agregar dependencias nuevas sin justificarlo.
- No renombrar archivos masivamente sin necesidad.
- No tocar configuraciones sensibles sin explicarlo.

## Forma de trabajo
- Hacer cambios pequeños y fáciles de revisar.
- Explicar decisiones técnicas importantes.
- Mantener compatibilidad con la estructura actual.