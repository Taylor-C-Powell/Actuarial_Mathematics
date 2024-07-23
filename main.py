from Annuities import *
from TVM_Functions import *

def calculate_compound_interest(interest_rate, accumulation_periods):
    return pow((1 + interest_rate), accumulation_periods)





def calculate_num_of_level_payments(previous_value, interest_rate, amount):
    # calculates how many level payments can be made until the fund is depleted
    # also calculates the value of the final payment (which is smaller than the level payments)
    count = 0
    while previous_value > amount:
        previous_value = (previous_value * (1 + interest_rate)) - amount
        count += 1
    print("count: ", count)
    print("final payment: ", previous_value)


def calculate_num_of_increasing_payments(previous_value, interest_rate, initial_payment, amount_of_increase):
    # calculates how many payments can be made until the fund is depleted
    # payments increase at a fixed amount each payment period
    # also calculates the value of the final payment
    count = 0
    payment = initial_payment
    while previous_value > payment:
        previous_value = (previous_value * (1 + interest_rate)) - payment
        payment += amount_of_increase
        count += 1
    print(previous_value)





def find_bond_price(F, C, r, i, n):
    return (F * r * annuity_immediate_PV(i, n)) + (C * v(i, n))


x = annuity_due_PV(0.08, 8)
print(x)
