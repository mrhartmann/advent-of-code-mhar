import numpy as np

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def input_parser(test_input):

    test_inputs = test_input.split('\n')
    signal_histories = []
    for sig in test_inputs:
        signal_histories.append(np.array([int(i) for i in sig.split(" ")]))

    return signal_histories


# SIGNALS = input_parser(test_input)
with open("data/day9.txt", "r") as file:
    SIGNALS = input_parser(file.read())


def future_extrapolate_from_gradient(gradient_list):
    """List with the signal and all diffs until its only zeros
    Returns: the extrapolated value for the signal at list[0] by summing all 
    gradients with the last signal value"""
    diff_transfer = [n_order_grad[-1]
                     for n_order_grad in reversed(gradient_list)]
    return sum(diff_transfer)


def past_extrapolate_from_gradient(gradient_list):
    """List with the signal and all diffs until its only zeros
    Returns: the extrapolated value for the signal at list[0] by summing all 
    gradients with the last signal value"""
    diff_transfer = [n_order_grad[0]
                     for n_order_grad in reversed(gradient_list)]

    res = 0
    for i, v in enumerate(diff_transfer):
        res = v - res

    return res


new_timestep_extrapolates = []
past_timestep_extrapolates = []
for signal in SIGNALS:
    all_diffed = False
    curr_descent = [signal]
    i = 0
    while np.any(curr_descent[-1]):

        curr_descent.append(np.diff(curr_descent[i]))
        i += 1

    new_timestep_extrapolates.append(
        future_extrapolate_from_gradient(curr_descent))
    past_timestep_extrapolates.append(
        past_extrapolate_from_gradient(curr_descent))

print(new_timestep_extrapolates, sum(new_timestep_extrapolates))
print(past_timestep_extrapolates, sum(past_timestep_extrapolates))
