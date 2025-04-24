# import some of the tools I'll need
from sys import exit
from random import randint
from textwrap import dedent

#import the ability to create monsters - I would like to give them random stats at their creation
import Monsters

class Labours(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)