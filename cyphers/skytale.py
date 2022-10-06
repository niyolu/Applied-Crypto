from cyphers.base import CryptoBase

# skytale as a table is wound along its columns
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


class Skytale(CryptoBase):
    def encrypt2(x, w):
        n = len(x)
        assert n % w == 0
        h = n // w
        cypher = ["-"] * n
        for i in range(n):
            row = i // w
            col = i % w
            cypher[row + col * h] = x[i]
        return "".join(cypher)
    
    def encrypt(x, w):
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
        return Skytale.encrypt(x, len(x) // w)
    
def visualize(x, h, w):
    matrix = []
    n = len(x)
    for j in range(h):
        print(x[j: j + h * w: h])
            

    



    