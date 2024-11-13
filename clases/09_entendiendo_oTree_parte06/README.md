# Entendiendo oTree: Asset Market Teams

Después de haber visto en nuestra [sesión anterior](../08_entendiendo_oTree_parte05/README.md) sobre el uso de *"Apps & Rounds" y "Treatments & Timeouts"* para la configuración de aplicaciones, rondas, tratamientos y temporizadores de nuestros experimentos, ahora veremos cómo implementar y personalizar funcionalidades interactivas en tiempo real y automatización de pruebas en oTree, empleando live pages y bots. Estos recursos nos permitirán crear páginas dinámicas donde los participantes puedan interactuar en tiempo real y realizar simulaciones automatizadas para evaluar el comportamiento en distintas condiciones experimentales, optimizando el proceso de prueba y la experiencia del usuario.

## Asset Market Teams

El juego *asset_market_teams* en oTree es un experimento de mercado de activos en equipo, diseñado para estudiar el comportamiento de los participantes al comerciar con activos en un mercado competitivo. Los jugadores están organizados en equipos y pueden comprar y vender activos durante varias rondas, mientras el valor del activo fluctúa o sigue una tendencia predefinida. 

El objetivo es maximizar las ganancias al anticipar movimientos del mercado, tomar decisiones de compra o venta estratégicas, y gestionar el riesgo en conjunto con los compañeros de equipo. Este tipo de juego se utiliza para investigar la formación de burbujas financieras, el impacto de la coordinación en decisiones de inversión, y cómo los participantes reaccionan ante la incertidumbre y las señales del mercado.

![img_01](../../imgs/09/001.png)<sup><a href="#bib_01">1</a></sup>

## Live pages

Las *live pages* permiten la comunicación continua con el servidor y se actualizan en tiempo real, lo que es ideal para juegos que requieren un tiempo continuo. Son perfectas para juegos que involucran mucha interacción entre los jugadores, como aquellos con intercambio constante de información o decisiones, como subastas o juegos de negociación.

### Sending data to the server

Llama a la función `liveSend()` en tu código JavaScript cada vez que quieras enviar datos al servidor. Por ejemplo, para enviar una oferta de 99 en nombre del usuario, llamarías a `liveSend()` con ese valor.

```js
// Enviar el valor 99 al servidor usando la función liveSend
liveSend(99);
```

La función debe definir un argumento que reciba cualquier dato que se le envíe.

```python
class MyPage(Page):
    # Método estático que maneja la recepción de datos en tiempo real.
    @staticmethod
    def live_method(player, data):
        # Imprime el mensaje recibido con la identificación del jugador y los datos enviados.
        print('recibido una oferta de', player.id_in_group, ':', data)
```

Si estás utilizando oTree Studio, debes definir una función para el jugador cuyo nombre comience con `live_`. (Nota: la función `live_method` en WaitPage aún no es compatible).

### Sending data to the page

Para enviar datos de vuelta, debes retornar un diccionario cuyas claves sean los ID de los jugadores que recibirán el mensaje. Por ejemplo, aquí hay un método que simplemente envía "gracias" a quien envíe un mensaje.

```python
def live_method(player, data):
    # Retorna un diccionario donde la clave es el ID del jugador y el valor es el mensaje "thanks".
    return {player.id_in_group: 'thanks'}
```

Para enviar a varios jugadores, usa su `id_in_group`. Por ejemplo, este código reenvía cada mensaje a los jugadores 2 y 3:

```python
def live_method(player, data):
    # Retorna un diccionario que envía el mismo mensaje a los jugadores con id_in_group 2 y 3.
    return {2: data, 3: data}
```

Para transmitir el mensaje a todo el grupo, usa 0 (un caso especial ya que no es un `id_in_group` real).

```python
def live_method(player, data):
    # Retorna un diccionario que envía el mensaje a todos los jugadores del grupo usando el ID especial 0.
    return {0: data}
```

En tu JavaScript, define una función `liveRecv`. Esta será llamada automáticamente cada vez que se reciba un mensaje del servidor.

```js
function liveRecv(data) {
    // Muestra en la consola el mensaje recibido desde el servidor.
    console.log('¡mensaje recibido!', data);
    
    // Aquí va tu código para manejar el mensaje recibido.
}
```

### Example: auction

```python
class Group(BaseGroup):
    # Define el jugador con la oferta más alta y la cantidad de la oferta más alta.
    highest_bidder = models.IntegerField()
    highest_bid = models.CurrencyField(initial=0)

class Player(BasePlayer):
    # La clase Player está vacía por ahora, pero puede contener campos adicionales si es necesario.
    pass
```

```python
def live_method(player, bid):
    # Obtiene el grupo al que pertenece el jugador y su ID dentro del grupo.
    group = player.group
    my_id = player.id_in_group
    
    # Si la oferta actual es más alta que la oferta más alta registrada, actualiza los valores.
    if bid > group.highest_bid:
        group.highest_bid = bid
        group.highest_bidder = my_id
        
        # Prepara una respuesta con el ID del jugador y su oferta.
        response = dict(id_in_group=my_id, bid=bid)
        
        # Retorna el diccionario con la respuesta para todos los jugadores del grupo (ID especial 0).
        return {0: response}
```

```html
<table id="history" class="table">
    <tr>
        <th>Jugador</th>
        <th>Oferta</th>
    </tr>
</table>
<input id="inputbox" type="number">
<button type="button" onclick="sendValue()">Enviar</button>

<script>

    // Obtiene el elemento de la tabla y el campo de entrada.
    let history = document.getElementById('history');
    let inputbox = document.getElementById('inputbox');

    // Esta función se llama automáticamente cuando se recibe un mensaje.
    function liveRecv(data) {
        // Agrega una nueva fila en la tabla con el ID del jugador y la oferta recibida.
        history.innerHTML += '<tr><td>' + data.id_in_group + '</td><td>' + data.bid + '</td></tr>';
    }

    // Esta función se llama cuando el jugador presiona el botón "Enviar".
    function sendValue() {
        // Envía el valor introducido en el campo de entrada al servidor.
        liveSend(parseInt(inputbox.value));
    }

</script>
```

(Nota: en JavaScript, `data.id_in_group` es igual a `data['id_in_group']`).

### Data

Los datos que envíes y recibas pueden ser de cualquier tipo (siempre que sean serializables en formato JSON). Por ejemplo, estos son todos válidos:

```js
// Envía el número 99 al servidor.
liveSend(99);

// Envía el texto 'hello world' al servidor.
liveSend('hello world');

// Envía un arreglo con los números 4, 5, y 6 al servidor.
liveSend([4, 5, 6]);

// Envía un objeto con dos claves: 'type' con valor 'bid' y 'value' con valor 10.5.
liveSend({'type': 'bid', 'value': 10.5});
```

El tipo de dato más versátil es un diccionario, ya que permite incluir múltiples piezas de metadatos, en particular, el tipo de mensaje que es:

```js
// Envía un objeto que representa una oferta con un valor de 99.9 al jugador 3.
liveSend({'type': 'offer', 'value': 99.9, 'to': 3});

// Envía un objeto que representa una respuesta, indicando que la oferta fue aceptada por el jugador 3.
liveSend({'type': 'response', 'accepted': true, 'to': 3});
```

Luego, puedes usar sentencias `if` para procesar diferentes tipos de mensajes:

```python
def live_method(player, data):
    # Obtiene el tipo de mensaje del diccionario 'data'.
    t = data['type']
    
    # Si el tipo de mensaje es 'offer', procesa la oferta.
    if t == 'offer':
        # Obtiene el jugador al que se le envía la oferta.
        other_player = data['to']
        
        # Prepara una respuesta con el tipo 'offer', el jugador que envía y el valor de la oferta.
        response = {
            'type': 'offer',
            'from': player.id_in_group,
            'value': data['value']
        }
        
        # Retorna la respuesta al jugador especificado.
        return {other_player: response}
    
    # Si el tipo de mensaje es 'response', procesar según el caso (aquí se puede agregar más lógica).
    if t == 'response':
        # Procesar la respuesta aquí
        ...
```

### History

Por defecto, los participantes no verán los mensajes que fueron enviados antes de que llegaran a la página. (Y los datos no se reenviarán si actualizan la página.) Si deseas guardar el historial, deberías almacenarlo en la base de datos. Cuando un jugador carga la página, tu JavaScript puede hacer una llamada como `liveSend({})`, y puedes configurar tu `live_method` para recuperar el historial del juego desde la base de datos.

### ExtraModel

Las páginas en vivo a menudo se utilizan junto con un `ExtraModel`, que te permite almacenar cada mensaje o acción individual en la base de datos.

### Keeping users on the page

Supongamos que se requieren 10 mensajes antes de que los usuarios puedan continuar a la siguiente página.

Primero, debes omitir el `{{ next_button }}`. (O usar JavaScript para ocultarlo hasta que la tarea esté completada.)

Cuando la tarea esté completada, envías un mensaje:

```python
class Group(BaseGroup):
    # Almacena el número de mensajes enviados.
    num_messages = models.IntegerField()
    # Indica si el juego ha terminado.
    game_finished = models.BooleanField()


class MyPage(Page):
    def live_method(player, data):
        # Obtiene el grupo al que pertenece el jugador.
        group = player.group
        
        # Aumenta el contador de mensajes en 1.
        group.num_messages += 1
        
        # Si se han enviado 10 mensajes, marca el juego como terminado.
        if group.num_messages >= 10:
            group.game_finished = True
            # Prepara la respuesta indicando que el juego ha terminado.
            response = dict(type='game_finished')
            # Retorna la respuesta a todos los jugadores.
            return {0: response}
```

Luego, en la plantilla, envía la página automáticamente mediante JavaScript:

```js
function liveRecv(data) {
    // Muestra en la consola el mensaje recibido.
    console.log('recibido', data);
    
    // Obtiene el tipo de mensaje recibido.
    let type = data.type;
    
    // Si el tipo es 'game_finished', envía el formulario automáticamente.
    if (type === 'game_finished') {
        document.getElementById("form").submit();
    }
    
    // Aquí puedes manejar otros tipos de mensajes si es necesario.
}
```

Por cierto, usando una técnica similar, podrías implementar una página de espera personalizada, por ejemplo, una que te permita continuar después de un tiempo determinado, incluso si no todos los jugadores han llegado.

### General advice about live pages

Aquí hay algunos consejos generales (que no aplican a todas las situaciones). Se recomienda implementar la mayor parte de tu lógica en Python y usar JavaScript solo para actualizar el HTML de la página, porque:

- El lenguaje JavaScript puede ser bastante complicado de usar correctamente.
- Tu código Python se ejecuta en el servidor, que es centralizado y confiable. JavaScript se ejecuta en los clientes, que pueden desincronizarse entre sí, y los datos pueden perderse cuando la página se cierra o se recarga.
- Debido a que el código Python se ejecuta en el servidor, es más seguro y no puede ser visto ni modificado por los participantes.

### Example: tic-tac-toe

Supongamos que estás implementando un juego de tres en línea (tic-tac-toe). Hay 2 tipos de mensajes que tu `live_method` puede recibir:

1. Un jugador marca una casilla, por lo que necesitas notificar al otro jugador.
2. Un jugador carga (o recarga) la página, por lo que necesitas enviarle la disposición actual del tablero.

Para la situación 1, debes usar un manejador de eventos de JavaScript como `onclick`, por ejemplo, para que cuando el jugador haga clic en la casilla 3, ese movimiento se envíe al servidor:

```js
// Envía un mensaje al servidor indicando que el jugador ha marcado la casilla 3.
liveSend({square: 3});
```

Para la situación 2, es conveniente poner un código como este en tu plantilla, que envíe un mensaje vacío al servidor cuando la página se carga:

```js
// Cuando el contenido de la página se ha cargado completamente, envía un mensaje vacío al servidor.
document.addEventListener("DOMContentLoaded", (event) => {
    liveSend({});
});
```

El servidor maneja estas 2 situaciones con una sentencia "if":

```python
def live_method(player, data):
    # Obtiene el grupo al que pertenece el jugador.
    group = player.group

    # Si los datos contienen el campo 'square', se está manejando la situación 1 (un jugador hace un movimiento).
    if 'square' in data:
        # SITUACIÓN 1
        square = data['square']

        # save_move debería guardar el movimiento en un campo del grupo.
        # Por ejemplo, si el jugador 1 modifica la casilla 3,
        # eso cambia group.board de 'X O XX  O' a 'X OOXX  O'
        save_move(group, square, player.id_in_group)

        # Para poder resaltar la casilla (y quizás decir quién hizo el movimiento).
        news = {'square': square, 'id_in_group': player.id_in_group}
    else:
        # SITUACIÓN 2: El jugador ha cargado o recargado la página.
        news = {}

    # get_state debería contener el estado actual del juego, por ejemplo:
    # {'board': 'X O XX  O', 'whose_turn': 2}
    payload = get_state(group)

    # .update combina los dos diccionarios (payload y news).
    payload.update(news)

    # Retorna el estado actualizado a todos los jugadores.
    return {0: payload}
```

En la situación 2 (cuando el jugador carga la página), el cliente recibe un mensaje como:

*{'board': 'X OOXX  O', 'whose_turn': 2}*

Este mensaje contiene:
- `'board'`: El estado actual del tablero, mostrando las marcas de los jugadores (por ejemplo, 'X' y 'O').
- `'whose_turn'`: El jugador que tiene el turno para hacer el siguiente movimiento, en este caso el jugador 2.

En la situación 1, el jugador recibe la actualización sobre el movimiento que acaba de realizarse, **y** el estado actual del juego.

*{'board': 'X OOXX  O', 'whose_turn': 2, 'square': square, 'id_in_group': player.id_in_group}*

Este mensaje incluye:
- `'board'`: El estado actual del tablero de juego.
- `'whose_turn'`: El ID del jugador que tiene el turno de jugar.
- `'square'`: La casilla que ha sido modificada (por el jugador que hizo el movimiento).
- `'id_in_group'`: El ID del jugador que realizó el movimiento.


El código de JavaScript puede ser "sencillo". No necesita llevar un seguimiento de quién es el turno; simplemente confía en la información que recibe del servidor. Incluso puede redibujar el tablero cada vez que recibe un mensaje.

Tu código también deberá validar la entrada del usuario. Por ejemplo, si el jugador 1 intenta mover cuando en realidad es el turno del jugador 2, debes bloquear ese movimiento. Por las razones mencionadas en la sección anterior, es mejor hacer esto en tu `live_method` en lugar de en el código de JavaScript.

### Summary

Como se ilustró anteriormente, el patrón típico para un `live_method` es el siguiente:

```python
if usuario_realizo_una_accion:
    # Obtener el estado actual del juego
    estado = obtener_estado_actual_del_juego()
    
    # Si la acción es ilegal o inválida, simplemente retornar sin hacer nada
    if accion_es_ilegal_o_invalida:
        return
    
    # Actualizar los modelos basados en el movimiento del jugador
    actualizar_modelos_con_el_movimiento()

    # Generar la retroalimentación (feedback) para enviar al usuario, o a otros usuarios
    noticias = generar_retroalimentacion()
else:
    # Si no hay acción, no se genera retroalimentación
    noticias = {}

# Obtener el estado actual del juego (en caso de que haya cambiado)
estado = obtener_estado_actual_del_juego()

# Combinar el estado con las noticias generadas (para enviar una respuesta completa)
payload = combinar_estado_con_noticias()

# Retornar el payload con la información actualizada
return payload
```

Nota que obtenemos el estado del juego dos veces. Esto se debe a que el estado cambia cuando actualizamos nuestros modelos, por lo que necesitamos refrescarlo después de realizar las actualizaciones.


### Troubleshooting

Si llamas a `liveSend` antes de que la página haya terminado de cargarse, obtendrás un error como "liveSend is not defined". Por lo tanto, espera a que se cargue el contenido del DOM (o utiliza `jQuery document.ready`, etc.):

```js
// Espera a que el contenido del DOM esté completamente cargado antes de ejecutar el código.
window.addEventListener('DOMContentLoaded', (event) => {
    // tu código va aquí...
});
```

No envies `liveSend` cuando el usuario haga clic en el botón "next", ya que salir de la página podría interrumpir el `liveSend`. En su lugar, haz que el usuario haga clic en un botón normal que dispare un `liveSend`, y luego realiza `document.getElementById("form").submit();` en tu función `liveRecv`.


## Bots

Los bots en oTree son herramientas automáticas que simulan a los participantes interactuando con tu aplicación. Estos bots navegan por las páginas del experimento, completan los formularios y realizan las acciones necesarias para verificar que todo funcione correctamente, tal como lo haría un participante humano. 

El propósito de esta funcionalidad es facilitar las pruebas automáticas, de modo que no tengas que intervenir manualmente para verificar el comportamiento de tu aplicación. Los bots pueden ser configurados para seguir los flujos del experimento, lo que ayuda a detectar posibles errores o problemas en el diseño, como interacciones entre páginas o validación de entradas.

Además, oTree Studio puede generar automáticamente el código para los bots, lo que hace que todo el proceso sea aún más sencillo. Así, puedes crear y ejecutar pruebas sin tener que escribir todo el código de prueba desde cero, ahorrando tiempo y esfuerzo. En resumen, esta característica está dirigida a facilitar la creación de experimentos y garantizar que todo funcione de manera fluida y confiable, incluso sin la intervención directa de los participantes humanos.

### Running bots

Para agregar bots a tu aplicación (consulta las instrucciones a continuación):

1. En la configuración de tu sesión, establece `use_browser_bots=True`.

Esto permite que oTree ejecute bots de navegador automáticamente cuando se inicie una sesión.

2. Ejecuta el servidor y crea una sesión. Una vez que se abran los enlaces de inicio, las páginas se reproducirán automáticamente con los bots del navegador. 

Esto hace que los bots interactúen de manera automática con tu aplicación, facilitando la prueba del flujo y las funcionalidades sin necesidad de intervención manual.

### Writing tests

En oTree Studio, ve a la sección "Tests" de tu aplicación. Haz clic en el botón para generar automáticamente el código de los bots. Si deseas refinar el código generado (como agregar declaraciones `expect()`), lee las secciones siguientes.

Si estás utilizando un editor de texto, ve a `tests.py`. Aquí puedes ver ejemplos de cómo definir el archivo `tests.py` para personalizar y mejorar las pruebas, incluyendo la adición de expectativas y validaciones sobre el comportamiento de los bots.


### Submitting pages

Debes hacer un `yield` por cada envío de página. Por ejemplo:

```python
# Se hace un 'yield' por cada página que el bot debe interactuar.
yield pages.Start  # El bot interactúa con la página de inicio.
yield pages.Survey, dict(name="Bob", age=20)  # El bot envía los datos del formulario de la página 'Survey'.
```

Aquí, primero enviamos la página de inicio (`Start`), que no contiene un formulario. La página siguiente tiene 2 campos de formulario, por lo que enviamos un diccionario con los datos correspondientes.

El sistema de pruebas generará un error si el bot envía datos inválidos para una página, o si envía las páginas en un orden incorrecto.

Se utilizan declaraciones `if` para jugar con cualquier número de jugador o ronda. Por ejemplo:

```python
# Si es la primera ronda, el bot interactúa con la página de introducción.
if self.round_number == 1:
    yield pages.Introduction

# Si el jugador es el primero en el grupo, hace una oferta de 30.
if self.player.id_in_group == 1:
    yield pages.Offer, dict(offer=30)
# Si el jugador no es el primero, acepta la oferta.
else:
    yield pages.Accept, dict(offer_accepted=True)
```

Tus declaraciones `if` pueden depender de `self.player`, `self.group`, `self.round_number`, etc.

Es importante **ignorar las páginas de espera** al escribir bots, ya que los bots deben proceder automáticamente sin necesidad de esperar que todos los jugadores lleguen a la página. Las páginas de espera generalmente se gestionan de forma diferente, y el bot debe continuar sin interactuar con ellas.

### Rounds

Tu código de bot debe jugar solo **1 ronda** a la vez. oTree se encargará de ejecutar el código automáticamente **NUM_ROUNDS** veces, según la configuración del número de rondas en tu experimento.

Esto significa que no es necesario incluir un ciclo para las rondas en el código del bot, ya que oTree gestionará la repetición de las rondas por ti.


### expect()

Puedes usar las declaraciones `expect` para asegurarte de que tu código está funcionando como esperas.

Por ejemplo:

```python
# Verifica que el jugador tenga 100 manzanas antes de realizar la acción.
expect(self.player.num_apples, 100)

# El bot realiza la acción de comer 1 manzana.
yield pages.Eat, dict(apples_eaten=1)

# Verifica que el número de manzanas del jugador haya disminuido a 99.
expect(self.player.num_apples, 99)

# El bot avanza a la siguiente página.
yield pages.SomeOtherPage
```

Si el valor de `self.player.num_apples` no es 99, recibirás una alerta con un error. Esto se debe a que las declaraciones `expect` verifican que el valor esperado sea el correcto, y si no es así, informarán del error.

También puedes usar `expect` con tres argumentos para realizar comparaciones. Por ejemplo, `expect(self.player.budget, '<', 100)` verificará que `self.player.budget` sea menor que 100. Los operadores que puedes usar son: '<', '<=', '==', '>=', '>', '!=', 'in', y 'not in'. Esto te permite hacer comprobaciones más complejas y validar distintos aspectos del estado de tu juego o la aplicación en función de las condiciones que definas.

### Testing form validation

Si utilizas validación de formularios, deberías probar que tu aplicación está rechazando correctamente las entradas inválidas por parte del usuario, utilizando `SubmissionMustFail()`.

Esto te permite asegurarte de que la aplicación no permita el envío de datos incorrectos o inválidos. Si el formulario contiene datos no válidos, `SubmissionMustFail()` generará un error, lo que indica que el bot ha intentado enviar datos que no cumplen con las reglas de validación definidas en el formulario.

```python
class MyPage(Page):

    # Especificamos el modelo y los campos del formulario que el jugador debe llenar
    form_model = 'player'  # El formulario está asociado al modelo 'player'
    form_fields = ['int1', 'int2']  # Los campos del formulario que se van a mostrar

    @staticmethod
    def error_message(player, values):
        # Comprobamos si la suma de los valores de 'int1' y 'int2' no es 100
        if values["int1"] + values["int2"] != 100:
            # Si la suma no es 100, mostramos un mensaje de error
            return 'The numbers must add up to 100'
```

Para probar que está funcionando correctamente, debes asegurarte de que el formulario rechace las entradas que no cumplan con la validación definida. Usando herramientas de prueba como `expect` o `SubmissionMustFail()`, puedes verificar que el mensaje de error se muestre cuando los valores no sean válidos (por ejemplo, cuando la suma no sea 100).


```python
# Primero, se verifica que la suma de los valores en 'int1' e 'int2' no sea 100,
# lo que debería generar un error de validación. El bot debe fallar al intentar
# enviar estos valores.
yield SubmissionMustFail(pages.MyPage, dict(int1=99, int2=0))

# Luego, se prueba con valores válidos, donde la suma de 'int1' e 'int2' sí sea 100,
# por lo que el bot debería proceder sin errores.
yield pages.MyPage, dict(int1=99, int2=1)
```

El bot enviará el formulario de `MyPage` dos veces. Si la primera sumisión es exitosa, se generará un error, ya que no debería haberse enviado con datos inválidos. La función `SubmissionMustFail` asegura que la primera sumisión falle, y la segunda es una prueba de que la validación funciona correctamente con datos válidos.


### Checking the HTML

`self.html` contiene el HTML de la página que estás a punto de enviar. Puedes usarlo junto con `expect()` para realizar pruebas más detalladas. Esto te permite verificar que el contenido de la página se genera correctamente antes de enviarla, asegurando que los datos o la estructura HTML cumplen con lo esperado en tu aplicación.


```python
# Si el jugador es el primero en el grupo, verificamos que 'is_winner' sea True
# y que el mensaje 'you won the game' esté presente en el HTML de la página.
if self.player.id_in_group == 1:
    expect(self.player.is_winner, True)  # Verificamos que 'is_winner' sea True
    print(self.html)  # Imprimimos el HTML para ver el contenido de la página
    expect('you won the game', 'in', self.html)  # Verificamos que el mensaje esté en el HTML
else:
    # Si el jugador no es el primero, verificamos que 'is_winner' sea False
    # y que el mensaje 'you did not win' esté presente en el HTML.
    expect(self.player.is_winner, False)  # Verificamos que 'is_winner' sea False
    expect('you did not win', 'in', self.html)  # Verificamos que el mensaje esté en el HTML

# Procedemos a la siguiente página de resultados.
yield pages.Results
```

`self.html` se actualiza con el HTML de la siguiente página después de cada declaración `yield`. Esto significa que después de cada envío, el contenido de `self.html` reflejará la estructura de la página que sigue. Los saltos de línea y los espacios extra se ignoran, por lo que la comparación de cadenas no se ve afectada por diferencias de formato visual. Esta característica es útil para verificar que el contenido de la página se genera correctamente al avanzar en el flujo del juego o la aplicación.


### Automatic HTML checks

Se generará un error si el bot intenta enviar campos de formulario que no se encuentran realmente en el HTML de la página, o si falta un botón de envío en el HTML de la página.

Sin embargo, el sistema de bots no puede ver los campos y botones que se agregan dinámicamente con JavaScript. En estos casos, debes desactivar la comprobación del HTML utilizando `Submission` con el parámetro `check_html=False`. Esto permitirá que el bot envíe la página incluso si los campos o botones no están presentes en el HTML estático inicial, sino que se agregan dinámicamente después.


```python
# El bot envía la página 'MyPage' con un diccionario que contiene el valor 'foo' igual a 99.
# Esto simula la acción de un usuario completando un formulario en esa página.
yield pages.MyPage, dict(foo=99)
```

A esto:

```python
# El bot envía la página 'MyPage' con un diccionario que contiene el valor 'foo' igual a 99.
# Se utiliza 'Submission' para enviar el formulario y se establece 'check_html=False'
# para desactivar la comprobación del HTML, lo que permite enviar la página incluso si
# los campos o botones son generados dinámicamente con JavaScript.
yield Submission(pages.MyPage, dict(foo=99), check_html=False)
```

(Si usas `Submission` sin `check_html=False`, los dos fragmentos de código serían equivalentes. Esto se debe a que la comprobación del HTML se realiza por defecto. Al desactivarla con `check_html=False`, el bot no verifica el HTML de la página antes de enviarla, lo cual es útil cuando el formulario contiene elementos generados dinámicamente con JavaScript.)


### Simulate a page timeout

Puedes usar `Submission` con el parámetro `timeout_happened=True` para simular que ha ocurrido un tiempo de espera o que el usuario ha tardado más de lo esperado para enviar la página. Esto puede ser útil para probar cómo se comporta la aplicación cuando los participantes no envían sus respuestas dentro del tiempo límite o si deseas simular una situación de retraso en la interacción del usuario.


```python
# El bot envía la página 'MyPage' con un diccionario que contiene el valor 'foo' igual a 99.
# Se utiliza 'Submission' con el parámetro 'timeout_happened=True', lo que simula que el tiempo
# de espera ha ocurrido. Esto puede ser útil para probar el comportamiento de la página cuando el
# usuario no ha enviado el formulario dentro del tiempo esperado.
yield Submission(pages.MyPage, dict(foo=99), timeout_happened=True)
```

## Actividad Práctica: Asset Market Teams






## NOTA

Para la nota del taller de la sesión deben interactuar con mínimo 2 jugadores (1 grupos) e interactuar con ellos, deben generar el archivo `.otreezip` enviarlo al profesor Ferley `heiner.rincon@urosario.edu.co` con el asunto `Taller sesión 7`, y con copia a Jorge `hopkeinst@gmail.com`.

Cualquier error que presenten, pueden consultar a Jorge por correo electrónico o chat.

## Bibliografía

Aquí tienes la bibliografía en el formato solicitado:

<ol>
    <li id="bib_01"> Chen, D.L., Schonger, M., & Wickens, C., “oTree – An Open-Source Platform for Laboratory, Online, and Field Experiments,” <em>Journal of Behavioral and Experimental Finance</em>, vol. 9, pp. 88-97, 2016. [Online]. Available: <a href="https://doi.org/10.1016/j.jbef.2015.12.001">https://doi.org/10.1016/j.jbef.2015.12.001</a>. [Accessed: 11-Nov-2024].</li>
    <li id="bib_02"> McClelland, G.H., “oTree Documentation: Bots.” [Online]. Available: <a href="https://otree.readthedocs.io/en/latest/bots.html">https://otree.readthedocs.io/en/latest/bots.html</a>. [Accessed: 11-Nov-2024].</li>
    <li id="bib_03"> McClelland, G.H., “oTree Documentation: Live Pages.” [Online]. Available: <a href="https://otree.readthedocs.io/en/latest/live.html">https://otree.readthedocs.io/en/latest/live.html</a>. [Accessed: 11-Nov-2024].</li>
    <li id="bib_04"> Holt, C.A., <em>Markets, Games, & Strategic Behavior</em>. New York, NY: Pearson Education, 2006.</li>
    <li id="bib_05"> oTree Project, “oTree Documentation.” [Online]. Available: <a href="https://otree.readthedocs.io/en/latest/">https://otree.readthedocs.io/en/latest/</a>. [Accessed: 11-Nov-2024].</li>
    <li id="bib_06"> oTree Project, “oTree GitHub Repository.” [Online]. Available: <a href="https://github.com/oTree-org/otree">https://github.com/oTree-org/otree</a>. [Accessed: 11-Nov-2024].</li>
</ol>



