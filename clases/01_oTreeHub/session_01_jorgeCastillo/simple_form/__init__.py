
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'simple_form'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    edad = models.IntegerField()
    nombre = models.StringField()
class Form_01(Page):
    form_model = 'player'
    form_fields = ['nombre', 'edad']
class Results_01(Page):
    form_model = 'player'
page_sequence = [Form_01, Results_01]