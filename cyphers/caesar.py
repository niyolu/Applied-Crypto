from cyphers.base import CryptoBase
from alphabets.latin import Latin
    
class Caesar(CryptoBase):
    def encrypt(x: str, n: int = 3) -> str:
        def encrypt_char(c: str):
            return Latin.chr((Latin.ord(c) + n) % len(Latin))
        return "".join([encrypt_char(c) if c != Latin.delim else c for c in x])

    def decrypt(x: str, n: int = 3) -> str:
        return Caesar.encrypt(x, -n)