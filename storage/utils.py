def merge(x, y: dict) -> dict:
    z = x.copy()
    z.update(y)

    return z