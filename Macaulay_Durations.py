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


def dmac_bond(F, r, n, i, C):
    if F == find_bond_price(F, r, n, i, C):
        return annuity_due_PV(i, n)
    return ((F * r * increasing_annuity_immediate_PV(i, n)) + (n * C * v(i, n))) / find_bond_price(F, r, n, i, C)