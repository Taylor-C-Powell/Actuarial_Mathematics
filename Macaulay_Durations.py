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


def cmac_inflows(i):
    num_of_inflows = int(input("Please input the number of cash inflows: "))
    numerator = 0
    denominator = 0
    for inflow in range(num_of_inflows):
        p = float(input("Please input the price of inflow " + str(1 + inflow) + ": "))
        t = float(input("Please input the time-value of inflow " + str(1 + inflow) + ": "))
        numerator += (pow(t, 2) * p * v(i, t))
        denominator += (p * v(i, t))
    return numerator / denominator


def cmod_inflows(i):
    num_of_inflows = int(input("Please input the number of cash inflows: "))
    numerator = 0
    denominator = 0
    for inflow in range(num_of_inflows):
        p = float(input("Please input the price of inflow " + str(1 + inflow) + ": "))
        t = float(input("Please input the time-value of inflow " + str(1 + inflow) + ": "))
        numerator += ((t * (t + 1)) * p * v(i, t + 2))
        denominator += (p * v(i, t))
    return numerator / denominator


def dmac_bond(F, r, n, i, C):
    if F == find_bond_price(F, r, n, i, C):
        return annuity_due_PV(i, n)
    return ((F * r * increasing_annuity_immediate_PV(i, n)) + (n * C * v(i, n))) / find_bond_price(F, r, n, i, C) / 2


def dmod_bond(F, r, n, i, C):
    return dmac_bond(F, r, n, i, C) / (1 + i)


def cmac_bond(F, r, n, i, C):
    numerator = 0
    for period in range(n - 1):
        numerator += pow(period + 1, 2) * (F * r) * v(i, period + 1)
    numerator += pow(n, 2) * ((F * r) + C) * v(i, n)
    return numerator / find_bond_price(F, r, n, i, C)


def cmod_bond(F, r, n, i, C):
    return (cmac_bond(F, r, n, i, C) + dmac_bond(F, r, n, i, C)) / pow(1 + i, 2)


def dmac_annuity(n, i):
    return increasing_annuity_immediate_PV(i, n) / annuity_immediate_PV(i, n)


def dmac_perpetuity_immediate(i):
    return (1 + i) / i


def dmac_perpetuity_due(i):
    return 1 / i


def first_order_modified_approximation(price_initial, interest_rate_initial, new_interest_rate):
    return price_initial - (
                dmod_bond(1000, 0.07, 4, 0.06, 1000) * price_initial * (new_interest_rate - interest_rate_initial))


def first_order_macaulay_approximation(price_initial, interest_rate_initial, new_interest_rate):
    return price_initial * pow((1 + interest_rate_initial) / (1 + new_interest_rate),
                               dmac_bond(1000, 0.07, 4, 0.06, 1000))
