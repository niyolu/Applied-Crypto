from itertools import chain
from .base import Alphabet_Base

class Latin(Alphabet_Base):
    symbols = list(map(chr, range(ord("A"), ord("Z") + 1)))
    
class FullLatin(Alphabet_Base):
    symbols = list(chain(
        map(chr, range(ord("A"), ord("Z") + 1)),
        map(chr, range(ord("a"), ord("z") + 1)),
    ))

def test_Latin():
    assert Latin.ord("A") == 0
    assert Latin.ord("Z") == 25
    assert Latin.chr(0) == "A"
    assert Latin.chr(25) == "Z"
    assert len(Latin) == 26
    assert Latin.delim == " "
    
if __name__ == "__main__":
    test_Latin()