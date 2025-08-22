# Taller 3 - Sessions, Subsessions, Groups & Participant
---
## Fecha de entrega: 27 Agosto 2025
---

## Sessions

- Una Session es la ejecución completa de un experimento.

- Contiene todas las rondas y jugadores.

- Se crea cuando el administrador inicia el experimento desde la interfaz de oTree.

👉 Piensa en la Session como "toda la clase de experimento".

```python
    # Aquí se modifica la configuración de la sesión
    def creating_session(subsession: Subsession):
        for p in subsession.get_players():
            p.participant.vars['saldo_inicial'] = 100
```

---

## Subsessions

- Una Subsession corresponde a una ronda dentro de una Session.

- Cada Subsession contiene un conjunto de jugadores y grupos.

- Permite que un mismo juego tenga múltiples rondas con variaciones en reglas o datos.

👉 Cada Subsession es "una ronda del juego".

```python
    class Subsession(BaseSubsession):
        # Ejemplo: asignar un valor distinto por ronda
        def creating_session(self):
            for p in self.get_players():
                p.ronda_valor = self.round_number * 10
```

---

## Groups

*Ya lo vimos en el taller anterior, pero aquí un repaso rápido:*

- Un Group es un subconjunto de jugadores dentro de una Subsession.

- Se utiliza en juegos que requieren interacción entre participantes.

- El número y la composición de los grupos puede definirse automáticamente o manualmente.

👉 Un Group es "la mesa de jugadores que interactúan entre sí en esa ronda".

```python
    class Group(BaseGroup):
        decision_a = models.IntegerField()
        decision_b = models.IntegerField()

    # Ejemplo: emparejar jugadores manualmente
    def creating_session(subsession: Subsession):
        subsession.group_randomly()
```

---

## Participant

- Representa a una persona real que participa en el experimento.

- Su información persiste a lo largo de todas las apps y rondas de la Session.

- Guarda datos como:

    - Identificador único del participante.

    - Respuestas a preguntas.

    - Pagos acumulados.

👉 El Participant es "la persona real en el experimento".

```python
    class Player(BasePlayer):
        respuesta = models.IntegerField()

    # Ejemplo: guardar un dato en participant.vars
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['ultima_respuesta'] = player.respuesta
```

---

### Recursos útiles

- [Documentación oficial de oTree - Built-in fields and methods](https://otree.readthedocs.io/en/latest/models.html#built-in-fields-and-methods)

- [Ejemplos oficiales de oTree](https://www.otreehub.com/)

- [Guía rápida de oTree en español (GitHub)](https://github.com/otree-org/otree)

---

## Public Goods Game

Idea del juego:

- Cada jugador recibe una dotación inicial de 10,000 puntos (ENDOWMENT).

- Decide cuánto de esa dotación aportar a un fondo común (contribution).

- El total del fondo común se multiplica por 2 (MULTIPLIER = 2).

- Esa cantidad se reparte en partes iguales entre todos los jugadores.

- La ganancia de cada jugador = lo que se quedó + su parte del fondo multiplicado.


---

## 📚 Actividad practica 


❗**Nota:** `Recordar usar el método de entrega de actividades y parciales indicado en la sección de "Entrega de actividades y parciales" del curso.` *[Click para visitar "Entrega de actividades y parciales" en la introducción del curso.](../../README.md)*

1. [QUIZ Public Goods](https://forms.gle/vg27XE6yDfaSCZcv8)

2. Public Goods:

    - Versión A:

        a. Sessions -> Definir el numero de rondas en `BaseConstants` usando el atributo `NUM_ROUNDS = 1`

        b. Subsession -> Agregar un relleno vació o *pass* al `class Subsession(BaseSubsession)`, ya que no se requiere lógica de subsession momentáneamente.

        c. Group -> Definir el tipo de dato que usara el campo `total_contribution`, que para este caso sera de tipo `models.CurrencyField()`.

        d. Group -> Crear el campo `individual_share` que también será de tipo `models.CurrencyField()`.

        e. Participant -> Al campo `set_payoffs` se le perdió su asignación, por lo que debes volver a agregar el bucle que calcula el pago de cada jugador:
        ```python
            for p in players:
            p.payoff = C.ENDOWMENT - p.contribution + group.individual_share
        ```

    ---

    - Versión B:

        a. Sessions -> Definir el numero de participantes por grupo en `BaseConstants` usando el atributo `PARTICIPANTS_PER_GROUP = 3`.

        b. Sessions -> Determinar el dinero base con el que comenzaran los jugadores en 10000 dentro de la sección `BaseConstants` mediante el atributo `ENDOWMENT = cu()`.

        c. Subsession -> Declarar el dato que recibirá la clase `Subsession` como `BaseSubsession`.

        d. Group -> `Group` debería estar definido como una clase es decir usando el `class` corrige esta definición.

        e. Participant -> Al campo `set_payoffs` se le perdió su asignación, por lo que debes volver a agregar el bucle que calcula el pago de cada jugador:
        ```python
            for p in players:
            p.payoff = C.ENDOWMENT - p.contribution + group.individual_share
        ```

- En la **versión A**, el foco es que los estudiantes trabajen con rondas, grupos y payoffs.

- En la **versión B**, el foco es que los estudiantes completen constantes de sesión, subsession y lógica de grupo-participante.


En la siguiente lista se realiza la asignación de la versión a entregar. La asignación se realizó **al azar** y a **cada ID** de le asignó **una versión**: 

<img src="../../imgs/3/Lista Taller 3.png" style="margin: 20px;">

Dependiendo de la versión asignada, deberás cumplir con las tareas correspondientes a cada una y para una mejor verificación de lo realizado tomar una ScreenShot al finalizar cada inciso, adjuntar las imágenes con el proyecto creado en un zip al correo designado.

Enlaces de interés:

- [Apoyo Taller 3]()

- [Rúbrica de calificación](Rubrica_Taller_PublicGoods.pdf)