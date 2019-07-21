def triplet(atuple):
    for id1, x0 in enumerate(atuple):
        for id2, x1 in enumerate(atuple):
            for id3, x2 in enumerate(atuple):
                if id1 != id2 and id1 != id3 and id2 != id3:
                    if x0 + x1 + x2 == 0:
                        result = (x0, x1, x2)
                        return result
                    else:
                        result = ()
    return result