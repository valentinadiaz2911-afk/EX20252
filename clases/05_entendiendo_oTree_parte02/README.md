# Entendiendo oTree Parte 2: Models - Prisoner

Después de haber visto en nuestra [sesión anterior](../04_entendiendo_oTree_parte01/README.md) la jerarquía de trabajo de oTree así como desarrollado el juego de 'Adivinar 2/3 del promedio' ahora vamos a adentrarnos un poco más y poder personalizar de mejor manera las actividades dentro de un experimento. Para ello, en esta sesión trabajaremos con los Modelos o `Models`.

Pero, antes de hablar de ello, es necesario recapitular en lo siguiente:

![zurich_01](../../imgs/05/001.png)<sup><a href="#bib_01">1</a></sup>

Nuestro objetivo con los experimentos, desde una perspectiva computacional, es eso: Mostrarle algo al participante y obtener su reacción/interacción.

Esta obtención de interacción se puede hacer de muchas maneras y no podemos limitarnos a que sean solamente cosas que hace el participante como ingresar un nombre, un número, presionar un botón; también son datos que el participante no ingresa pero con lo cual si participa activamente: cuánto tiempo le demoró en escoger una respuesta, escogió varias respuestas, miró más a una parte de la pantalla, pasó más el mouse por un sector que por otro de la pantalla.

Todos estos datos _(lista de opciones, tiempos, verdadero/falso, etc)_ nos son muy útiles para validar o no las teorías que tengamos y poder generar mejores conclusiones a través de su respectivo análisis.

Ahora bien **¿ Cómo lo podemos hacer con oTree ?** Usando modelos. Los modelos son representaciones de nuestros datos en la base de datos, y estos modelos son los que lo almacenan, por eso son tan importantes. En la actualidad y por defecto oTree tiene los modelos de Participant, Player, Session, Subsession y Group. Se pueden crear más, pero para la gran mayoría de actividades y situaciones estos son de ayuda

## Bibliografía

<ol>
    <li id="bib_01"> oTree, “Conceptual overview” oTree Documentation. [Online]. Available: <a href="https://otree.readthedocs.io/en/latest/models.html">https://otree.readthedocs.io/en/latest/models.html</a>. [Accessed: 07-Sep-2024].
    <li id="bib_02"> Philipp Chapkovski, “Zurich workshop on online experiments” Repositorio de GitHub. [Online]. Available: <a href="https://github.com/chapkovski/zurich-workshop">https://github.com/chapkovski/zurich-workshop</a>. [Accessed: 08-Sep-2024].
    <li id="bib_03">Wikipedia, “Dilema del prisionero” Wikipedia. [Online]. Available:  <a href="https://es.wikipedia.org/wiki/Dilema_del_prisionero">https://es.wikipedia.org/wiki/Dilema_del_prisionero</a>. [Accessed: 08-Sep-2024].
</ol>
