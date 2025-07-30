# Tools: oTree, Python y GIT

## Introducción a Python

<img src="https://www.python.org/static/community_logos/python-logo.png" width="200" style="border-radius: 12px; border: 1px solid #ddd"/>


### Objetivo
Comprender los fundamentos del lenguaje de programación Python, incluyendo su sintaxis básica, estructuras de control, funciones, manejo de paquetes y entornos virtuales. Esto sentará las bases para usar Python en desarrollo de experimentos, análisis de datos o automatización.

---

### ¿Qué es Python?

Python es un lenguaje de programación:
- Interpretado
- De alto nivel
- Multi-paradigma
- Con una sintaxis clara y legible

Fue creado por **Guido van Rossum** y es ampliamente utilizado en ciencia de datos, inteligencia artificial, desarrollo web y automatización.

---

### Instalación

1. Descargar Python desde: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Activar la opción **"Add Python to PATH"** al instalar.
3. Verificar la instalación:
```bash
    python --version
```

---

### Tipos de datos y variables

En Python no es necesario declarar explícitamente el tipo de una variable, ya que el lenguaje es dinámicamente tipado. Esto significa que Python detecta automáticamente el tipo de dato según el valor que se le asigna.

```python
    entero = 10          # int - Número entero
    decimal = 3.14       # float - Número decimal
    texto = "Hola"       # str - Cadena de caracteres
    bandera = True       # bool - Booleano
    lista = [1, 2, 3]    # list - Lista o arreglo (Array)
    diccionario = {"nombre": "Ana", "edad": 25}  # dict - Diccionario, es una estructura de datos que almacena pares clave-valor
```

---

### Estructuras de control

#### Condicionales

En Python, if, elif y else se usan para ejecutar bloques de código según condiciones:

- if: evalúa una condición; si es verdadera, ejecuta el bloque de código.

- elif: (abreviación de "else if") evalúa otra condición si la anterior fue falsa.

- else: se ejecuta si ninguna de las condiciones anteriores se cumple.

<img src="https://www.luisllamas.es/images/20096/programacion-condicional-doble.png" width="300" style="margin: 20px; border-radius: 12px; border: 1px"/>



```python
    if edad >= 18:
        print("Mayor de edad")
    elif edad == 17:
        print("Casi")
    else:
        print("Menor de edad")
```

#### Bucles

Los bucles permiten ejecutar un bloque de código varias veces:

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTq48RIhoz75vOXkzPcjypiOANpn3cbagbhQ&s" width="300" style="margin: 20px; border-radius: 12px; border: 1px"/>

- For loop: itera sobre una secuencia (lista, tupla, cadena, etc.). Ejecuta el bloque de código una vez por cada elemento.

```python
    for i in range(5):  # range(5) genera una secuencia de números del 0 al 4
        print(i)
```

- While loop: ejecuta mientras una condición sea verdadera.

````python
    contador = 0
    while contador < 3:
        print(contador)
        contador += 1  # Incrementa el contador en 1
````

---

### Funciones

Las funciones son bloques de código reutilizables que realizan una tarea específica. Se definen con la palabra clave `def`, seguida del nombre de la función y paréntesis.

<img src="https://naps.com.mx/blog/wp-content/uploads/2020/06/Funciones-en-Python.-Estructura-de-una-funci%C3%B3n.png" width="300" style="margin: 20px; border-radius: 12px; border: 1px"/>

```python
    def saludar(nombre):
        return f"Hola, {nombre}"

    mensaje = saludar("Carlos")
    print(mensaje)
```

---

### Módulos y paquetes

Los módulos son archivos de Python que contienen definiciones y declaraciones. Los paquetes son colecciones de módulos organizados en directorios.

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiM04eFw_PT-ObUOTYYe3KLps-GUcGfwg8jgrf_YZHbpJCd_9VBz25xv6X8ZA9SCVPYVKxrq6LyMg9a6b0NeHjmvQPSmqOqd2sgOn-rdVxGFepu2aXkg_ILCxsVXwWR6IKHz8l83zRBaZBP/s1600/PACKAGE.jpg" width="300" style="margin: 20px; border-radius: 12px; border: 1px"/>

- Archivo llamado operaciones.py

```python
    def sumar(a, b):
        return a + b
```

- Archivo principal

```python
from operaciones import sumar
print(sumar(2, 3))
```

---

### Buenas prácticas

- Usar nombres descriptivos.

- Comentar el código cuando sea necesario.

- Escribir funciones pequeñas y reutilizables.

- Seguir la guía [PEP8](https://www.python.org/dev/peps/pep-0008/) (documento oficial de Python que define las guías de estilo para escribir código limpio, legible y consistente).

### Recursos útiles

- [Python para principiantes – W3Schools](https://www.w3schools.com/python/)

- [Documentación oficial de Python](https://docs.python.org/3/)

- [Google's Python Class (gratis)](https://developers.google.com/edu/python)

---
---

## Introducción a oTree

<img src="https://otree.readthedocs.io/en/latest/_images/splash.png" width="300" style="border-radius: 12px; border: 1px"/>


### Objetivo
Aprender a crear, ejecutar y estructurar un experimento en oTree, una plataforma basada en Python usada para juegos económicos, encuestas interactivas y experimentos sociales.

---

### ¿Qué es oTree?

**oTree** es una plataforma de código abierto escrita en **Python**, diseñada para construir:

- Juegos económicos (como dilemas del prisionero, subastas, bienes públicos).
- Encuestas interactivas.
- Experimentos de laboratorio o en línea con múltiples participantes.

---

### Requisitos previos

- Python 3.10 o superior
- Git (opcional pero recomendado)
- Conocimientos básicos de programación en Python

---

### Instalación

```bash
    pip install otree

    otree --version #Verifica la instalación y versión de oTree (No obligatorio)
```

---

### Crear un nuevo proyecto

```bash
    otree startproject nombre_proyecto

    cd nombre_proyecto # Permite entrar al directorio del proyecto
```
- Estructura del proyecto

nombre_proyecto/
├── __init__.py
├── settings.py
└── nombre_app/ (creada después)

---

### Crear una app dentro del proyecto

```bash 
    otree startapp nombre_app
```

Esto creará una carpeta con:

- `__init__.py:` configuración de app

    - `models:` sección del `__init__.py` que define datos y lógica

    - `pages:` sección del `__init__.py` que define interfaz y flujo

- `templates/:` HTML para las páginas

---

### Estructura básica de una app

#### init ➜ models

Define las clases Player, Group, Subsession, con campos (IntegerField, StringField, etc.).

```python
    from otree.api import *

    class C(BaseConstants):
        NAME_IN_URL = 'mi_app'
        NUM_ROUNDS = 3
        PLAYERS_PER_GROUP = None

    class Subsession(BaseSubsession):
        pass

    class Group(BaseGroup):
        pass

    class Player(BasePlayer):
        respuesta = models.IntegerField() # Campo para almacenar respuestas en este caso será un número entero
```

#### init ➜ pages

Define qué ve cada jugador y en qué orden.

```python
    class MiPagina(Page):
        form_model = 'player'
        form_fields = ['respuesta']

    class Resultados(Page):
        def is_displayed(player):
            return player.round_number == C.NUM_ROUNDS

    page_sequence = [MiPagina, Resultados]
```

#### templates/mi_app/MiPagina.html

Se usa html con DJango para definir la interfaz. (Django es un framework de Python que permite crear aplicaciones web de forma rápida y sencilla)

```html
    {{ block title }} Mi pregunta {{ endblock }}

    {{ block content }}
        ¿Cuál es tu número favorito?
        {{ formfields }}
        {{ next_button }}
    {{ endblock }}
```

---

### Ejecutar el experimento (modo local)

```bash
    otree devserver # Inicia el servidor de desarrollo

    #Nos debería mostrar algo como:
    http://localhost:8000 #Url donde se ejecuta el experimento
```

---

### Recursos útiles

- [Documentación oficial de oTree](https://otree.readthedocs.io/en/latest/)

- [Ejemplos oficiales de oTree](https://www.otreehub.com/)

- [Guía rápida de oTree en español (GitHub)](https://github.com/otree-org/otree)

---
---

## Introducción a Git y GitHub

<p float="left">
  <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" width="150" style="margin: 20px;"/>
  <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="150" style="border-radius: 12px; border: 1px solid #ddd; margin: 20px;"/>
</p>



### Objetivo
Aprender los fundamentos de Git para controlar versiones de nuestros proyectos, colaborar en equipo y gestionar cambios de manera ordenada.

❗**Nota:** `En este curso nos limitaremos a usar Git para clonar el repositorio y tener en nuestro dispositivo de forma local los archivos necesarios para el desarrollo de los experimentos. No profundizaremos en el uso de GitHub, pero es importante mencionar que GitHub es una plataforma que permite alojar repositorios de Git y colaborar con otros desarrolladores.`

---

### ¿Qué es Git?

**Git** es un sistema de control de versiones distribuido.  
Permite guardar el historial de cambios de un proyecto y trabajar con otros de forma simultánea.

> Imagina que Git es como una "máquina del tiempo" para tu código.

---

### Instalación

- Descárgalo desde: [https://git-scm.com](https://git-scm.com)
- Verifica que esté instalado:

```bash
    git --version
```

---

### Configuración inicial (Desde la terminal)
```bash
    git config --global user.name "Tu Nombre"
    git config --global user.email "
```

---

### Comandos básicos (Desde la terminal)

```bash
# Inicializa un repositorio Git en la carpeta actual
git init

# Verifica el estado actual de los archivos (si están modificados, sin seguimiento, listos para commit, etc.)
git status

# Agrega un archivo específico al área de preparación (staging)
git add archivo.py

# Agrega todos los archivos modificados al área de preparación
git add .

# Registra los cambios preparados en el historial del repositorio con un mensaje
git commit -m "Mensaje explicativo del cambio"

# Muestra el historial de commits del repositorio
git log

# Muestra un resumen del historial de commits (una línea por commit)
git log --oneline

# Conecta el repositorio local con uno en GitHub (URL del repositorio remoto)
git remote add origin https://github.com/usuario/repositorio.git

# Cambia el nombre de la rama actual a 'main'
git branch -M main

# Envía los commits locales al repositorio remoto
git push -u origin main

# Trae los últimos cambios desde el repositorio remoto y los fusiona
git pull

# Clona un repositorio remoto en tu computadora (copia todo el proyecto)
git clone https://github.com/usuario/repositorio.git

# Muestra las diferencias entre el archivo actual y la última versión guardada
git diff

# Deshace los cambios hechos en un archivo (lo restaura a su versión anterior)
git restore archivo.py

# Elimina un archivo del proyecto y también del control de versiones
git rm archivo.py

# Reestablece todo el proyecto al último commit confirmado (⚠️ borra cambios locales)
git reset --hard

# Muestra la lista de archivos ignorados (si existe un archivo .gitignore)
git check-ignore -v *
```

---

### Recursos útiles

- [Sitio oficial de Git](https://git-scm.com)

- [GitHub Docs](https://docs.github.com/es)

- [Guía visual de Git (en español)](https://ndpsoftware.com/git-cheatsheet.html#loc=workspace;)

- [Curso completo de Git y GitHub (en español)](https://www.youtube.com/watch?v=3GymExBkKjE&t=8547s&ab_channel=MoureDevbyBraisMoure)

---

### Otras formas de usar Git

Mientras que la mayoría de los comandos de Git se ejecutan desde la terminal, existen herramientas gráficas que facilitan su uso:

- **[GitHub Desktop:](https://desktop.github.com/)** Interfaz gráfica para Git, fácil de usar.

- **[SourceTree:](https://www.sourcetreeapp.com/)** Otra interfaz gráfica avanzada.

❗**Nota:** `Cabe resaltar que para usar estas herramientas en conjunto con GitHub, es necesario tener una cuenta en GitHub.`

---
---

## 📚 Actividad practica 

❗**Nota:** `Recordar usar el método de entrega de actividades y parciales indicado en la sección de "Entrega de actividades y parciales" del curso.` *[Click para visitar "Entrega de actividades y parciales" en la introducción del curso.](../../README.md)*

1. [Formulario Utimatum/Dictador](https://docs.google.com/forms/d/14k2UL4Q-cAugpEqzCQQbgv8nZ1NNlDdCl8Pml1TlQuo/viewform?edit_requested=true)

2. Ultimatum Game:

    - Versión A: 
        a. Crea un proyecto llamada `ultimatum_game`.

        b. Dentro del proyecto, crea una app llamada `ultimatum_A`.
        
        c. Modifica el archivo `settings.py` para incluir la app `ultimatum_A` en la lista de `SESSION_CONFIGS`.

        d. Coloca tu nombre en el template `MyPage.html`.

        e. Comprueba que el experimento funciona correctamente ejecutando el comando `otree devserver` y accediendo a la URL proporcionada.

    ---

    - Versión B: 
        a. Crea un proyecto llamada `ultimatum_game`.

        b. Dentro del proyecto, crea una app llamada `ultimatum_B`.

        c. Modifica el archivo `settings.py` para incluir la app `ultimatum_B` en la lista de `SESSION_CONFIGS`.

        d. Coloca tu nombre en el template `Results.html`.

        e. Comprueba que el experimento funciona correctamente ejecutando el comando `otree devserver` y accediendo a la URL proporcionada.


Dependiendo de la versión asignada, deberás cumplir con las tareas correspondientes a cada una y para una mejor verificación de lo realizado tomar una ScreenShot al finalizar cada inciso, adjuntar las imágenes con el proyecto creado en un zip al correo designado.

[Rúbrica de calificación](clases\01_Tools_oTree_Python_GIT_02_Forms_SimpleSurvey\Rubrica_Taller_Ultimatum.pdf)