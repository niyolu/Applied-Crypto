from cyphers.scytale import Scytale, visualize
from tests.testutils import test_cypher, bench_cypher


def test():
    msg = "HOWDOESTHISWORK"
    w, h = 3, 5
    test_cypher(Scytale.encrypt, Scytale.decrypt, msg, w, verbose=True)
    print("cypher visualization:")
    visualize(Scytale.encrypt(msg, w), h, w)
    visualize(Scytale.decrypt(Scytale.encrypt(msg, w), w), w, h)
    
def bench():
    msg = "HOWDOESTHISWORK"*100
    w = len(msg) // 5
    return bench_cypher(Scytale.encrypt, Scytale.decrypt, msg, w, name="scytale", verbose=True)

    
if __name__ == "__main__":
    test()
    print()
    bench()
