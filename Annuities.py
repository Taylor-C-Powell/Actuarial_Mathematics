def calculate_annuity_immediate_PV(interest_rate, accumulation_periods):
    # Calculates the present value of an annuity immediate: "a, angle(n)"
    return (1 - pow((1 / (1 + interest_rate)), accumulation_periods)) / interest_rate


def calculate_annuity_immediate_AV(interest_rate, accumulation_periods):
    # Calculates the accumulated value of an annuity immediate: "s, angle(n)"
    return (pow((1 + interest_rate), accumulation_periods) - 1) / interest_rate


def calculate_annuity_due_PV(interest_rate, accumulation_periods):
    # Calculates the present value of an annuity due: "a dot dot, angle(n)"
    return 1 + calculate_annuity_immediate_PV(interest_rate, accumulation_periods - 1)


def calculate_annuity_due_AV(interest_rate, accumulation_periods):
    # Calculates the accumulated value of an annuity due: "s dot dot, angle(n)"
    return calculate_annuity_immediate_AV(interest_rate, accumulation_periods + 1) - 1