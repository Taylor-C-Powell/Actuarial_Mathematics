from Annuities import *
from TVM_Functions import *

def Dmac_of_inflows(i):
    num_of_inflows = int(input("Please input the number of cash inflows: "))
    numerator = 0
    denominator = 0
    for inflow in range(num_of_inflows):
        p = float(input("Please input the price of inflow " + str(1 + inflow) + ": "))
        t = float(input("Please input the time-value of inflow " + str(1 + inflow) + ": "))
        numerator += (t * p * v(i, t))
        denominator += (p * v(i, t))
    return numerator / denominator

