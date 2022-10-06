from cyphers.caesar import Caesar
from tests.testutils import test_cypher
    
def test():
    msg = "Hallo Crypto World".upper()
    test_cypher(Caesar.encrypt, Caesar.decrypt, msg)

if __name__ == "__main__":
    test()