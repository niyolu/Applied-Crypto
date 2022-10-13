import timeit
from functools import partial


def test_cypher(enc, dec, msg, *args, name="Cypher", verbose=True):
    encrypted = enc(msg, *args)
    decrypted = dec(encrypted, *args)
    assert msg == decrypted
    if verbose:
        print(
            f"{name} test case successfull\n"
            f"result: {' -> '.join((msg, encrypted, decrypted))}"
        )
    
def bench_cypher(enc, dec, msg, *args, name="Cypher", n=10_000, r=3, verbose=False):
    time_f = partial(time, n=n, r=r)
    enc_f = partial(enc, msg, *args)
    encrypted = enc_f()
    dec_f = partial(dec, encrypted, *args)
    decrypted = dec_f()
    encryption_time_ms = time_f(enc_f) * 1000
    decryption_time_ms = time_f(dec_f) * 1000
    if verbose:
        print(
            f"{name} benchmark results:\n"
            f"encryption: {encryption_time_ms:.2f}ms\t"
            f"decryption: {decryption_time_ms:.2f}ms\n"
            f"result: {' -> '.join((msg, encrypted, decrypted))}"
        )
    return encryption_time_ms, decryption_time_ms
    
def time(f, n=100_000, r=3):
    return min(timeit.repeat(f, number=n, repeat=r)) / n
