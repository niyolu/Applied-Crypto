DEFAULT_DELIM = " "

class Alphabetmeta(type):
    def __new__(cls, clsname, bases, attrs):
        try:
            symbols = attrs["symbols"]
        except KeyError:
            return super().__new__(cls, clsname, bases, attrs)
        del attrs["symbols"]
        attrs["_idx2symbols"] = symbols
        attrs["_symbols2idx"] = {utf: idx for idx, utf in enumerate(map(ord, symbols))}
        attrs["_symbol_len"] = len(symbols)
        attrs["delim"] = attrs.get("delim", DEFAULT_DELIM)
        attrs["ord"] = classmethod(lambda ctx, s: getattr(ctx, "_symbols2idx")[ord(s)])
        attrs["chr"] = classmethod(lambda ctx, i: getattr(ctx, "_idx2symbols")[i])
        return super().__new__(cls, clsname, bases, attrs)
    
    def __len__(self):
        return self._symbol_len
    
class Alphabet_Base(metaclass=Alphabetmeta):
    pass