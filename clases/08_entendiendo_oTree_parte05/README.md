# Entendiendo oTree: Gift Exchange con Real Effort Task

Después de haber visto en nuestra [sesión anterior](../07_entendiendo_oTree_parte04/README.md) sobre el uso de *Multiplayer Games y chat* para la configuración de participantes de nuestros experimentos, ahora veremos cómo implementar y personalizar un juego de intercambio de regalos con una tarea de esfuerzo real usando oTree, cubriendo conceptos claves como "Apps & Rounds" y "Treatments & Timeouts"

## Introduction to the Real Effort Task Gift Exchange Game

El juego de intercambio de regalos es un experimento económico que modela una situación de reciprocidad en el trabajo, en la que un "empleador" ofrece un salario a un "empleado" a cambio de un nivel de esfuerzo. La "tarea de esfuerzo real" asignada permite que el nivel de trabajo del participante tenga un efecto directo en el resultado del juego.

![img_01](../../imgs/07/001.png)<sup><a href="#bib_01">1</a></sup>

### Game Objectives

El propósito es observar cómo la compensación y el nivel de esfuerzo afectan la reciprocidad entre los jugadores. Cada "empleado" elige su nivel de esfuerzo en respuesta al salario ofrecido, y los resultados ayudan a explorar incentivos y comportamientos en situaciones de trabajo.

## Apps & rounds

### Apps

En oTree, una *app* es una parte del experimento que organiza y gestiona el flujo de la experimentación, agrupando tareas y funciones en un solo bloque. Cada app puede tener su propia lógica y visualización, y pueden ser combinadas en diferentes configuraciones para crear experimentos más complejos. Los experimentos en oTree se dividen en rounds, que son ciclos repetitivos de la app, permitiendo que los participantes realicen acciones múltiples veces dentro del mismo juego o experiencia.

#### Combining apps

Para *combinar varias apps* en un solo experimento de oTree, debes incluirlas en el archivo settings.py en la lista SESSION_CONFIGS. De esta forma, cada app se ejecutará en secuencia durante las rondas del experimento.

```python
SESSION_CONFIGS = [
    dict(
        name='exp1',
        display_name="First experiment",
        num_demo_participants=2,
        app_sequence=['app1', 'app2', 'app3'], #Aquí se coloca el orden y las apps que deseas combinar
    ),
]
```

#### Passing data between apps


En oTree, puedes pasar datos entre diferentes *apps* utilizando variables en *participant o session*. Al almacenar datos en estas variables, puedes acceder a ellos en rondas posteriores de cualquier app. Por ejemplo, puedes guardar información como una recompensa o un puntaje y recuperarla más adelante para su uso en otra app. Esto se realiza mediante las funciones definidas en cada *app* y es útil para crear flujos de trabajo que requieren mantener el estado entre múltiples aplicaciones.

### Rounds

Las rounds representan las repeticiones de una misma fase del experimento. Dentro de una session, puedes tener múltiples *rounds*, y cada *round* puede contener múltiples apps que se ejecutan secuencialmente. Al usar rounds, puedes gestionar cómo se distribuyen las actividades entre las aplicaciones, permitiendo que los participantes pasen por varias fases del experimento de manera ordenada.

Para hacer que un juego se ejecute durante múltiples rondas en oTree, debes establecer **C.NUM_ROUNDS** en la configuración de tu aplicación. Por ejemplo, si el *app_sequence* de tu sesión es **['app1', 'app2']**, y **app1** tiene **NUM_ROUNDS = 3** y **app2** tiene **NUM_ROUNDS = 1**, entonces tu sesión tendrá 4 *subsesiones* en total. Cada ronda corresponderá a una nueva instancia del juego.

#### Round numbers

Puedes obtener el número de la ronda actual usando *player.round_number*. Este atributo está presente en los objetos de subsesión, grupo y jugador, y las rondas comienzan desde 1. Esto te permite hacer seguimientos de la ronda en la que se encuentra un jugador durante la ejecución de tu juego.


#### Passing data between rounds or apps


Cada ronda tiene objetos separados de *subsesión*, grupo y jugador. Por ejemplo, si estableces **player.my_field = True** en la *ronda 1*, en la *ronda 2*, al intentar acceder a **player.my_field**, su valor será None. Esto se debe a que los objetos de jugador de una ronda son distintos de los de otra ronda. Para acceder a datos de rondas o aplicaciones previas, puedes utilizar las técnicas descritas en la documentación de oTree.


#### in_rounds, in_previous_rounds, in_round, etc.

En oTree, los objetos **Player, Group y Subsession** tienen métodos para acceder a datos de rondas previas:

- *in_previous_rounds()* devuelve jugadores de rondas anteriores.
- *in_all_rounds()* incluye jugadores de todas las rondas.
- *in_rounds(m, n)* devuelve jugadores de rondas específicas.
- *in_round(m)* accede a un jugador en una ronda específica.

Estos métodos te permiten consultar información de rondas anteriores sin necesidad de almacenarla explícitamente.

```python
# Accede al jugador de la ronda anterior usando el número de la ronda actual menos uno
prev_player = player.in_round(player.round_number - 1)

# Imprime el resultado de la ronda anterior (por ejemplo, el pago del jugador)
print(prev_player.payoff)

```
Los métodos como *in_previous_rounds()*, *in_all_rounds()*, *in_rounds()* e *in_round()* funcionan de la misma manera para los objetos de *subsession* y grupo. Sin embargo, no tiene sentido usarlos si se reorganizan los grupos entre rondas, ya que estos métodos presuponen que los grupos no cambian durante el juego. Para acceder a la información de rondas anteriores o entre diferentes grupos, se deben utilizar adecuadamente dependiendo de cómo se gestionen las sesiones y grupos en el experimento.

#### Participant fields


Para acceder a los datos de un participante de una aplicación anterior, debes almacenarlos en el objeto *Participant*, ya que estos datos persisten entre aplicaciones. Para hacer esto, ve a la configuración y define `PARTICIPANT_FIELDS`, que es una lista de los nombres de los campos que deseas almacenar en el participante. Los métodos como *in_all_rounds()* solo sirven para acceder a datos de rondas anteriores dentro de la misma aplicación.

Los campos personalizados de los participantes se almacenan internamente en un diccionario llamado *participant.vars*. Por ejemplo, *participant.mylist = [1, 2, 3]* es equivalente a *participant.vars['mylist'] = [1, 2, 3]*.

#### Session fields

Para las variables globales que son las mismas para todos los participantes en una sesión, debes agregarlas a `SESSION_FIELDS`. Al igual que con `PARTICIPANT_FIELDS`, estos campos se almacenan internamente en `session.vars`, lo que permite que los valores sean accesibles en todo el ciclo de la sesión para todos los participantes.

#### Variable number of rounds

Para manejar un número variable de rondas, puedes usar páginas en vivo (Live pages). Alternativamente, puedes establecer `NUM_ROUNDS` en un número alto y luego ocultar el botón `{{ next_button }}` o usar `app_after_this_page` para evitar que los participantes avancen. Sin embargo, ten en cuenta que tener muchas rondas (más de 100) podría generar problemas de rendimiento, por lo que es importante probar bien la aplicación.

### Treatments
Para asignar participantes a diferentes grupos de tratamiento, puedes usar `creating_session`. Este método se ejecuta cuando se crea la sesión y permite asignar valores aleatorios o específicos a los participantes o grupos. Por ejemplo, puedes asignar un valor booleano (`True` o `False`) a cada jugador para un tratamiento como `time_pressure`. También es posible hacer lo mismo a nivel de grupo utilizando el método `get_groups()`.

```python
def creating_session(subsession):
    import random
    # Iteramos sobre los jugadores en la subsesión
    for player in subsession.get_players():
        # Asignamos un valor aleatorio (True o False) a 'time_pressure' para cada jugador
        player.time_pressure = random.choice([True, False])
        # Imprimimos el valor asignado para verificar
        print('set time_pressure to', player.time_pressure)
```

#### Treatment groups & multiple rounds







## Actividad Práctica: Bargaining
La negociación cooperativa o **"Cooperative bargaining"** es un proceso en el que dos personas deciden cómo compartir un excedente que pueden generar conjuntamente. Dado que este excedente puede dividirse de diversas maneras, los jugadores deben negociar cuál opción elegir. Este tipo de problemas de distribución se presentan en situaciones como la división de ganancias entre la dirección y los trabajadores, así como en la especificación de términos comerciales entre socios.

Ahora, la actividad consiste en:

1. Configurar "bargaining" en settings.py (2 jugadores por grupo).
2. Agregar una personalización a la página de espera.
3. Agregar por tiempo a la página de espera: si se demora más de 1 minuto el otro jugador, le coloque un valor de 0 puntos.
4. Agregar un chat para cada grupo en la parte en que se coloca la cantidad de puntos a aportar.

## NOTA

Para la nota del taller de la sesión deben interactuar con mínimo 2 jugadores (1 grupos) e interactuar con ellos, deben generar el archivo `.otreezip` enviarlo al profesor Ferley `heiner.rincon@urosario.edu.co` con el asunto `Taller sesión 7`, y con copia a Jorge `hopkeinst@gmail.com`.

Cualquier error que presenten, pueden consultar a Jorge por correo electrónico o chat.

## Bibliografía

Aquí tienes la bibliografía en el formato solicitado:

<ol>
    <li id="bib_01"> Chen, D.L., Schonger, M., & Wickens, C., “oTree – An Open-Source Platform for Laboratory, Online, and Field Experiments,” *Journal of Behavioral and Experimental Finance*, vol. 9, pp. 88-97, 2016. [Online]. Available: <a href="https://doi.org/10.1016/j.jbef.2015.12.001">https://doi.org/10.1016/j.jbef.2015.12.001</a>. [Accessed: 05-Nov-2024].</li>
    <li id="bib_02"> McClelland, G.H., “oTree Documentation: Apps & Rounds.” [Online]. Available: <a href="https://otree.readthedocs.io/en/latest/rounds.html#apps-rounds">https://otree.readthedocs.io/en/latest/rounds.html#apps-rounds</a>. [Accessed: 05-Nov-2024].</li>
    <li id="bib_03"> McClelland, G.H., “oTree Documentation: Treatments & Timeouts.” [Online]. Available: <a href="https://otree.readthedocs.io/en/latest/treatments.html#creating-session">https://otree.readthedocs.io/en/latest/treatments.html#creating-session</a>. [Accessed: 05-Nov-2024].</li>
</ol>


