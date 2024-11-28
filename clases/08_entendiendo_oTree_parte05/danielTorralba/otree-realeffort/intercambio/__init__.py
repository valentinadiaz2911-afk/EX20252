from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'intercambio'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    intercambio = models.IntegerField(label='Ingrese el aporte que desea reconocerle a su empleado:')


class Player(BasePlayer):
    agree = models.BooleanField()
    correcta_empleado = models.IntegerField()
    payoff_complete = models.IntegerField()


def creating_session(self):
    for group in self.get_groups():
        for player in group.get_players():
            if (player.id_in_group == 1):
                player.agree = random.choice([True, False])
            else:
                player.agree = not player.get_others_in_group()[0].agree

# PAGES

class Intercambio(Page):
    form_model = 'group'
    form_fields = ['intercambio']

    @staticmethod
    def is_displayed(player: Player):
        return player.agree 
    
    def vars_for_template(player: Player):
        pass
    
    def before_next_page(player: Player, timeout_happened):
        pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(group: Group):
        pass


class Results(Page):
    form_model = 'player'
    
    @staticmethod
    def vars_for_template(player: Player):
        payoff_complete = player.payoff_complete
        return{
            'payoff_complete': payoff_complete
        }


page_sequence = [Intercambio, ResultsWaitPage, Results]
