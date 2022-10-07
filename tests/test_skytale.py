from cyphers.scytale import Scytale, visualize
from tests.testutils import test_cypher

def test():
    msg = "HOWDOESTHISWORK"
    w, h = 3, 5
    test_cypher(Scytale.encrypt, Scytale.decrypt, msg, w)
    visualize(Scytale.encrypt(msg, w), h, w)
    visualize(Scytale.decrypt(Scytale.encrypt(msg, w), w), w, h)
    
if __name__ == "__main__":
    test()
