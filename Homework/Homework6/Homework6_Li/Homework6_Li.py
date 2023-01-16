# Homework 6
# Jiayin(Crystal) Li
import numpy as np
import math as m
import numpy.random as R
from collections import Counter


# %% Q2 (a)
def stem_and_leaf(pltdata):
    """this function passes data as a parameter and creates a list that holds the stem and leaf plot"""
    data_sor = np.sort(pltdata)  #sort the data from the smallest to largest
    leaves_lst = []  #initializing a list that stores the leaves for each stem
    leaves_total = []  #initializing a list that stores all the leaves

    # creating the stem list
    if data_sor[0] < 0:
        start = round(data_sor[0] / 10)
    else:
        start = int(data_sor[0] / 10)
    if data_sor[-1] < 0:
        end = round(data_sor[-1] / 10)
    else:
        end = int(data_sor[-1] / 10)

    stem_lst = list(range(start, end + 1))  # creating a numpy array that stores all the stems

    for num in data_sor:
        if -10 < num < 0:
            stem_lst = list(range(start, end + 1))
            zero_idx = stem_lst.index(0)
            stem_lst.insert(zero_idx, m.copysign(0, -1))  #inserting a stem of -0 if there are number between -10 and 0
            break
        else:
            continue

    # looping through the sorted data to complete the leaves list for each stem
    for stem in stem_lst:
        for num in data_sor:
            if num > 0:
                if str(m.floor(num) // 10) == str(stem):
                    leaves_lst.append(round(abs(num) % 10))
            elif -10 < num < 0:
                if str(m.copysign(round(num / 10), num)) == str(stem):
                    leaves_lst.append(round(abs(num) % 10))
            else:
                if round(num / 10) == stem:
                    leaves_lst.append(round(abs(num) % 10))
        leaves_total.append(leaves_lst)
        leaves_lst = []

    # create a numpy array that stores the stems and the leaves in a single variable
    stem_leaves = list(zip(stem_lst, leaves_total))
    return stem_leaves

# %% Q2 (a)
# test cases for the passing data function
data = np.array([68, 47, 63, 76, 44, 64, 81, 66, 106, 68, 72, 72, 46, 75, 49, 84, 88])
data1 = np.array([-23.75858, -12.45, -3.4, 4.43, 5.5, 5.678, 16.87, 24.7, 56.8])
print(stem_and_leaf(data))
print(stem_and_leaf(data1))


# %% Q2 (b)
def plot_stem_and_leaf(stem_leaves):
    """this function takes in the data structure that stores the stem and leaf plot and print out the formatted plot"""
    for tpl in stem_leaves:
        if str(tpl[0]) == "-0.0":
            print("-0", " |  ", end="")
        else:
            print(f"{tpl[0]:2}", " |  ", end="")
        for leaf in tpl[1]:
            print(leaf, end=" ")
        print()


# %% Q2 (b)
# test cases for plotting function
plot1 = stem_and_leaf(data)
plot2 = stem_and_leaf(data1)
plot_stem_and_leaf(plot1)
print()
plot_stem_and_leaf(plot2)


# %% Q3 (a)

# setting the seed
R.seed(3788232)


def gen_stop_signal(p, delay, n):
    """This is a function that takes in the probability p of each trial being a GO or a STOP trial,
    an array of Stop Signal Delays on STOP trials, and a number of experimental trials N. The function will return
    an array of conditions so that -1 is a GO trial and a positive number of stop delay indicates a STOP trial.
    """
    conditions = np.zeros(n, dtype=int)  # creating a numpy array to store the conditions
    num_delay = len(delay)  # the number of possible delay signal values

    for i in range(n):
        rnd = R.uniform()  # using Bernoulli process to generate conditions
        if rnd < p:
            conditions[i] = -1
        else:
            rnd1 = R.randint(0, num_delay)
            conditions[i] = delay[rnd1]
    return conditions


# %% Q3 (a)
# test case for gen_stop_signal function
p = 0.8
delays = np.array([50, 100, 150], dtype=int)
N = 100000
condition1 = gen_stop_signal(p, delays, N)
print(condition1)


# %% Q3 (b)
def random_check(arr_conditions):
    """This function checks the randomization of an array of conditions by counting the numbers in each category and
    calculate proportion"""
    c = Counter(arr_conditions)  # use Counter to count the number of conditions in each category
    go_trials = c[-1]
    stop_trials = len(arr_conditions) - c[-1]
    print(f"The proportion of GO vs. STOP trials is {go_trials / stop_trials}")
    print(f"The proportion fo GO vs. All trials is {go_trials / len(arr_conditions)}")
    print(c)  # print out the tally of the number of go trials and stop trials at different signal delays


# %% Q3 (b)
# Test case
print(random_check(condition1))
# We have verified that our conditions are randomized


# %% Q4
def rand_perm(N):
    """This function returns a random permutation of integers in the sequence from 1 to N"""
    lst = list(range(1, N + 1))
    perm = []
    while N >= 1:
        num = R.randint(1, N + 1)
        perm.append(lst.pop(num - 1))
        N -= 1
    return perm


# %% Q4
# Test case for Q4
print(rand_perm(5))


# %% Q5
def constr_random(Nconds, Nreps):
    """This function performs a constrained randomization of the order of conditions in the experiment"""
    lst_con = list(range(Nconds))  # create a list that stores all the possible conditions left
    count_conds = dict()
    for cond in lst_con:
        count_conds[cond] = Nreps  # create a dictionary that maps all conditions to their number left to generate

    Ntrials = Nconds * Nreps
    trials = np.zeros(Ntrials, dtype=int)  # create a numpy array to store the generated trial
    prev = -1
    for i in range(Ntrials):
        trials[i] = R.choice(lst_con)
        while trials[i] == prev:
            # specify conditions when more than one of a specific condition are left at the end
            # and repetition is inevitable. Ask to rerun the function so that a new random process
            # initiated.
            if len(lst_con) == 1 and count_conds[trials[i]] > 0:
                return "please rerun the function"
            else:
                trials[i] = R.choice(lst_con)
        count_conds[trials[i]] -= 1  # decrease the count of the condition by 1
        if count_conds[trials[i]] == 0:
            lst_con.remove(trials[i])  # if the count of the condition is 0, remove it from the generation list
        prev = trials[i]

    return trials


# %% Q5
# test case for Q5
con_trial = constr_random(4, 20)
print(con_trial)


# %% Q5
def check_con(constr_trial):
    """This is a function that checks the constrained randomization function works properly"""
    prev = -1
    for i in constr_trial:
        cond = constr_trial[i]
        if cond != prev:
            continue
        else:
            print("There is a repeat")
    print("There is no repeat")
    counter = Counter(constr_trial)
    print(counter)


# %% Q5
print(check_con(con_trial))