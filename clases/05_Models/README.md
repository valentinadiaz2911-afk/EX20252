# Taller 4 - Models
---
## Fecha de entrega: 3 Septiembre 2025
---

En **oTree**, los `models` son las clases y variables que definen la **lógica y los datos del experimento**.  
Todo lo que quieras **guardar en la base de datos** debe declararse como un **campo de modelo**.

---

## Tipos de modelos en oTree

En cada app de oTree, por defecto existen 3 modelos principales:

### 1. Subsession

- Representa una **ronda** del experimento.  
- Si tienes 5 rondas, habrá 5 instancias de `Subsession`.  
- Se usa para configurar condiciones al inicio de cada ronda.

### 2. Group

- Representa un **grupo de jugadores**.  
- Si tu juego es individual, no necesitas modificarlo.  
- Si tu juego es en grupos (ej: dilema del prisionero, bienes públicos), aquí guardas variables **colectivas**.

### 3. Player

- Representa a **cada participante**.  
- Aquí defines las **respuestas individuales** (ej: decisiones, preguntas del cuestionario, puntajes).

---

## Ejemplo básico

```python
    from otree.api import *

    class C(BaseConstants):
        NAME_IN_URL = 'mi_juego'
        PLAYERS_PER_GROUP = 2
        NUM_ROUNDS = 3

    class Subsession(BaseSubsession):
        pass

    class Group(BaseGroup):
        total = models.IntegerField()  # dato del grupo

    class Player(BasePlayer):
        decision = models.IntegerField()  # dato del jugador
        age = models.IntegerField(label="¿Cuál es tu edad?")
```
En este ejemplo:

- `Group.total` guarda un número compartido por los jugadores del grupo.  
- `Player.decision` y `Player.age` son respuestas individuales que se almacenan en la base de datos.  

---

### Campos (`models.Field`)

Los más usados son:

- `models.IntegerField()` → números enteros.  
- `models.FloatField()` → números decimales.  
- `models.StringField()` → texto.  
- `models.BooleanField()` → verdadero/falso.  
- `models.CurrencyField()` → dinero (usa la unidad experimental de oTree).  

Ejemplo con opciones:

```python
    choice = models.IntegerField(
        choices=[1, 2, 3],
        label="Elige un número"
    )
```

## Resumen

- Los `models` son las variables que se guardan en la base de datos.

- Se dividen en:

    - `Subsession` (ronda)

    - `Group` (grupo)

    - `Player` (participante)

- Usas `models.*Field()` para definir los datos que quieres almacenar.

---

### Recursos útiles

- [Documentación oficial de oTree - Models](https://otree.readthedocs.io/en/latest/models.html)

- [Ejemplos oficiales de oTree](https://www.otreehub.com/)

- [Guía rápida de oTree en español (GitHub)](https://github.com/otree-org/otree)

---
## El juego de 2/3 del promedio

El **juego de 2/3 del promedio** es un experimento muy usado en economía y teoría de juegos para estudiar cómo las personas razonan sobre lo que harán los demás.  

## Reglas básicas
1. Cada jugador elige **un número entero** dentro de un rango (normalmente entre 0 y 100).  
2. Se calcula el **promedio** de todos los números elegidos.  
3. El ganador es el jugador cuyo número esté más cerca de **2/3 de ese promedio**.  

---

## Ejemplo
Supongamos que hay 3 jugadores y eligen:  
- Jugador A: 30  
- Jugador B: 60  
- Jugador C: 90  

El promedio es:  
\[
(30 + 60 + 90) / 3 = 60
\]

2/3 del promedio =  
\[
60 \times \tfrac{2}{3} = 40
\]

El número más cercano a **40** es **30** → gana el **Jugador A**.  

---

## La lógica detrás
- Si todos eligen al azar, el promedio rondará 50, entonces 2/3 de eso sería ~33.  
- Si la gente piensa en esto, tenderán a elegir números más bajos.  
- Si todos son **perfectamente racionales** y creen que los demás también lo son, la única solución estable (equilibrio de Nash) es que todos elijan **0**.  

---

## Niveles de razonamiento
Esto muestra hasta qué nivel de razonamiento estratégico llega cada persona:  

- **Nivel 0:** Elige al azar o cerca de 50.  
- **Nivel 1:** Piensa: “El promedio será 50, entonces yo elijo 33”.  
- **Nivel 2:** Piensa: “Los demás van a elegir 33, entonces yo elijo 22”.  
- **Nivel n:** Va ajustando hacia abajo hasta acercarse a **0**.  

---

## 📚 Actividad practica 


❗**Nota:** `Recordar usar el método de entrega de actividades y parciales indicado en la sección de "Entrega de actividades y parciales" del curso.` *[Click para visitar "Entrega de actividades y parciales" en la introducción del curso.](../../README.md)*

1. [QUIZ Experimental Methods](https://forms.gle/sXjYpAZAj86CfNSu5)

2. 2/3 del Promedio:

    - Versión A:

        a. Realizar un Fetch del repositorio de GitHub.

        b. A la constante `NAME_IN_URL = 'guess_2_3'` agregar su primer nombre y primer apellido dentro de las comillas, pero evitando quitar el nombre original, es decir agregándolo al final.

        c. Cambiar el valor de la constante `VALOR_MAXIMO` para que sea 100.

        d. Definir el tipo de dato que recibirá la variable `dos_tercios_promedio` como `models.FloatField()`. Esto para poder recibir números decimales.

        e. Definir el tipo de dato que recibirán las variables `mejor_estimacion` y `n_ganadores` como `models.IntegerField()`. Esto para poder recibir solo números enteros.

        f. Agregar `group.n_ganadores` en el pago de los jugadores, es decir en la terminación de `p.payoff` que se encuentra al final de la función `set_payoffs`.

    ---

    - Versión B:

        a. Realizar un Fetch del repositorio de GitHub.

        b. A la constante `NAME_IN_URL = 'guess_2_3'` agregar su primer nombre y primer apellido dentro de las comillas, pero evitando quitar el nombre original, es decir agregándolo al final.

        c. Definir el valor de la constante `BOTE_GANANCIAS` en 10000.

        d. La variable `estimacion` debe contar con un `min`, `max` y `label`, en ese orden para poder ser utilizada en el formulario de entrada.

        e. Asignarle el valor inicial como falso a la variable booleana `es_ganador` usando `initial = False`, con el fin de evitar ganadores prematuros.

        f. En la función `set_payoffs`, asegurarse de que `players` incluya `group.get_players()` en su asignación, para decirle a la app como obtener los jugadores del grupo.

En la siguiente lista se realiza la asignación de la versión a entregar. La asignación se realizó **al azar** y a **cada ID** de le asignó **una versión**: 

<img src="../../imgs/4/Lista_Taller_4.png" style="margin: 20px;">

Dependiendo de la versión asignada, deberás cumplir con las tareas correspondientes a cada una y para una mejor verificación de lo realizado **tomar una ScreenShot al finalizar cada inciso**, **adjuntar las imágenes con el proyecto creado en un zip al correo designado**. Evitar archivos adicionales en el zip, **solo** debe contener la carpeta del proyecto y las imágenes solicitadas. Verificar que el proyecto enviado tenga los **cambios guardados**.

Enlaces de interés:

- [Apoyo Taller 4](https://youtu.be/m5JGYtdwArw)

- [Rúbrica de calificación](Rubrica_Taller_2-3_promedio.pdf)