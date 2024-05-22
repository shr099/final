# Explicación de proyecto

##

## Descripción
###### Este proyecto se centra en la conversión de caracteres y palabras a sus representaciones en formato binario (byte) y viceversa, utilizando un menú interactivo en Git Bash. Además, se ha documentado el proceso de desarrollo en GitHub y JIRA Software para asegurar una gestión adecuada del proyecto.

## Funcionalidades
1. Generar la representación en byte de un carácter.
2. Generar la representación en byte de una palabra.
3. Generar la representación ASCII de un byte.

## Comandos Utilizados
* 'git init': Inicializar git
* 'git remote add origin [Link]': Unir repo local con el remoto
* 'git checkout -b [rama]': Crear ramas
* 'git checkout [rama]': Cambiarse de ramas
* 'git pull origin [rama]': Bajar cambios repo nube a repo local
* 'git add .': Guardar cambios en los archivos
* 'git commit -m “[[RAMA] Mensaje]”' = Guardar cambios en la rama
* 'git push origin [rama]': Subir cambios del repo local al repo de la nube
* 'git status': Ver estado; rama en la que estoy y si hay cambios pendientes

##### MERGE
* 'git checkout [rama donde va a quedar la fusión ]'
* 'git merge [rama a fusionar]'
* 'git push origin [rama donde va a quedar la fusión]'
* '.gitignore'
* 'git log --oneline': Historial mas corto

## Ramas creadas:
1. henao (creada por Santiago Henao)
2. juan (creada por Juan Muñoz)
3. sebas (creado por Sebastian Ramirez)

## CHANGELOG
### Añadido - 2024-05-21
* Creación del repositorio inicial en GitHub.
* Configuración inicial del proyecto con un archivo README.md.
* Creación de la rama `henao` para la funcionalidad de convertir un carácter a byte.
* Implementación de la función para convertir un carácter a byte en la rama `henao`.
* Implementación de la función para convertir una palabra a bytes en la rama `henao `.
* Creación de la rama `sebas` para la funcionalidad de convertir un byte a ASCII.
* Implementación de la función para convertir un byte a ASCII en la rama `sebas`.
* Implementación del menú de opciones en la rama `main`.

### Añadido - 2024-05-22
* Actualización del archivo .gitignore para incluir exclusiones específicas del proyecto.
* Exclusión del archivo prueba.py
* Actualización del archivo README.md con la información de los integrantes del grupo y los comandos utilizados en Git.
* Pull request a la actualización del archivo README.md
* Creación y documentación de Historias de Usuario en JIRA Software.


## Integrantes del proyecto:
|    Nombre               |  Usuario GitHub |
| ----------------------- |:---------------:|
| **Santiago Henao**      | shr099          |
| **Juan Fernando Muñoz** | juanferm0410    |
| **Sebastian Ramírez**   | JSeb22          |
