from cyphers.skytale import Skytale, visualize
from tests.testutils import test_cypher

def test():
    msg = "HOWDOESTHISWORK"
    w, h = 3, 5
    test_cypher(Skytale.encrypt, Skytale.decrypt, msg, w)
    visualize(Skytale.encrypt(msg, w), h, w)
    visualize(Skytale.decrypt(Skytale.encrypt(msg, w), w), w, h)
    
if __name__ == "__main__":
    test()
