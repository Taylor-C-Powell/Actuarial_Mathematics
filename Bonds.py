from Annuities import *
from TVM_Functions import *


def find_bond_price(F, C, r, i, n):
    return (F * r * annuity_immediate_PV(i, n)) + (C * v(i, n))
