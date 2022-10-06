from abc import ABC, abstractclassmethod

class CryptoBase(ABC):
    @abstractclassmethod
    def encrypt(x: str) -> str:
        pass
    
    @abstractclassmethod
    def decrypt(x: str) -> str:
        pass