import sys
import numpy as np

def __update_learning_rate__(lr, beta1, beta2):
    return lr * (np.sqrt(1 - beta2)/(1 - beta1))

def __update__(x, lr, new_value):
    return x - lr * new_value

def __weighted_average__(rho, grad_weight_aver, gradient):
    return rho*grad_weight_aver + (1-rho)*gradient

def __moment__(beta, current_gradient, gradient):
    return beta * current_gradient + gradient

def __reciprocal_sqrt__(val):
    epsilon = sys.float_info.epsilon
    return 1 / np.sqrt(np.array(val + epsilon, dtype=np.float))

