from itertools import chain
from .base import Alphabet_Base

# TODO: string.lower_ascii
class Latin(Alphabet_Base):
    symbols = list(map(chr, range(ord("A"), ord("Z") + 1)))
    
class FullLatin(Alphabet_Base):
    symbols = list(chain(
        map(chr, range(ord("A"), ord("Z") + 1)),
        map(chr, range(ord("a"), ord("z") + 1)),
    ))