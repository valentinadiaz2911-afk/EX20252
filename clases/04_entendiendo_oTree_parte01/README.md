# Entendiendo oTree Parte 1: Session, Subsession, Group, Player

Después de haber desarrollado en nuestra [sesión anterior](../03_groups_publicGoods_trust_games/README.md) 2 juegos, haberlos ejecutado y capturar datos, podemos observar trabajo en grupos.

Ahora vamos a hacer un análisis mejor de cómo es el funcionamiento, de manera jerárquica, de las variables, grupos, el experimento en general, etc.

Para esto tendremos:

1. <a href="#sesión">Sesión</a>
2. Subsesión
3. Grupo
4. Página
5. Participante
6. Jugador

Los 4 primeros se pueden agrupar como maneras en que se pueden visualizar y asociar la interacción _(Sesión, Subsesión, Grupo, Página)_ mientras los dos últimos se trata sobre las personas _(Participante, Jugador)_.

## Por interacción

Como ya se ha mencionado una de las maneras en que se establece una interacción es a través de la sesión, subsesión, grupo o página.

Esta interacción, **y es muy importante** tiene que ver con la lógica del negocio _(en palabras de un desarrollador, programador o ingeniero de sistemas)_ o sea, con cómo se es el paso a paso, el actuar / accionar, los datos que se esperan recoger, el momento / tiempo, etc.

Una gráfica que nos puede ayudar a entender esto sería la siguiente:

![session_subsession_pages](../../imgs/04/001.webp)<sup><a href="#bib_01">1</a></sup>

### Sesión

La sesión es todo el evento que consiste en un experimento completo. Durante este varios participantes realizan una serie de juegos, actividades o aplicaciones.

![session_01](../../imgs/04/002.png)<sup><a href="#bib_02">2</a></sup>

![session_02](../../imgs/04/004.png)<sup><a href="#bib_02">2</a></sup>

Una sesión puede contener una cantidad `n` de juegos o aplicaciones ordenadas _(recuerden 'app_sequence' en el archivo `settings.py`)_.

Un ejemplo de una sesión sería citar a varios participantes y que realicen un juego de bienes públicos, seguidos de un juego de confianza y terminando en una encuesta _(3 aplicaciones en total: 2 juegos + encuesta)_.

![session_appSequence](../../imgs/04/003.png)

### Subsesión

Cada subsesión es cada una de las aplicaciones o juegos o actividades que hagan parte de la sesión, y por ronda. O sea si tuviésemos un juego de confianza y se hacen 2 rondas de este, habrían 2 subsesiones de este juego.

![subsession](../../imgs/04/005.png)<sup><a href="#bib_02">2</a></sup>

### Grupo

Un grupo es un conjunto de jugadores de una subsesión.

![group](../../imgs/04/006.png)<sup><a href="#bib_02">2</a></sup>

Por ejemplo, si tenemos una subsesión con 20 jugadores y formamos grupos de 2 personas para le juego de confianza, se forman 10 grupos. A cada jugador dentro del grupo se le puede dar un identificador dentro de este _(jugador # 1, jugador # 2, jugador # 3)_ pero que es exclusivo dentro de ese grupo.

> **Nota:** Los grupos se pueden aleatorizar entre cada subsesión, sin importar que sean el mismo juego. Siguiendo con el juego de confianza de 2 rondas, las parejas para cada ronda se pueden aleatorizar, entonces, para la primera ronda se puede formar un grupo con los jugadores A - B y otro con los jugadores C - D; pero para la ronda 2 los grupos pueden ser A - D y B - C.

### Página

Es la unidad más mínima de interacción y como su nombre lo dice, es cada una de las páginas que vemos, con la que los jugadores interactúan.

En estas se colocan los formularios para capturar los datos, se ponen tablas para visualizar información, letreros y etiquetas para obtener retroalimentación, etc.

Son nuestros archivos en formato `.html` y dentro de los cuales usamos llaves para llamar variables o interactuar con estas: `{{ formfields }}`, `{{ player.edad }}`, `{{ C.MULTIPLIER }}`, `{{ group.total_contribution }}`, etc.

## Por persona

Otra jerarquía que existe en oTree es por personas, en donde es importante tener en cuenta que Participante y Jugador están relacionados pero no son iguales porque uno contiene al otro _(el participante contiene al jugador)_.

![participant_player](../../imgs/04/007.webp)<sup><a href="#bib_01">1</a></sup>

### Participante

El participante es la persona que asiste al laboratorio y es la misma a lo largo de toda la sesión sin importar subsesión o aplicaciones o rondas.

![participant_01](../../imgs/04/008.png)<sup><a href="#bib_02">2</a></sup>

Lo ideal es identificar al participante mediante un código o ID para tener en cuenta al final y poder relacionar la recompensa a pagarle, para el consentimiento, etc.

![participant_02](../../imgs/04/009.png)<sup><a href="#bib_02">2</a></sup>

### Jugador

El jugador es el nombre que se le da al participante durante cada subsesión.

![player](../../imgs/04/010.png)<sup><a href="#bib_02">2</a></sup>

Como cada subsesión es diferente _(porque es una aplicación diferente, es una ronda diferente, es una encuesta, etc)_ es aquí donde usamos dentro del archivo `__init__.py` la parte de **Player** para generar variables en donde vamos a guardar los datos a recolectar de la interacción de la persona.

## Trabajo de práctica: Adivinando 2/3 del promedio

Para poner en práctica los conceptos vistos, vamos a realizar un juego conocido como 'Adivina 2/3 del promedio' _(Guess 2/3 of the average)_. <sup><a href="#bib_03">3</a></sup> Aquí se tiene una cantidad de jugadores por grupo, y a cada jugador se le da la oportunidad que de un número entre 0 y el valor máximo, luego se calcula 2/3 del promedio de los números del grupo, y quien más se acerque se lleva el premio.



## Bibliografía

<ol>
    <li id="bib_01"> oTree, “Conceptual overview” oTree Documentation. [Online]. Available: <a href="https://otree.readthedocs.io/en/latest/conceptual_overview.html">https://otree.readthedocs.io/en/latest/conceptual_overview.html</a>. [Accessed: 12-Aug-2024].
    <li id="bib_02"> Philipp Chapkovski, “Zurich workshop on online experiments” Repositorio de GitHub. [Online]. Available: <a href="https://github.com/chapkovski/zurich-workshop">https://github.com/chapkovski/zurich-workshop</a>. [Accessed: 02-Sep-2024].
    <li id="bib_03">Wikipedia, “Adivina 2/3 del promedio” Wikipedia. [Online]. Available:  <a href="https://es.wikipedia.org/wiki/Adivina_2/3_del_promedio">https://es.wikipedia.org/wiki/Adivina_2/3_del_promedio</a>. [Accessed: 03-Sep-2024].
</ol>

