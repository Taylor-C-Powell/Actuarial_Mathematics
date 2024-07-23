from Annuities import *
from TVM_Functions import *


def find_bond_price(F, r, n, i, C):
    if r == i:
        return F
    return (F * r * annuity_immediate_PV(i, n)) + (C * v(i, n))
