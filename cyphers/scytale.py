from cyphers.base import CryptoBase
import numpy as np

# scytale as a matrix; unraveled column wise
#   H | O | W
#  ---|---|---
#   D | O | E
#  ---|---|---
#   S | T | H
#  ---|---|---
#   I | S | W
#  ---|---|---
#   O | R | K
# linear adressing is row-column wise
# transposed indexing inverts i and j in equation


class Scytale(CryptoBase):
    def encrypt(x, w):
        return "".join(np.array(list(x)).reshape((len(x) // w, w)).T.ravel())
    
    def encrypt2(x, w):
        n = len(x)
        assert n % w == 0
        h = n // w
        cypher = ["-"] * n
        for i, c in enumerate(x):
            row = i // w
            col = i % w
            cypher[row + col * h] = c
        return "".join(cypher)
    
    def encrypt3(x, w):
        n = len(x)
        assert n % w == 0
        h = n // w
        cypher = ["-"] * n
        it = iter(x)
        for row in range(h):
            for col in range(w):
                cypher[row + col * h] = next(it)
        return "".join(cypher)
    
    def decrypt(x, w):
        return Scytale.encrypt(x, len(x) // w)

    
def visualize(x, h, w):
    matrix = []
    for j in range(h):
        print(x[j: j + h * w: h])

