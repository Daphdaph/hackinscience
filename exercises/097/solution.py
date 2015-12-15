def love_meet(bob, alice):
    a = set(bob) & set(alice)
    return a


def affair_meet(bob, alice, silvester):
    a = set(alice) & set(silvester)
    b = set(bob)
    c = a - b
    return c
