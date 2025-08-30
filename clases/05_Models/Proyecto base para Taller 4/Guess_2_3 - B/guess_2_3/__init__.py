from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    # Necesarias para el juego
    PLAYERS_PER_GROUP = 3 # Van a ser 3 jugadores por grupo
    NUM_ROUNDS = 3 # Van a ser 3 rondas en total del juego
    NAME_IN_URL = 'guess_2_3' # Nombre que se colocará en la URL (navegador web) para el juego
    # Dependientes del juego
    VALOR_MAXIMO = 100 # Cada jugador podrá colocar un valor entre 0 y 100
    BOTE_GANANCIAS = cu(0) # El jugador que quede más cerca del valor promedio ganará 10.000 puntos


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    dos_tercios_promedio = models.FloatField() # Para almacenar los dos tercios del promedio
    mejor_estimacion = models.IntegerField() # Para almacenar la mejor estimación de los jugadores
    n_ganadores = models.IntegerField() # Para almacenar la cantidad de ganadores


class Player(BasePlayer):
    estimacion = models.IntegerField(
         = 0, # Aquí el valor mínimo que puede ingresar un jugador es 0
         = C.VALOR_MAXIMO, # Con esto se establece que el valor máximo que puede ingresar un jugador es el establecido arriba en constantes como 'VALOR_MAXIMO'
         = "Escoja un valor entre 0 y 100:" # Es lo que se va a mostrar al jugador cuando vaya a ingresar su estimación
    )
    es_ganador = models.BooleanField() # Es para almacenar si un jugador fue ganador o no


# FUNCTIONS
def set_payoffs(group: Group):
    players = 
    estimaciones = [p.estimacion for p in players]
    dos_tercios_promedio = (2 / 3) * sum(estimaciones) / len(players)
    group.dos_tercios_promedio = round(dos_tercios_promedio, 2)
    group.mejor_estimacion = min(estimaciones, key=lambda estimacion: abs(estimacion - group.dos_tercios_promedio))
    ganadores = [p for p in players if p.estimacion == group.mejor_estimacion]
    group.n_ganadores = len(ganadores)
    for p in ganadores:
        p.es_ganador = True
        p.payoff = C.BOTE_GANANCIAS / group.n_ganadores


def historico_promedio_2_3(group: Group):
    return [g.dos_tercios_promedio for g in group.in_previous_rounds()]

# PAGES
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Instrucciones(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Estimacion(Page):
    form_model = 'player' # El modelo del cual vamos a recolectar datos
    form_fields = ['estimacion'] # La variable que vamos a recolectar, en este caso, de Player

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(historico_promedio_2_3=historico_promedio_2_3(group))


class Resultados(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        estimaciones_ordenadas = sorted(p.estimacion for p in group.get_players())
        return dict(estimaciones_ordenadas=estimaciones_ordenadas)


page_sequence = [Instrucciones, Estimacion, ResultsWaitPage, Resultados]
