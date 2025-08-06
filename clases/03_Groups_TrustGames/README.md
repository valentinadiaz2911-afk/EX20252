# Taller 2 - Groups & Trust Games
---
## Fecha de entrega: 13 Agosto 2025
---
## Groups

En oTree, los **`group`** es una agrupación de participantes dentro de una **subsession** (una ronda del experimento).  
Los grupos permiten modelar interacciones entre jugadores, como en juegos de negociación, cooperación, competencia, etc.

---

### ¿Cómo se forman los grupos?

Los grupos pueden formarse de varias formas:

- **Automáticamente** por oTree (por defecto, por orden de llegada).
- **Manual o personalizada**, usando el método `creating_session` en la clase `Subsession`.
- **Reasignación por rondas**, si el juego tiene múltiples rondas y los grupos deben cambiar.

#### Ejemplo para agrupar aleatoriamente

```python
def creating_session(subsession):
    subsession.group_randomly(fixed_id_in_group=True)
```
---
### ¿Qué contiene un `group`?

Un objeto `Group` puede contener:

- **Variables compartidas entre jugadores**, por ejemplo: monto a repartir, resultado del grupo, etc.
- **Métodos lógicos**, como funciones para calcular resultados grupales.
- **Acceso a los jugadores** del grupo con:

```python
group.get_players()
```

---
### Ejemplo práctico

Si haces un juego donde un jugador propone y otro acepta (como el **juego del ultimátum**), esos dos jugadores se agrupan en un `Group`.

```python
class Group(BaseGroup):
    offer = models.CurrencyField()
    accepted = models.BooleanField()
```
---

### Relación entre estructuras en oTree

```text
Session → Subsession → Group → Player
```

---

### Recursos útiles

- [Documentación oficial de oTree - Groups](https://otree.readthedocs.io/en/latest/multiplayer/groups.html)

- [Ejemplos oficiales de oTree](https://www.otreehub.com/)

- [Guía rápida de oTree en español (GitHub)](https://github.com/otree-org/otree)

---

## Trust Game (Juego de Confianza 🤝)

El **Trust Game** o **Juego de Confianza** es un experimento económico clásico que mide la **confianza** y la **reciprocidad** entre dos jugadores:

- **Jugador A (Trustor → "Confiante" o "Depositante de confianza")**: decide cuánto dinero enviar al Jugador B.
- **Jugador B (Trustee → "Receptor" o "Depositario de confianza")**: recibe el dinero enviado multiplicado (por ejemplo, ×3) y luego decide cuánto devolver a A.

---

### Dinámica del juego paso a paso

1. Ambos jugadores reciben una cantidad inicial (por ejemplo, 100 unidades).
2. El **Jugador A** envía una parte (o nada) al **Jugador B**.
3. La cantidad enviada se multiplica por un factor (típicamente ×3).
4. El **Jugador B** decide cuánto devolver al **Jugador A**.

---

### ¿Qué mide este juego?

- El nivel de **confianza** del Jugador A (cuánto está dispuesto a enviar).
- El nivel de **reciprocidad** del Jugador B (cuánto devuelve).

---

### Interpretación

- Si A no envía nada, no hay posibilidad de ganar más.
- Si B no devuelve nada, puede generar desconfianza en futuras interacciones.
- Se usa para estudiar **comportamiento prosocial**, **cooperación** y **altruismo condicional**.


---

## 📚 Actividad practica 


❗**Nota:** `Recordar usar el método de entrega de actividades y parciales indicado en la sección de "Entrega de actividades y parciales" del curso.` *[Click para visitar "Entrega de actividades y parciales" en la introducción del curso.](../../README.md)*

1. [QUIZ Trust](https://forms.gle/BtXzYgJJ8EvFUW3x8)

2. Trust Game:

    - Versión A:

        a. Clona el repositorio [EX20252](https://github.com/sEF-uRosario/EX20252).

        b. Abre el proyecto `Trust Game - A` dentro de la capeta `Proyecto base para taller 2`.

        c. Establecer la cantidad de jugadores por grupo en 2 agregando el `PLAYERS_PER_GROUP = 2` en la sección C(BaseConstants) en el archivo `__init__.py`.

        d. Configura el `form_model = ""` de la clase `Enviar(Page)`  para que use el modelo `group`.

        e. Agrega la parte faltante en el **return** de la función `is_displayed` usada en la clase `Enviar(Page)`, para que solo el jugador 1 (id_in_group == 1) pueda ver esa página, usando `player.id_in_group == 1`.

        f. Comprobar que el juego funciona correctamente con el `otree devserver`.

    ---

    - Versión B:

        a. Clona el repositorio [EX20252](https://github.com/sEF-uRosario/EX20252).

        b. Abre el proyecto `Trust Game - B` dentro de la capeta `Proyecto base para taller 2`.

        c. Indicar que se manejara la variable group en la función `dinero_devuelto_choices()` con `(group: Group)`.

        d. Para la función `set_payoffs(group: Group)` definir las ids de los jugadores que se agruparan en el juego, dándole el valor de id correspondiente en cada caso a `group.get_players_by_id()`. Es decir, el jugador 1 tendrá el id 1 y el jugador 2 tendrá el id 2.

        e. Agregar la parte faltante en la asignación `group = player` de la función `vars_for_template(player: Player)` usada en la clase `Devolver(Page)`, para que se asigne el grupo al jugador, usando `group = player.group`.

        f. Comprobar que el juego funciona correctamente con el `otree devserver`.

En la siguiente lista se realiza la asignación de la versión a entregar. La asignación se realizó **al azar** y a **cada ID** de le asignó **una versión**: 

<img src="../../imgs/2/Lista Taller 2.png" style="margin: 20px;">

Dependiendo de la versión asignada, deberás cumplir con las tareas correspondientes a cada una y para una mejor verificación de lo realizado tomar una ScreenShot al finalizar cada inciso, adjuntar las imágenes con el proyecto creado en un zip al correo designado.

Enlaces de interés:

- [Apoyo Taller 2]()

- [Rúbrica de calificación](Rubrica_Taller_Trust.pdf)

