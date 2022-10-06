from abc import ABC, abstractclassmethod
from .alphabets.latin import Latin

class CryptoBase(ABC):
    @abstractclassmethod
    def encrypt(x: str) -> str:
        pass
    
    @abstractclassmethod
    def decrypt(x: str) -> str:
        pass
    
class Caesar(CryptoBase):
    def encrypt(x: str, n: int = 3) -> str:
        def encrypt_char(c: chr):
            return Latin.chr((Latin.ord(c) + n) % len(Latin))
        return "".join([encrypt_char(c) if c != Latin.delim else c for c in x])
    
    def decrypt(x: str, n: int = 3) -> str:
        def decrypt_char(c: chr):
            return Latin.chr((Latin.ord(c) - n) % len(Latin))
        return "".join([decrypt_char(c) if c != Latin.delim else c for c in x])
    
    
def test_caesar():
    msg = "Hallo Crypto World".upper()
    encryped = Caesar.encrypt(msg)
    decrypted = Caesar.decrypt(encryped)
    print(msg, encryped, decrypted, sep="\n|\nV\n")
    assert msg == decrypted

if __name__ == "__main__":
    test_caesar()
    