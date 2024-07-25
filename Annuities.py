from TVM_Functions import *

def annuity_immediate_PV(i, n):
    # Calculates the present value of an annuity immediate: "a, angle(n)"
    return (1 - pow((1 / (1 + i)), n)) / i


def annuity_immediate_AV(i, n):
    # Calculates the accumulated value of an annuity immediate: "s, angle(n)"
    return (pow((1 + i), n) - 1) / i


def annuity_due_PV(i, n):
    # Calculates the present value of an annuity due: "a dot dot, angle(n)"
    return 1 + annuity_immediate_PV(i, n - 1)


def annuity_due_AV(i, n):
    # Calculates the accumulated value of an annuity due: "s dot dot, angle(n)"
    return annuity_immediate_AV(i, n + 1) - 1


def increasing_annuity_immediate_PV(i, n):
    return (annuity_due_PV(i, n) - (n * v(i, n))) / i


def perpetuity_immediate(i):
    return 1 / i