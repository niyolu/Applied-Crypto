def test_cypher(enc, dec, msg, *args):
    encryped = enc(msg, *args)
    decrypted = dec(encryped, *args)
    print(msg, encryped, decrypted, sep="\n|\nV\n")
    assert msg == decrypted
    