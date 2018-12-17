from math import sqrt

def average(int_set):
    return sum(int_set)/len(int_set)

def standard_deviation(int_set):
    average = average(int_set)
    return sqrt(sum([(i - average)**2 for i in int_set])/len(int_set))

def conditional_probability(p_a, p_b):
    return (p_a*p_b)/p_b

def bayes_probability(p_a, p_b):
    return conditional_probability(p_a, p_b) * p_b / p_a