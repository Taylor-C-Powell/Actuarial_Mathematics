from Annuities import *
from TVM_Functions import *
from Bonds import *


def dmac_inflows(i):
    num_of_inflows = int(input("Please input the number of cash inflows: "))
    numerator = 0
    denominator = 0
    for inflow in range(num_of_inflows):
        p = float(input("Please input the price of inflow " + str(1 + inflow) + ": "))
        t = float(input("Please input the time-value of inflow " + str(1 + inflow) + ": "))
        numerator += (t * p * v(i, t))
        denominator += (p * v(i, t))
    return numerator / denominator


def dmod_inflows(i):
    return dmac_inflows(i) / (1 + i)


def dmac_bond(F, r, n, i, C):
    if F == find_bond_price(F, r, n, i, C):
        return annuity_due_PV(i, n)
    return ((F * r * increasing_annuity_immediate_PV(i, n)) + (n * C * v(i, n))) / find_bond_price(F, r, n, i, C)


def dmac_mortgage(n, i):
    return increasing_annuity_immediate_PV(i, n) / annuity_immediate_PV(i, n)


def dmac_perpetuity_immediate(i):
    return (1 + i) / i

def dmac_perpetuity_due(i):
    return 1 / i