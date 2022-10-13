from alphabets.latin import Latin

def test_Latin():
    assert Latin.ord("A") == 0
    assert Latin.ord("Z") == 25
    assert Latin.chr(0) == "A"
    assert Latin.chr(25) == "Z"
    assert len(Latin) == 26
    assert Latin.delim == " "
    
if __name__ == "__main__":
    test_Latin()