from utils.logg import logg


@logg
def equal(a: object, b: object, msg: str = '') -> any:
    if a == b:
        return f"Assert equal: {a} == {b}"
    else:
        raise AssertionError(f"equal: {a} != {b}. {msg}")

@logg
def is_in(a: object, b: object, msg: str = '') -> any:
    if a in b:
        return f"Assert in: {a} in {b}"
    else:
        raise AssertionError(f"in: {a} not in {b}. {msg}")