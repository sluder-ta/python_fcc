# import some of the tools I'll need
from sys import exit
from random import randint
from textwrap import dedent

#import the ability to create monsters - I would like to give them random stats at their creation
import Monsters

class Labour(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

# labour 1
class NemeanLion(Labour):
    pass

# labour 2
class LernaeanHydra(Labour):
    pass

# labour 3
class CeryneianHind(Labour):
    pass

# labour 4
class ErymanthianBoar(Labour):
    pass

# labour 5
class AugeanStables(Labour):
    pass

# labour 6
class StymphalianBirds(Labour):
    pass

# labour 7
class CretanBull(Labour):
    pass

# labour 8
class MaresOfDiomedes(Labour):
    pass

# labour 9
class GirdleOfHippolyta(Labour):
    pass

# labour 10
class ApplesOfTheHesperides(Labour):
    pass

# labour 11
class CattleOfGeryon(Labour):
    pass

# labour 12
class CaptureCerebrus(Labour):
    pass

labours = {
    'slay the nemean lion': NemeanLion(),
    'slay the lernaean hydra': LernaeanHydra(),
    'capture the ceryneian hind': CeryneianHind(),
    'capture the erymanthian boar': ErymanthianBoar(),
    'clean the augean stables': AugeanStables(),
    'slay the stymphalian birds': StymphalianBirds(),
    'capture the cretan bull': CretanBull(),
    'steal the mares of diomedes': MaresOfDiomedes(),
    'obtain the girdle of hippolyta': GirdleOfHippolyta(),
    'obtain the cattle of geryon': CattleOfGeryon(),
    'steal the apples of hesperides': ApplesOfTheHesperides(),
    'capture cerberus': CaptureCerebrus()
}