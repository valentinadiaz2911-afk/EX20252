from otree.api import *


doc = """
Juego de Public Goods
"""


class C(BaseConstants):
    NAME_IN_URL = 'publicGoods'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(10000)
    MULTIPLIER = 2


class Subsession(BaseSubsession):
    pass
    
    
class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min = 0,
        max = C.ENDOWMENT,
        label = "Con cuanto dinero quiere contribuir a la bolsa común ?"
    )


## FUNCTIONS

def set_payoffs(group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (group.total_contribution * C.MULTIPLIER) / C.PLAYERS_PER_GROUP
    for p in players:
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share

# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


class Contribucion(Page):
    form_model = "player"
    form_fields = ["contribution"]


page_sequence = [Contribucion, ResultsWaitPage, Results]
